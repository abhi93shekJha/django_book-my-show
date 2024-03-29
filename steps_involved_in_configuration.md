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
   docker-compose up (this will start all the services mentioned in docker-compose)
6. Configuring Github actions. Similar to Travis-CI, GitLab CI/CD, Jenkins. When code changes, we run tasks.
   Useful for automating certain tasks. Common uses, to run Deployment, Code Linting, Unit tests. All automatically.
   We will create config file at .github/workflows/checks.yml (this yml file can be named anything other than checks).
   Then we will set trigger in config file, and add steps for running testing and linting.
   We will then setup docker hub authentication.
7. Docker hub is where we pull base images from (by default).
   From an IP, docker hub allows to pull 100 images/6 hours. If logged in (authenticated user), 200 images/6 hours.
   Github Action uses shared IP address, so many users (1000s) have same IP, hence limit will be reached immediately.
   So, we authenticate ourselves from our github account to get a limit of 200 pulls/6 hours which is more than enough for most projects.
8. Register to docker hub. Then we will add secrets to our GitHub project.
   Secrets are nothing but encrypted authentication credentials to access docker hub.
   Not visible to the user, but gets decrypted automatically when we do some job (interating with docker hub).
