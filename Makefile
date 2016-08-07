all:
	@echo "Opciones:"
	@echo "	Exportar base de datos ----> export"
	@echo "Migraciones -----> migrate"
	@echo "Iniciar app -----> start"

export:
	python libmasys/manage.py dumpdata --indent 2 --format xml > libmasys/data/database.xml

migrate:
	python libmasys/manage.py makemigrations -y
	python libmasys/manage.py migrato --run-syncdb -y

start:
	python libmasys/manage.py runserver


heroku:
	sudo apt-get install wget
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	cd ..
	sudo heroku login
	sudo heroku create
	sudo git add .
	sudo git commit -m "heroku despliegue remoto"
	sudo git push heroku master
	sudo heroku run python manage.py syncdb --noinput
	sudo heroku ps:scale web=1
