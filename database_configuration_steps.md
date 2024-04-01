
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
- We will then configure Django, to tell it how to connect to db. We will do it insided settings.py, provide it to DATABASES variable. It takes in database engine name (postgresql in our case), Host name, Database name(as there can be multiple dbs present), user and password.
- Environment variable can be easily passed to docker container (see in docker-compose file). We are using these same env. variables inside django settings.py using (os.environ.get('DB_HOST'), here getting db HOST info from docker-compose to settings.py).
- These variables can be set in local env (as set in docker-compose), as well as in production evironment.
- With env. variables all the configurations are done at a single place and it is pulled with code whereever needed (as env. variable from our container is being used in settings.py for db connection in our project).
- Hence, we can change it at a single place (for local or for dev env.) and no need to change at other places.
- Install Postgresql adapter, which django uses to connect to postgres database.
- For this we need Psycopg2, which is a package needed for Django to connect to our Database. This is also called database adapter.
- Psycopg2 is most popular adapter for db connection supported by django officially.
- We can either download psycopg2-binary, where we won't have to install any other dependencies and it comes with all the dependencies.
- But this is not good for production as it is not optimized for the os it is running on (so slow performance).
- Other is psycopg2, which has good performace as it is compiled from source code when installed and it is compiled for specific os where it is running.
- But for installing this we will need few dependencies that it uses for its installation. We have configured this in our docker file.
- Once these instructions are mentioned in docker file, we won't have to change it for other machines, as docker uses its own base os, slim-buster for our project.
- List of packages needed to install psycopg2 are C compile, python3-dev and libpq-dev. Unfortunately they come with different names for our slim-buster package manager.
- We will first get these 3 mentioned packages, which are only useful for installing psycopg2 and then delete these for keeping container lightweight. Read in dockerfile.
- Finally we will add psycopg2 in requirements.txt.
