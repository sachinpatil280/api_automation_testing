FROM ubuntu:latest

RUN apt update
RUN apt-get install -y
RUN apt install python3 -y
RUN apt-get -y install python3-pip

WORKDIR /usr/app/src
CMD ['mkdir', 'ApiTesting']

COPY ./ /usr/app/src/ApiTesting
WORKDIR /usr/app/src/ApiTesting/utilities

ENTRYPOINT [ "sh", "run_test.sh"]
