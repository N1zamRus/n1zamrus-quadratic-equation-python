.DEFAULT_GOAL := test

PYTHON ?= python3

.PHONY: setup test

setup:
	$(PYTHON) -m pip install -r requirements-dev.txt

test:
	$(PYTHON) -m pytest -q
