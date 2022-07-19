export PYTHONPATH=.

crawl:
	python whereistheaccent/crawler/crawler.py

run:
	uvicorn server.server:app --reload

migration:
	alembic upgrade head

install:
	pip install -r requirements.txt

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down