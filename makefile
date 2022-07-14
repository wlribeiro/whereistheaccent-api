export PYTHONPATH=.

crawl:
	python whereistheaccent/crawler/crawler.py

run:
	uvicorn whereistheaccent.api.api:app --reload

migration:
	alembic upgrade head
