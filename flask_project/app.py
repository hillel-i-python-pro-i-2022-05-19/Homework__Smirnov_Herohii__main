from flask import Flask
from faker import Faker
import requests
import csv


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
            return requirements
    except:
        return f'There is no such file, sorry :('

@app.route("/generate-users")
def random_email_users_generation(*email_users):
    """
    Random email_users generation
    """
    email_users = [f'{fake.first_name()} {fake.unique.ascii_email()}' for _ in range(100)]

    return '<br>'.join(email_users)

@app.route("/space")
def space_man():
    some_url = 'http://api.open-notify.org/astros.json'

    responce = requests.get(some_url).json()
    return f'At this moment, there are {responce["number"]} astronauts.'


@app.route("/mean")
def count():
    with open('people_data.csv') as file:
        reader = list(csv.reader(file))

        height = 0
        weight = 0
        row = len(reader) - 1

        for index in range(1, row):
            height += float(reader[index][1])
            weight += float(reader[index][2])

        average_height = (height / row) * 2.54
        average_weight = (weight / row) * 0.453592

    return f'Average height is {average_height} cm and average weight is {average_weight} kg'
    
    

if __name__ == "__main__":
    app.run()
