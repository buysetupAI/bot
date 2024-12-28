from src.order_manager import OrderManager
from src.wallet_manager import WalletManager
from src.solana_client import SolanaClient

def test_place_order():
    solana_client = SolanaClient("http://mock-rpc")
    wallet_manager = WalletManager([])
    manager = OrderManager(solana_client, wallet_manager)
    assert manager.place_order("TOKEN", 10) is None
