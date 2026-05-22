# 08. Graph Analysis Design

## Prototype Implementation
The prototype builds an in-memory graph using **NetworkX**.
- **Entities as Nodes**: Customers, Accounts, Devices, IPs, Merchants.
- **Relationships as Edges**: OWNS, USES, CONNECTS_FROM, PAYS.
- **Detection Logic**:
  - **Shared Entities**: Identifies IPs or Devices linked to an excessive number of customers.
  - **Mule Accounts**: Identifies accounts receiving funds from many distinct customers.
  - **Suspicious Clusters**: Identifies dense subgraphs that suggest organized fraud rings.

## Production Design
The production service will utilize a persistent Graph Database (**Neo4j**).
- **Real-time Ingestion**: Transaction events update the graph in near real-time.
- **Cypher Queries**: Complex relationship patterns are detected using optimized graph traversal queries (Cypher).
- **Graph Embeddings**: Future iterations will use Graph Neural Networks (GNNs) to detect suspicious subgraphs automatically.
