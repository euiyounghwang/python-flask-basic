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
```