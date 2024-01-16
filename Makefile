SHELL := env PYTHON_VERSION=$(PYTHON_VERSION) /bin/bash
.SILENT: install test lint format
PYTHON_VERSION ?= 3.10

install:
	curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
	$(HOME)/.rye/shims/rye pin $(PYTHON_VERSION)
	$(HOME)/.rye/shims/rye sync
	$(HOME)/.rye/shims/rye run playwright install

test:
	$(HOME)/.rye/shims/rye run pytest --cov-branch --cov-report term --cov=core tests/
	rm .coverage*

lint:
	$(HOME)/.rye/shims/rye run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	$(HOME)/.rye/shims/rye run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	$(HOME)/.rye/shims/rye run yapf --in-place --recursive main.py core tests

run:
	$(HOME)/.rye/shims/rye run streamlit run main.py
	
all: install lint test
