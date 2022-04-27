from time import sleep
from jinja2 import Environment, FileSystemLoader
import json

env = Environment(
    loader=FileSystemLoader('templates'),
    lstrip_blocks=True,
    trim_blocks=True
    )
while True:
    with open('resume.json') as file:
        resume = json.load(file)

    with open('resume.html', 'w') as file:
        file.write(env.get_template('resume.html').render(
            resume, trim_blocks = True, lstrip_blocks=True
            ))

    sleep(1)