# Same targets as every other service in this repository. See app/api/Makefile.
.PHONY: install lint fmt typecheck test coverage

install:
	npm ci

lint:
	npm run lint
	npm run format:check

fmt:
	npm run format

typecheck:
	npm run build

test:
	npm run test

coverage:
	npm run test:coverage
