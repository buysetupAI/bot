import pytest
from src.wallet_manager import WalletManager

def test_check_limit():
    wallets_config = [
        {"name": "Test Wallet", "max_limit": 100}
    ]
    manager = WalletManager(wallets_config)
    assert manager.check_limit("Test Wallet", 50) is True
    assert manager.check_limit("Test Wallet", 150) is False
