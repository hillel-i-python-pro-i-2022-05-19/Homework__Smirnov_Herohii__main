from flask import Flask
from faker import Faker
from random import choice as random_choice
import requests


app = Flask(__name__)
fake = Faker(['en_US', 'uk_UA'])


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello_there():
    return "Hello, there!"

@app.route("/requirements")
def read_requirements_txt():
    """
    Reading requirements
    """
    try:
        with open ('requirements.txt', 'r') as file:
            requirements = file.read()
            file.close()
            return requirements
    except:
        return f'There is no such file, sorry :('

@app.route("/generate-users")
def random_email_users_generation(*email_users):
    """
    Random email_users generation
    """

    users_name = fake.name().split()[0]

    emails = ('@gmail.com', '@yahoo.com', '@ukr.net', '@hotmail.com')
    random_email_address = random_choice(emails)

    return f'{users_name}{random_email_address}'

@app.route("/space")
def space_man():
    some_url = 'http://api.open-notify.org/astros.json'

    responce = requests.get(some_url).json()
    return f'At this moment, there are {responce["number"]} astronauts.'


@app.route("/mean")
def count():
    ...
    

if __name__ == "__main__":
    app.run()
