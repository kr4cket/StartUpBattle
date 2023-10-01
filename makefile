.SILENT:

build-containers:
	docker-compose up -d --build telegram-bot

add-tables:
	yoyo apply --database postgresql://stbuser:stbuser@localhost:5436/data ./worker/migrations