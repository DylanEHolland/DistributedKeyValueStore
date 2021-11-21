from dkvs.structures import DistributedStore


def test_store_init():
    store = DistributedStore()
    store.add_peer("10.1.38.6")
    print(store)


if __name__ == "__main__":
    test_store_init()