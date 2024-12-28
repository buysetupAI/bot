# Strategies

## Dollar-Cost Averaging (DCA)
A method of investing a fixed amount in a token at regular intervals, reducing the impact of volatility.

### Configuration Example:
```yaml
tokens:
  - symbol: "TOKEN"
    strategy: "DCA"
    amount: 100
    intervals: 5
```

### Workflow:
1. Divide the total investment amount by the number of intervals.
2. Execute a purchase at each interval.

### Benefits:
- Reduces the risk of investing at a single high price.
- Smoothens the entry into volatile markets.
