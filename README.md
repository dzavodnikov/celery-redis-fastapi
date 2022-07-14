# Description

This project show how to run [Celery](https://docs.celeryq.dev/) on [Redis](https://redis.io/)
with [FastAPI](https://fastapi.tiangolo.com/) in [Docker](https://www.docker.com/).

## Pre-configuration for developers

1. Create Python virtual environment:

   ```bash
   python -m venv venv
   ```

2. Switch to that virtual environment and istall all dependencies:

   ```bash
   (venv) pip install -r requirements.txt -c constraints.txt
   ```

## Run Celery

1. Execute steps from "Pre-configuration for developers".

2. Run Redis in Docker:

   ```bash
   docker run -d --name redis -p 6379:6379 redis:7.0.3
   ```
   
   You are can connect to Redis server using binding port `6379`.

3. Run Celery (that will restarting automatically after file modification):

   ```bash
   (venv) watchmedo auto-restart --directory=./celery --pattern=*.py --recursive -- celery --app celery/tasks worker --loglevel=INFO -E
   ```

4. Run [Flower](https://flower.readthedocs.io/) to monitoring Celery:

   ```bash
   (venv) celery --broker=redis://localhost:6379/0 flower --port=5555
   ```

5. Go to <http://localhost:5555> to see [Flower UI](https://flower.readthedocs.io/en/latest/screenshots.html).

6. Run REST server (that will updated automatically after file modification):

   ```bash
   (venv) uvicorn rest:app --host localhost --port 80 --workers 4 --reload
   ```

7. Go to <http://localhost:8080/docs> to see [Swagger UI](https://swagger.io/tools/swagger-ui/)
   and prepare the requests.

8. Execute request `/sum` to start task and receive task ID.

9. Receive the data using request `/result` with task ID parameter.

### Developing under Windows

Note that current configuration map Celery (from `celery` directory) and FastAPI script (from
`server` directory) into the Docker, but windows not send update actions to Docker.

So, after updating the mapped files go to proper container and execute:

```bash
touch rest.py
```

```bash
touch tasks.py
```

## Run environment into the Docker

1. Run all containers using [Docker Compose](https://docs.docker.com/compose/):

   ```bash
   docker-compose up
   ```

   To stop the Docker use following command:

   ```bash
   docker-compose down
   ```

2. Run [Flower](https://flower.readthedocs.io/) to monitoring Celery:

   ```bash
   (venv) celery --broker=redis://localhost:6379/0 flower --port=5555
   ```

3. Go to <http://localhost:5555> to see [Flower UI](https://flower.readthedocs.io/en/latest/screenshots.html).

4. Go to <http://localhost:8080/docs> to see [Swagger UI](https://swagger.io/tools/swagger-ui/)
   and prepare the requests.

5. Execute request `/sum` to start task and receive task ID.

6. Receive the data using request `/result` with task ID parameter.
