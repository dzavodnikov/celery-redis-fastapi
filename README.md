# Description

This project show how to run [Celery](https://docs.celeryq.dev/) on [Redis](https://redis.io/)
with [FastAPI](https://fastapi.tiangolo.com/) in [Docker](https://www.docker.com/).

## How to run

1. Run all containers using [Docker Compose](https://docs.docker.com/compose/):

   ```bash
    docker-compose up
   ```

   To stop the Docker use following command:

   ```bash
   docker-compose down
   ```

2. Go to <http://localhost:8080/docs> to see [Swagger UI](https://swagger.io/tools/swagger-ui/)
   and prepare the requests.

3. Execute request `/sum` to start task and receive task ID.

4. Receive the data using request `/result` with task ID parameter.

## Monitoring Celery using Flower

To run [Flower](https://flower.readthedocs.io/):

1. Execute following commend into the PIP:

   ```bash
   celery --broker=redis://localhost:6379/0 flower --port=5555
   ```

2. Go to <http://localhost:5555>.

## Connect to Redis

You are can connect to Redis server using binding port `6379`.

## Developing under Windows

Note that current configuration map Celery (from `celery` directory) and FastAPI script (from
`server` directory) into the Docker, but windows not send update actions to Docker.

So, after updating the mapped files go to proper container and execute:

```bash
touch rest.py
```

```bash
touch tasks.py
```
