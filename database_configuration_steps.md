
##### Using Postgres with Docker compose

- Using docker compose for postgres will allow us to define db configurations which can be reused by other developers and also be reusable for deployement environment.
- Docker compose will help persist data on our local (using volumes), until we clear it deliberately. It will help us test our code locally.
- It helps handling network. Handles opening ports and services interaction in docker-compose itself. Also helps specifying settings for environment variable.

##### Architecture

- We will have two services in our docker-compose.
- One for database (with postgres), another for our app (django).
- Both will communicate with each other.

##### Steps for database configuration:

- Create 'db' service inside docker-compose.
- Provide environment in both db and app services. See in docker-compose.
- Add volumes in db service.
-
