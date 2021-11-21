from dkvs.structures import DistributedStore


def test_store_init():
    store = DistributedStore()
    print(store)


if __name__ == "__main__":
    test_store_init()