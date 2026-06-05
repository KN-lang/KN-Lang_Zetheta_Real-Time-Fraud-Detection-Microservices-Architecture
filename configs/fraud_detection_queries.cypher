// 1. Community detection candidate: customers sharing device, IP, phone, or email signals
MATCH (c:Customer)-[:USES|LOGGED_IN_FROM|HAS_PHONE|HAS_EMAIL]->(s)<-[:USES|LOGGED_IN_FROM|HAS_PHONE|HAS_EMAIL]-(other:Customer)
WHERE c <> other
RETURN c.customer_id AS customer, labels(s) AS shared_signal, count(DISTINCT other) AS connected_customers
ORDER BY connected_customers DESC LIMIT 50;

// 2. Centrality candidate: devices or IPs connected to many customers and blocked transactions
MATCH (s)<-[:USES|LOGGED_IN_FROM]-(c:Customer)-[:INITIATED]->(t:Transaction {decision: 'BLOCK'})
WHERE s:Device OR s:IP
RETURN labels(s) AS signal_type, s.device_id AS device_id, s.ip_address AS ip_address, count(DISTINCT c) AS customers, count(t) AS blocked_transactions
ORDER BY customers DESC LIMIT 25;

// 3. Path analysis: shortest path from transaction customer to known fraud customer
MATCH (c:Customer {customer_id: $customer_id}), (f:Customer {confirmed_fraud: true})
MATCH p = shortestPath((c)-[*..4]-(f))
RETURN p LIMIT 25;

// 4. Temporal analysis: rapid card, account, or device cycling in one hour
MATCH (c:Customer)-[:USES]->(d:Device)<-[:USES]-(other:Customer), (c)-[:INITIATED]->(t:Transaction)
WHERE t.occurred_at >= datetime() - duration('PT1H')
RETURN d.device_id AS device, count(DISTINCT c) + count(DISTINCT other) AS customers, count(t) AS recent_transactions
ORDER BY recent_transactions DESC LIMIT 50;

// 5. Fraud topology matching: many accounts paying one merchant after shared address linkage
MATCH (addr:Address)<-[:HAS_ADDRESS]-(c:Customer)-[:OWNS]->(a:Account)-[:INITIATED]->(t:Transaction)-[:PAID]->(m:Merchant)
WITH addr, m, count(DISTINCT a) AS accounts, sum(t.amount) AS total_amount
WHERE accounts >= 5 AND total_amount > 100000
RETURN addr.address_hash AS address, m.merchant_id AS merchant, accounts, total_amount
ORDER BY total_amount DESC LIMIT 25;

// 6. Mule account pattern: many customers transferring to the same account
MATCH (c:Customer)-[:OWNS]->(:Account)-[:TRANSFERRED_TO]->(target:Account)
WITH target, count(DISTINCT c) AS source_customers
WHERE source_customers >= 5
RETURN target.account_id AS suspected_mule_account, source_customers
ORDER BY source_customers DESC LIMIT 25;
