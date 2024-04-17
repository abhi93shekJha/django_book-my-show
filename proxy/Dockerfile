# We could have used 'nginx' instead of 'nginx-unprivileged' but by default this nginx image gives root access. So using the below mentioned image
# We should give as least assess as possible, so that there is no hacking possibility in future.
FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="abhi93shek.jha@gmail.com"

# copying are very obvious
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

# setting up environment variables to be used by default.conf.tpl file (which will be later saved to nginx defaulf.conf file)
# these are actually default values and can be overridden later (ofcourse using docker-compose, when we are running this service.).
ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

# switching to root user, to setup our image by running command mentioned below.
USER root

# chmod 755, will allow to read the content from static file
# then we are creating the configuration file(default.conf), which is mentioned in run.sh script (that is copying configurations from default.conf.tpl template to this file)
# giving access of this file to nginx user(this user is present as part of this base nginx image mentioned in the first line).
# finally giving executable permission to run.sh script for docker container to be able to run the script
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

# default volume that will be created for this image. Later we will be mapping this volume in docker-compose
VOLUME /vol/static

# switching back to nginx user (with least priviledge)
USER nginx

# default command that will be run by this docker-container
CMD ["/run.sh"]
