# Every service in this repository exposes the same targets. That uniform
# interface is what lets one reusable workflow build all of them without
# knowing anything about Python.
.PHONY: install lint fmt typecheck test coverage

install:
	uv sync --extra dev

lint:
	uv run ruff check .
	uv run ruff format --check .

fmt:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run mypy src

test:
	uv run pytest

coverage:
	uv run pytest --cov=api --cov-report=term --cov-report=xml
