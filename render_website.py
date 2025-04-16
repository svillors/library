import json
import os

from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)

template = env.get_template('template.html')


def on_reload():
    with open('./books/meta_data.json') as raw_books:
        books = json.load(raw_books)
    template = env.get_template('template.html')
    rendered_page = template.render(books=books)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("file updated")


on_reload()

server = Server()
template_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'template.html'
)
server.watch(template_path, on_reload)
root_dir = os.path.abspath(os.path.dirname(__file__))
server.serve(root=root_dir,
             default_filename='index.html',
             port=8000,
             liveport=35729)
