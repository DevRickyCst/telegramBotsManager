local:
	uv run chalice local

deploy:
	uv run chalice deploy

lint:
	uv run ruff check --fix