test:
	python -m pytest --cov-report term --cov=django_datetime_helpers tests.py
	python -m mypy django_datetime_helpers.py --ignore-missing-imports
	python -m flake8 django_datetime_helpers.py

