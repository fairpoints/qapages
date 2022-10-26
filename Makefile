init:
	pip install --upgrade pip-tools pip setuptools
	pip install --editable src/
	pip install --upgrade -r requirements/main.txt  -r requirements/dev.txt

update-deps:
	pip install --upgrade pip-tools pip setuptools
	pip-compile --upgrade --build-isolation --generate-hashes --output-file \
		requirements/main.txt requirements/main.in
	pip-compile --upgrade --build-isolation --generate-hashes --output-file \
		requirements/dev.txt requirements/dev.in

update: update-deps init

up-dev:
	docker-compose up --build --force-recreate --detach --remove-orphans

mongodump:
	docker-compose exec mongo \
		mongodump -u $(MONGO_USERNAME) -p $(MONGO_PASSWORD) \
		--gzip --archive > mongodump.gz

mongorestore:
	docker-compose exec -T mongo \
		mongorestore -u $(MONGO_USERNAME) -p $(MONGO_PASSWORD) \
		--gzip --archive --drop < mongorestore.gz