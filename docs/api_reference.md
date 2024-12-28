# API Reference

## Solana Client
### Methods:
- `send_request(method: str, params: list)`
  Sends a JSON-RPC request to the Solana blockchain.

### Example:
```python
client = SolanaClient("https://api.mainnet-beta.solana.com")
response = client.send_request("getBalance", ["YourPublicKey"])
