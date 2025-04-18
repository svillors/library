import json
import os

from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)

template = env.get_template('template.html')


def on_reload():
    with open('./books/meta_data.json') as raw_books:
        books = json.load(raw_books)
    chunked_books = list(chunked(books, 20))
    os.makedirs('pages', exist_ok=True)
    for number, books in enumerate(chunked_books, start=1):
        template = env.get_template('template.html')
        rendered_page = template.render(
            chunked_books=chunked(books, 2),
            current_page=number,
            pages_amount=len(chunked_books)
        )
        with open(
            os.path.join('pages', f'index{number}.html'),
            'w',
            encoding="utf8"
        ) as file:
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
             default_filename='pages/index1.html',
             port=8000,
             liveport=35729)
