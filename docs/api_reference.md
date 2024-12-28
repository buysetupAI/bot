# API Reference

## Solana Client
### Methods:
- `send_request(method: str, params: list)`
  Sends a JSON-RPC request to the Solana blockchain.

### Example:
```python
client = SolanaClient("https://api.mainnet-beta.solana.com")
response = client.send_request("getBalance", ["YourPublicKey"])
```

## Wallet Manager
### Methods:
- `get_wallet_by_name(name: str)`
  Retrieves wallet details by its name.
- `check_limit(wallet_name: str, amount: float)`
  Checks if the amount exceeds the wallet's limit.

## Order Manager
### Methods:
- `place_order(token: str, amount: float)`
  Places an order to buy a specified token.

## Strategy Manager
### Methods:
- `execute_strategy(strategy_config: dict)`
  Executes the given strategy configuration.
