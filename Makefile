build:
	docker network create cc_frontend && docker network create cc_backend && docker compose up --build
	
stop:
	docker compose stop
	
clean:
	docker system prune -f || true && docker volume prune -f || true && docker rmi `docker images -aq` -f || true && docker container prune -f || true

