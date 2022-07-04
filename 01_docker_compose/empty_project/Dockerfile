FROM python:3.10

# setting working directory
WORKDIR /usr/src/empty_project/

# no pyc files at disk
ENV PYTHONDONTWRITEBYTECODE 1

# no buffering of stdout/stderr
ENV PYTHONUNBUFFERED 1

# install the requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy and set mode for the entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY . .

# execute the entrypoint.sh, making sure db is configured before server starts
# ENTRYPOINT
ENTRYPOINT ./entrypoint.sh
