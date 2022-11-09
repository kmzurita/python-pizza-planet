export

run:
	python3 manage.py run

install:
	pip3 install -r requirements.txt

test:
	pytest

init-db:
	python3 manage.py db init

migrate-db:
	python3 manage.py db migrate

upgrade-db:
	python3 manage.py db upgrade

empty-db:
	python3 manage.py db downgrade

seed-db:
	python3 manage.py db upgrade
	python3 manage.py seed_db