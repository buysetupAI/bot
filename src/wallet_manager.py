class WalletManager:
    def __init__(self, wallets_config):
        self.wallets = wallets_config

    def get_wallet_by_name(self, name):
        return next(wallet for wallet in self.wallets if wallet['name'] == name)

    def check_limit(self, wallet_name, amount):
        wallet = self.get_wallet_by_name(wallet_name)
        return amount <= wallet['max_limit']
