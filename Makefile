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
