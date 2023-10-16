"""This generates the static HTML file from the JSON resume file."""
import json

from time import sleep
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates"), lstrip_blocks=True, trim_blocks=True
)
while True:
    with open("resume.json", encoding="utf-8") as file:
        resume = json.load(file)

    with open("resume.html", "w", encoding="utf-8") as file:
        file.write(
            env.get_template("resume.html").render(
                resume, trim_blocks=True, lstrip_blocks=True
            )
        )

    sleep(1)
