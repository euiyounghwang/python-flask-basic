# python-flask-basic
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
