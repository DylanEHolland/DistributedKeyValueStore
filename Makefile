run:
	@-FLASK_ENV="development" PYTHONPATH="./" python3 -m daemon

run_peer:
    @-FLASK_ENV="development" PYTHONPATH="./" python3 -m daemon -p 10.1.38.6;
