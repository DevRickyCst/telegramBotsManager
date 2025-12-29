local:
	AWS_PROFILE=perso uv run chalice local

deploy:
	AWS_PROFILE=perso uv run chalice deploy

lint:
	uv run ruff check --fix

pyright:
	uv run pyright chalicelib