from __future__ import annotations

from pathlib import Path

import pandas as pd
import typer
from rich.console import Console

from fraud_platform.anomaly.anomaly_detector import AnomalyDetector
from fraud_platform.cases.case_manager import CaseManager
from fraud_platform.config import load_rules_config
from fraud_platform.events.event_handlers import run_event_pipeline as execute_event_pipeline
from fraud_platform.graph.graph_analyzer import GraphAnalyzer
from fraud_platform.reports.report_writer import ReportWriter
from fraud_platform.rules.rule_engine import RuleEngine
from fraud_platform.scoring.risk_scorer import RiskScorer
from fraud_platform.simulation.transaction_generator import generate_sample_data

app = typer.Typer(help="Local fraud detection simulation pipeline.")
console = Console()


@app.command("generate-data")
def generate_data(records: int = typer.Option(1000, min=1), output: Path = typer.Option(Path("data/generated"))):
    outputs = generate_sample_data(records=records, output_dir=output)
    console.print(f"Generated {records} transactions in {output}")
    for name, path in outputs.items():
        console.print(f"- {name}: {path}")


@app.command("score-transactions")
def score_transactions(
    transactions: Path = typer.Option(Path("data/generated/transactions.csv"), exists=True),
    output: Path = typer.Option(Path("data/output")),
    rules: Path = typer.Option(Path("config/rules.yaml"), exists=True),
):
    paths = run_scoring(transactions, output, rules)
    console.print(f"Reports written to {output}")
    for name, path in paths.items():
        console.print(f"- {name}: {path}")


@app.command("simulate-attack")
def simulate_attack(attack_type: str = typer.Option("velocity")):
    messages = {
        "velocity": "Velocity attack: one customer attempts more than five payments within ten minutes.",
        "shared-device": "Shared-device attack: many customer IDs transact from a single device fingerprint.",
        "mule": "Mule account pattern: many customers route transfers through one account.",
    }
    console.print(messages.get(attack_type, f"Unknown attack type '{attack_type}'. Try velocity, shared-device, or mule."))


@app.command("run-pipeline")
def run_pipeline(records: int = typer.Option(1000, min=1), generated: Path = typer.Option(Path("data/generated")), output: Path = typer.Option(Path("data/output"))):
    generate_sample_data(records=records, output_dir=generated)
    paths = run_scoring(generated / "transactions.csv", output, Path("config/rules.yaml"))
    console.print(f"Pipeline completed for {records} records")
    console.print(f"Summary: {paths['summary']}")


@app.command("run-event-pipeline")
def run_event_pipeline(records: int = typer.Option(1000, min=1), generated: Path = typer.Option(Path("data/generated")), output: Path = typer.Option(Path("data/output"))):
    generate_sample_data(records=records, output_dir=generated)
    transactions = pd.read_csv(generated / "transactions.csv")
    paths = execute_event_pipeline(transactions, output, Path("config/rules.yaml"))
    console.print(f"Event pipeline completed for {records} records")
    console.print(f"Event log: {paths['event_log']}")
    console.print(f"Event summary: {paths['event_pipeline_summary']}")


def run_scoring(transactions_path: Path, output_dir: Path, rules_path: Path) -> dict[str, Path]:
    transactions = pd.read_csv(transactions_path)
    config = load_rules_config(rules_path)
    rule_hits = RuleEngine(config).evaluate(transactions)
    anomaly_alerts = AnomalyDetector().detect(transactions)
    _, graph_alerts = GraphAnalyzer(
        shared_device_threshold=config["rules"]["shared_device_many_customers"]["threshold"],
        shared_ip_threshold=config["rules"]["same_ip_many_customers"]["threshold"],
    ).analyze(transactions)
    risk_scores = RiskScorer().score(transactions, rule_hits, anomaly_alerts, graph_alerts)
    fraud_cases = CaseManager().create_cases(risk_scores)
    return ReportWriter().write(output_dir, risk_scores, fraud_cases, rule_hits, anomaly_alerts, graph_alerts, len(transactions))
