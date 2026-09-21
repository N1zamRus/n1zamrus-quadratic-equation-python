.DEFAULT_GOAL := test

PYTHON ?= python3

.PHONY: test

test:
	$(PYTHON) -m pytest -q
