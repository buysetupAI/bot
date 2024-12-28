# AI BUY SETUP BOT

AI-powered trading bot for tokens on the Solana blockchain, offering features such as:
- Token purchasing with customizable wallet limits
- Dollar-Cost Averaging (DCA) strategies
- AI-driven token selection and strategy execution

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/ai-buy-setup.git
   cd ai-buy-setup
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot using the file `config/config.yaml`.

4. Start the bot:
   ```bash
   python src/main.py
   ```

## Configuration

Edit the `config/config.yaml` file to customize your settings.

Example configuration:
```yaml
rpc_url: "https://api.mainnet-beta.solana.com"
wallets:
  - name: "Main Wallet"
    public_key: "YourPublicKey"
    private_key: "YourPrivateKey"
    max_limit: 1000
tokens:
  - symbol: "TOKEN"
    address: "TokenAddress"
    strategy: "DCA"
ai_settings:
  enable: true
  model: "gpt-4"
  parameters:
    risk_tolerance: "medium"
    max_tokens: 10
```

## Features

- **AI-Driven Decisions**: Automatically identifies tokens and optimal strategies based on AI recommendations.
- **DCA Strategies**: Smooth investment through regular purchases.
- **Wallet Limits**: Ensures spending does not exceed predefined limits for each wallet.

## Project Structure

```plaintext
AI-BUY-SETUP/
│
├── README.md                 
├── .gitignore                
├── requirements.txt          
├── config/
│   ├── config.yaml           
│   ├── tokens.json           
│   └── wallets.json          
├── src/
│   ├── __init__.py
│   ├── main.py               
│   ├── strategies.py         
│   ├── solana_client.py      
│   ├── order_manager.py      
│   ├── wallet_manager.py     
│   ├── ai_decision.py        
│   └── utils.py              
├── tests/
│   ├── test_main.py          
│   ├── test_strategies.py    
│   ├── test_solana_client.py 
│   └── ...
└── docs/
    ├── architecture.md       
    ├── api_reference.md      
    └── strategies.md         
```

## Testing

Run tests to ensure all features are working as expected:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
