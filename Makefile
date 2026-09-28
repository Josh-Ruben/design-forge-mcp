# Makefile

.PHONY: python java run

python:
	cd python && python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -e .

java:
	cd java && ./mvnw clean package

run:
	python -m design_forge.server
