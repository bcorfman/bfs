SHELL := env PYTHON_VERSION=$(PYTHON_VERSION) /bin/bash
.SILENT: install test lint format
PYTHON_VERSION ?= 3.10

cloudinstall:
	curl -sSL https://install.python-poetry.org | python3 -
	$(HOME)/.local/bin/poetry install
	$(HOME)/.local/bin/poetry run playwright install-deps
	$(HOME)/.local/bin/poetry run playwright install

install:
	curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
	$(HOME)/.rye/shims/rye pin $(PYTHON_VERSION)
	$(HOME)/.rye/shims/rye sync 


test:
	$(HOME)/.rye/shims/rye run pytest -m unit --cov-branch --cov-report term --cov=core tests/
	rm -f .coverage

cloudtest:
	$(HOME)/.local/bin/poetry run pytest -m system tests/

lint:
	$(HOME)/.rye/shims/rye run pylint main.py ./core

format:
	$(HOME)/.rye/shims/rye run black main.py core tests
	$(HOME)/.rye/shims/rye run yapf --in-place --recursive main.py core tests

run:
	$(HOME)/.rye/shims/rye run streamlit run main.py
	
all: install lint test
