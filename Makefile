.SILENT: install test lint format

install:
	python -m pip install --upgrade pip
	pip install poetry
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.prefer-active-python true 
	poetry install --no-root
	poetry run playwright install
test:
	poetry run pytest --cov-branch --cov-report term --cov-report lcov --cov=core tests/
	rm .coverage*

lint:
	poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	poetry run yapf --in-place --recursive --style pep8 *.py

run:
	poetry run python main.py
	
all: install lint test