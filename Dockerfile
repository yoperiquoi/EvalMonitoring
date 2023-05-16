FROM ubuntu
WORKDIR /app

ARG GIT_URL=https://github.com/MatthisHoules/Energy-Monitoring-Usecase.git
ARG JOULEHUNTER_GIT=https://github.com/powerapi-ng/joulehunter.git
ARG SERVICE_NAME=Energy-Monitoring-Usecase


RUN apt update && \
    apt install -y python3\
    python3-pip\
    git && \
    git clone $GIT_URL && \
    pip3 install -r ./$SERVICE_NAME/requirements.txt && \
    git clone $JOULEHUNTER_GIT && \
    cd joulehunter && \
    python3 setup.py install

WORKDIR /app/$SERVICE_NAME

RUN git pull

LABEL maintainer="yoann.periquoi@imt-atlantique.fr"
LABEL fr.imta.devops.docker.version="1.0.0"
LABEL fr.imta.devops.docker.description="energy monitoring usecase"

ENTRYPOINT [ "python3", "serve_example_no_recursive.py" ]
