build:
	docker-compose up --build
stop:
	docker-compose stop

clean:
	docker-compose down -v --rmi all
