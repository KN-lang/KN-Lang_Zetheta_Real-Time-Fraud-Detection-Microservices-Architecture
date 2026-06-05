# Day 07 - Rule Simulation Design

Rule simulation replays historical enriched transactions against candidate rules without emitting production decisions. Outputs include hit rate, false-positive estimate, customer impact, merchant impact, blocked amount, and overlap with existing rules. Simulation uses sampled traffic plus confirmed fraud and false-positive labels from case outcomes.
