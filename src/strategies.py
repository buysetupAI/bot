class StrategyManager:
    def __init__(self, order_manager):
        self.order_manager = order_manager

    def execute_strategy(self, strategy_config):
        if strategy_config['type'] == 'DCA':
            self._execute_dca(strategy_config)

    def _execute_dca(self, strategy_config):
        token = strategy_config['token']
        amount = strategy_config['amount']
        intervals = strategy_config['intervals']

        for i in range(intervals):
            self.order_manager.place_order(token, amount / intervals)
