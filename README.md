# API Menu

API de teste

## Tecnologias

* Python 3.7
* Django 2.2
* Django Rest Framework 3.10
* Heroku(web versão demo)


## Versão DEMO

Versão demo disponível no Heroku [ACESSAR](https://menu-tests.herokuapp.com/docs/).

![Screenshot](https://i.imgur.com/JBhBNW9.png)

### Acesso documentação completa
Clicar no botão login do lado direito da tela

>**Usuário:** Menu    - **Senha:** Menu#123

## Instalação

```python
pip install -r requirements.txt
python manage.py runserver
```

## Teste de integração
```python
python manage.py tests
```

## Autenticação

Para autenticação foi usado **Basic Authorization**
>**Usuário:** Menu    - **Senha:** Menu#123


## Exemplos

Curl
```curl
curl -u Menu:Menu#123 https://menu-tests.herokuapp.com/clientes
```
Python(requests)
```python
import requests
from requests.auth import HTTPBasicAuth

requests.get('https://menu-tests.herokuapp.com/clientes', auth=HTTPBasicAuth('Menu', 'Menu#123'))
```