from statistics import mean
from faker import Faker
import csv
import requests
from flask import Blueprint, request

hw1 = Blueprint('hw1', __name__, url_prefix='/hw1')


@hw1.route('/requirements/')
def first_task():
    with open('requirements.txt', 'r') as file:
        req = file.read()
    return '<pre>{}</pre>'.format(req)


@hw1.route('/generate-users/')
def second_task():
    faker = Faker()
    lst = []
    quantity = request.args.get('count', default=10, type=int)
    for i in range(quantity):
        lst.append(f'{faker.name()} {faker.ascii_email()}')
    res = '\n'.join(lst)
    return '<pre>{}</pre>'.format(res)


@hw1.route('/mean/')
def third_task():
    with open('hw.csv', 'r') as file:
        reader = csv.DictReader(file)
        h = []
        w = []
        for row in reader:
            height_cm = float(row[' "Height(Inches)"']) * 2.54
            weight_kg = float(row[' "Weight(Pounds)"']) / 2.205
            h.append(height_cm)
            w.append(weight_kg)
        res = f'Mean height: {round(mean(h), 2)} cm, mean weight: {round(mean(w), 2)} kg'
    return res


@hw1.route('/space/')
def fourth_task():
    try:
        r = requests.get('http://api.open-notify.org/astros.json')
        r_json = r.json()
    except requests.exceptions.ConnectionError as e:
        return f'Error: {e}'
    if 'people' not in r_json:
        return "The json doesn't have the attribute 'people'"
    res = r_json['people']
    return res