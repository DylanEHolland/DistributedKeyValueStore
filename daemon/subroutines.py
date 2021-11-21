from argparse import ArgumentParser
from dkvs.structures import DistributedStore


def load_store():
    store = DistributedStore()
    return store


def parse_args():
    ap = ArgumentParser()
    ap.add_argument("--peer", "-p")

    return ap.parse_args()


