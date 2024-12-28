import requests

class SolanaClient:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def send_request(self, method, params):
        return requests.post(self.rpc_url, json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1}).json()
