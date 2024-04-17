# We are not using it directly, but when we run our proxy we will set some values in it and then use it (dynamically)

server {    # nginx will look for this block
    listen ${LISTEN_PORT};    # the server will listen to this port number, this is an env. variable that will be passed here.

    location /static {               # any url with /static will go to /vol/static location, for  media files
        alias /vol/static;
    }

    location / {               # any url with /, it will go to server(wsgi server).
        uwsgi_pass            ${APP_HOST}:${APP_PORT};
        include               /etc/nginx/uwsgi_params;    # include, will include uwsgi params (this params are required to read http requests by the service. This is an standard file)
        client_max_body_size  10M;                       # maximum body size of the request body, meaning maximux image size that can be uploaded is 10MB.
    }
}
