FROM python:3.10

# setting working directory
WORKDIR /usr/src/empty_project/

ENV PYTHONDONTWRITEBYTECODE 1
# no pyc files at disk
ENV PYTHONUNBUFFERED 1
# no buffering stdout/stderr

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
