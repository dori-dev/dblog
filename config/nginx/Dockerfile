FROM nginx:1.15
LABEL MAINTAINER="Mohammad Dori | https://github.com/dori-dev"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
