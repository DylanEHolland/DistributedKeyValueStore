class DistributedStore(object):
    def __init__(self):
        self.peers = []
        self.connected_peers = set()
        self.store = {}

    def __str__(self):
        return f"<DistributedStore peers: {self.peers}>"

    def add_peer(self, ip_address):
        if ip_address not in self.peers and type(ip_address) == str:
            self.peers.append(ip_address)

    def join(self):
        pass

    def serve(self):
        pass


class Client(object):
    def connect(self):
        pass

    def get(self, key):
        pass

    def set(self, key, value):
        pass