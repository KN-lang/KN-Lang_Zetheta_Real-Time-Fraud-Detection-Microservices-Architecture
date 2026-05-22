from __future__ import annotations

import networkx as nx
import pandas as pd


class GraphAnalyzer:
    def __init__(self, shared_device_threshold: int = 4, shared_ip_threshold: int = 5, mule_account_threshold: int = 6):
        self.shared_device_threshold = shared_device_threshold
        self.shared_ip_threshold = shared_ip_threshold
        self.mule_account_threshold = mule_account_threshold

    def analyze(self, transactions: pd.DataFrame) -> tuple[nx.Graph, pd.DataFrame]:
        graph = self.build_graph(transactions)
        if transactions.empty:
            return graph, self._empty()
        alerts: list[dict[str, object]] = []
        self._shared_entities(transactions, alerts, "device_id", "SHARED_DEVICE", self.shared_device_threshold)
        self._shared_entities(transactions, alerts, "ip_address", "SHARED_IP", self.shared_ip_threshold)
        self._mule_accounts(transactions, alerts)
        self._clusters(graph, alerts)
        return graph, pd.DataFrame(alerts).drop_duplicates(subset=["entity_id", "alert_type"]) if alerts else self._empty()

    def build_graph(self, transactions: pd.DataFrame) -> nx.Graph:
        graph = nx.Graph()
        for row in transactions.itertuples(index=False):
            customer = f"customer:{row.customer_id}"
            account = f"account:{row.account_id}"
            device = f"device:{row.device_id}"
            ip = f"ip:{row.ip_address}"
            merchant = f"merchant:{row.merchant_id}"
            txn = f"transaction:{row.transaction_id}"
            graph.add_edge(customer, account, relationship="OWNS")
            graph.add_edge(customer, device, relationship="USES")
            graph.add_edge(customer, ip, relationship="CONNECTS_FROM")
            graph.add_edge(customer, merchant, relationship="PAYS")
            graph.add_edge(account, txn, relationship="HAS_TRANSACTION")
        return graph

    def _shared_entities(self, df: pd.DataFrame, alerts: list[dict[str, object]], column: str, alert_type: str, threshold: int) -> None:
        for entity_id, group in df.groupby(column):
            customer_count = group["customer_id"].nunique()
            if customer_count > threshold:
                alerts.append(
                    {
                        "entity_id": entity_id,
                        "alert_type": alert_type,
                        "severity": "HIGH",
                        "reason": f"{column} is linked to {customer_count} customers",
                        "related_transactions": ",".join(group["transaction_id"].astype(str).head(25)),
                    }
                )

    def _mule_accounts(self, df: pd.DataFrame, alerts: list[dict[str, object]]) -> None:
        for account_id, group in df.groupby("account_id"):
            sender_count = group["customer_id"].nunique()
            if sender_count > self.mule_account_threshold:
                alerts.append(
                    {
                        "entity_id": account_id,
                        "alert_type": "MULE_ACCOUNT_PATTERN",
                        "severity": "HIGH",
                        "reason": f"Account is associated with {sender_count} customers",
                        "related_transactions": ",".join(group["transaction_id"].astype(str).head(25)),
                    }
                )

    def _clusters(self, graph: nx.Graph, alerts: list[dict[str, object]]) -> None:
        for idx, component in enumerate(nx.connected_components(graph)):
            customer_nodes = [node for node in component if node.startswith("customer:")]
            device_nodes = [node for node in component if node.startswith("device:")]
            ip_nodes = [node for node in component if node.startswith("ip:")]
            if len(customer_nodes) >= 8 and (len(device_nodes) <= 3 or len(ip_nodes) <= 3):
                alerts.append(
                    {
                        "entity_id": f"cluster:{idx}",
                        "alert_type": "SUSPICIOUS_CLUSTER",
                        "severity": "MEDIUM",
                        "reason": f"Cluster links {len(customer_nodes)} customers through concentrated devices/IPs",
                        "related_transactions": "",
                    }
                )

    @staticmethod
    def _empty() -> pd.DataFrame:
        return pd.DataFrame(columns=["entity_id", "alert_type", "severity", "reason", "related_transactions"])
