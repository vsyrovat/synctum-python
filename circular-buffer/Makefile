.PHONY: deps fmt checkfmt lint test clean demo

deps:
	pipenv install --dev

fmt:
	pipenv run isort --profile black .
	pipenv run black .

checkfmt:
	pipenv run black . --check --diff

lint:
	pipenv run black . --check --diff
	pipenv run mypy .

test:
	pipenv run pytest

clean:
	find . -type f -name '*.py[cod]' -delete -o -type d -name __pycache__ -delete

demo:
	python main.py demo/input1.txt
	python main.py demo/input2.txt
