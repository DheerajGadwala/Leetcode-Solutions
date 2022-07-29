Initially we can pick any of the n pickups. Then we can either pick the delivery for the pickup or any of the n-1 pickups.
​
Initial state => (n pickups, 0 deliveries) => (n, 0)
​
(n, 0) => (n-1, 1)[n choices]
(n-1, 1) => (n-2, 2)[n-1 choices] or (n-1, 0)[1 choice]
(n-2, 2) => (n-3, 3)[n-2 choices] or (n-2, 1)[2 choices]
....so on