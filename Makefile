# Usage:
# 	make run
# 	make stop
.PHONY: up restart stop down bash ps

CONTAINER_NAME_WEB := app

up:
	docker compose up -d

restart:
	docker compose restart

stop:
	docker compose stop

down:
	docker compose down

bash:
	docker compose exec -it ${CONTAINER_NAME_WEB} bash

ps:
	docker compose ps
