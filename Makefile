SHELL=/bin/bash

setup: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt

run: .venv
	. venv/bin/activate; export FLASK_APP=main; export FLASK_ENV=development; flask run