.PHONY: test


lint:
	flake8

test-no-migrations:
	-make lint
	pytest --nomigrations -s

test:
	-make lint
	pytest -s

docker-build:
	docker-compose up -d
