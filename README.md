# Extraction Microservice

Satellite Data Extraction and Distribution, and coordinates calculation

# Getting started

To start, you will need [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)

# Running

Clone the Github repo
```bash
$ git clone https://github.com/Novatics/nasaDataAPI
```

Access the main project folder
```bash
$ cd nasaData
```
Create .env file
```bash
$ touch .env
```

Copy and paste the lines below in .env
```
POSTGRES_USER=extractapi
POSTGRES_PASSWORD=extractapi123
POSTGRES_DB=extractapi
POSTGRES_HOST=db-extract
PORT=8000
```

Run the app

```bash
$ (sudo) docker-compose run web-extract python manage.py makemigrations core
$ (sudo) docker-compose run web-extract python manage.py migrate core
$ (sudo) docker-compose up
```

And you are good to go! o/
