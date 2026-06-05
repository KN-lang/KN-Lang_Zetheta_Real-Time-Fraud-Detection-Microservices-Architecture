// 1. Customers sharing a device with confirmed fraud
MATCH (c:Customer)-[:USES]->(d:Device)<-[:USES]-(f:Customer {confirmed_fraud: true}) RETURN c, d, f LIMIT 50;
// 2. Mule cluster through shared beneficiary
MATCH (c1:Customer)-[:OWNS]->(:Account)-[:TRANSFERRED_TO]->(b:Beneficiary)<-[:TRANSFERRED_TO]-(:Account)<-[:OWNS]-(c2:Customer) WHERE c1 <> c2 RETURN c1, b, c2 LIMIT 50;
// 3. Shared IP burst across many customers
MATCH (c:Customer)-[:LOGGED_IN_FROM]->(ip:IPAddress) WITH ip, count(DISTINCT c) AS customers WHERE customers > 10 RETURN ip, customers;
// 4. High-risk merchant receiving blocked transactions
MATCH (t:Transaction {decision: 'BLOCK'})-[:PAID]->(m:Merchant) RETURN m, count(t) AS blocked ORDER BY blocked DESC LIMIT 20;
// 5. Short path from transaction customer to known fraud entity
MATCH p = shortestPath((c:Customer)-[*..4]-(f:Customer {confirmed_fraud: true})) RETURN p LIMIT 25;
// 6. Device cycling on one account
MATCH (a:Account)<-[:OWNS]-(:Customer)-[:USES]->(d:Device) WITH a, count(DISTINCT d) AS devices WHERE devices > 5 RETURN a, devices;
