# python-flask-basic
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white" />

Connexion is a modern Python web framework that makes spec-first and api-first development easy. You describe your API in an OpenAPI (or swagger) specification with as much detail as you want and Connexion will guarantee that it works as you specified.

Based on your specification, Connexion provides the following functionality:
- Automatic routing to your Python functions
- Authentication
- Request validation
- Parameter parsing and injection
- Response serialization
- Response validation
- A Swagger UI console with live documentation and ‘try it out’ feature


#### Install Poerty
```bash
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```


#### Using Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate

# Migrate
alembic init alembic
alembic revision -m "first migrations"
alembic upgrade head
```


#### Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies with basic library:
```bash
poetry config virtualenvs.in-project true
poetry init
poetry add uvicorn
poetry add pytest
poetry add "connexion[swagger-ui]"
poetry add "connexion[flask]"
poetry add "connexion[swagger-ui]"
```


#### Handling with different user for github when pushing the commit
```bash
(.venv) ➜  python-flask-basic git:(master) git push -u origin master
remote: Permission to euiyounghwang/python-flask-basic.git denied to euiyounghwang1.
fatal: unable to access 'https://github.com/euiyounghwang/python-flask-basic.git/': The requested URL returned error: 403
(.venv) ➜  python-flask-basic git:(master) git config --local credential.helper ""
```

#### Run Service
```bash
http://localhost:5000/api/ui/
```


#### Push Docker-io with my account
```bash
docker push euiyoung/fn-flask-basic-api:es

(.venv) ➜  python-elasticsearch git:(master) docker push euiyoung/fn-flask-basic-api:es
The push refers to repository [docker.io/euiyoung/fn-flask-basic-api]
5d647ec1a1fb: Pushed
fd06eaaba40d: Pushed
64affd5054b0: Pushed
0d9bf610013e: Pushed
ddb6a9981c5b: Pushed
91f013cc9ad4: Pushed
1d228a5c814d: Pushed
96241174affd: Pushed
174a3bb9cb52: Pushed
f69e96eb5a0c: Pushed
44ea9a923069: Pushed
4b9bc13fb5b2: Pushed
c9f974dacf48: Pushed
cdc9dae211b4: Pushed
7095af798ace: Pushed
fe6a4fdbedc0: Pushed
e4d0e810d54a: Pushed
4e006334a6fd: Pushed
es: digest: sha256:1154c1125dca43ae585f45af4bf0df9374eecf05ab35d3fb9ac5131e97b0ce22 size: 4101
```