all:
	@echo "Opciones:"
	@echo "	Exportar base de datos ----> export"
	@echo "Migraciones -----> migrate"
	@echo "Iniciar app -----> start"

export:
	python libmasys/manage.py dumpdata --indent 2 --format xml > libmasys/data/database.xml

migrate:
	python libmasys/manage.py makemigrations
	python libmasys/manage.py migrate --run-syncdb

start:
	python libmasys/manage.py runserver


heroku:
	sudo apt-get install wget
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	cd ..
	sudo heroku login
	sudo heroku create bibliodudar
	heroku buildpacks:set heroku/python
	$(MAKE) deploy

deploy:
	git add .
	git commit -m "heroku despliegue remoto"
	git push heroku master
	heroku run python libmasys/manage.py makemigrations
	heroku run python libmasys/manage.py migrate
	heroku ps:scale web=1
