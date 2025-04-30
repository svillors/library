import json
import os

from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def set_env():
    return Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )


def on_reload():
    env = set_env()
    meta_data_path = os.getenv(
        'META_DATA_PATH',
        default='./books_data/meta_data.json'
    )
    with open(meta_data_path) as raw_books:
        books = json.load(raw_books)
    page_items_count = 20
    items_per_row_count = 2
    chunked_books = list(chunked(books, page_items_count))
    os.makedirs('pages', exist_ok=True)
    for number, books in enumerate(chunked_books, start=1):
        template = env.get_template('template.html')
        rendered_page = template.render(
            chunked_books=chunked(books, items_per_row_count),
            current_page=number,
            pages_amount=len(chunked_books)
        )
        with open(
            os.path.join('pages', f'index{number}.html'),
            'w',
            encoding='utf8'
        ) as file:
            file.write(rendered_page)


def main():
    on_reload()
    server = Server()
    template_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'template.html'
    )
    server.watch(template_path, on_reload)
    root_dir = os.path.abspath(os.path.dirname(__file__))
    server.serve(
        root=root_dir,
        default_filename='index.html',
        port=8000,
        liveport=35729
        )


if __name__ == '__main__':
    main()
