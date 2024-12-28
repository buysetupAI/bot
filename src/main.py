from configparser import ConfigParser
from src.solana_client import SolanaClient
from src.wallet_manager import WalletManager
from src.order_manager import OrderManager
from src.strategies import StrategyManager
from src.ai_decision import AIDecision

def main():
    config = ConfigParser()
    config.read('config/config.yaml')

    solana_client = SolanaClient(config['rpc_url'])
    wallet_manager = WalletManager(config['wallets'])
    order_manager = OrderManager(solana_client, wallet_manager)
    strategy_manager = StrategyManager(order_manager)
    ai_decision = AIDecision(config['ai_settings'])

    while True:
        recommendations = ai_decision.get_recommendations()
        for recommendation in recommendations:
            strategy_manager.execute_strategy(recommendation)

if __name__ == "__main__":
    main()
