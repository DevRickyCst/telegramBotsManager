local:
	AWS_PROFILE=perso uv run chalice local

deploy:
	AWS_PROFILE=perso uv run chalice deploy

lint:
	uv run ruff check --fix

mypy:
	uv run mypy chalicelib
