from daemon.subroutines import parse_args, load_store
from daemon import app

store = load_store()
args = parse_args()

if args.peer:
    store.add_peer(args.peer)

print(store)
store.join()

app.run(port=11381)
