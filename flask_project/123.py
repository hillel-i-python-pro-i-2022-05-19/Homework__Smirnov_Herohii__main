# from faker import Faker
# fake = Faker()

# for _ in range(10):
#     print(fake.name())

from unicodedata import name
import requests


some_url = 'http://api.open-notify.org/astros.json'
responce = requests.get(some_url)
print(responce.content)