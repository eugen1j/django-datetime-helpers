test:
	python -m pytest --cov-report term --cov=django_datetime_helpers tests.py
	python -m mypy django_datetime_helpers --ignore-missing-imports
	python -m flake8 django_datetime_helpers

build:
	python setup.py sdist bdist_wheel

upload:
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

test-upload:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*