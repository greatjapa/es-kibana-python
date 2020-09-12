
build:
	docker build -f Dockerfile -t test:latest .

up:
	docker-compose up

down:
	docker-compose down
