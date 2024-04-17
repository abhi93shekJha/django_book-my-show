# this script will run our proxy server (load balancer)
# specifies that this is a shell script (called as shbang)
#!/bin/sh

set -e  # entire script will fail if any of the below commands fail

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf   # Substitute environment variables in the NGINX configuration template(default.conf.tpl) and write to the NGINX configuration file
nginx -g 'daemon off;'   # this makes sure that this service is running in the foreground(to see logs). By default it runs in background and then we would need some sevice manager to see the logs.
                         # this will also make docker container continue to run util I kill the nginx server, which is necessary for some reason.