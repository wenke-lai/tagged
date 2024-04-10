pipeline: unittest delivery integration e2e

# ##############################
# Unit Tests
# ##############################

unittest: format lint test security

format-check:
	poetry run black server/ --check --diff --extend-exclude migrations
	poetry run isort server/ --check-only --diff

format:
	poetry run black server/ --extend-exclude migrations
	poetry run isort server/

lint:
	poetry run pylint server/*
	poetry run mypy server/

test:
	# poetry run pytest --cov=server server/

security:
	poetry run bandit -r server/ -c pyproject.toml
	poetry run safety check --full-report

# ##############################
# Delivery
# ##############################

delivery: requirements

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

requirements-dev:
	poetry export -f requirements.txt --output requirements.txt --with dev --without-hashes

# ##############################
# Integration Test
# ##############################

integration:
	@echo "TBD"

# ##############################
# E2E Test
# ##############################

e2e:
	@echo "TBD"

# ##############################
# Other commands
# ##############################

reset:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -f server/db.sqlite3
	python server/manage.py makemigrations
	python server/manage.py migrate
	# python server/manage.py createsuperuser
