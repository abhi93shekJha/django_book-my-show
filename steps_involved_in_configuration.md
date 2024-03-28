1. Created a dockerfile.
2. Created docker-compose.yml
3. Create requirements.dev.txt to mention flake8, to install it with docker just for development purpose.
   requirements.dev.txt will ensure that we only need those packages that is necessary for development and not for deployment.
4. Adding .flake8 file for excluding files from linting.

   docker-compose run --rm app sh -c "flake8 /app"

   Running flake with the above command. app is service name (defined inside docker-compose)
   /app is where my code is mounted inside the container. sh -c starts a shell inside container and runs
   the flake8 command. --rm is removing the container (app) once this command finishes running.
5. docker-compose run app (this will only run app service)
   docker-compose up (this will start all the sevices mention in docker-compose)
6. Configuring Github actions. Similar to Travis-CI, GitLab CI/CD, Jenkins. When code changes, we run tasks.
   Useful for automating certain tasks. Common uses, to run Deployment, Code Linting, Unit tests. All automatically.
   We will cre
