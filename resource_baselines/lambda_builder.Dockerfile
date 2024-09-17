FROM public.ecr.aws/lambda/python:3.12

RUN pip install poetry

ARG SRC_PATH

RUN echo $SRC_PATH

ADD $SRC_PATH /asset/

WORKDIR /asset

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt --target /asset --upgrade
