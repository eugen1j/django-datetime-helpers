test:
	./venv/bin/python -m pytest --cov-report term --cov=django_datetime_helpers tests.py
	./venv/bin/python -m mypy django_datetime_helpers.py --ignore-missing-imports
	./venv/bin/python -m flake8 django_datetime_helpers.py

