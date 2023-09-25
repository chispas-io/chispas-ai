import os
from multiprocessing import Process, Event

import click
from chispas.utils.database import initialize_database, erase_unknown_words_table
from chispas.utils.sessions import generate_secret_key

@click.group()
def cli():
    """Chispas CLI"""

@cli.command('init-db')
def init_db():
    """Clear the existing data and create new tables."""

    initialize_database()
    erase_unknown_words_table()
    click.echo('Initialized the database.')

@cli.command('secret-key')
def secret_key():
    """
    Create a secret key for sessions and password encryption. SECRET_KEY is
    mandatory for production.
    """

    new_key = generate_secret_key()
    click.echo(new_key)

@cli.command()
def serve():
    """Run the Flask app."""

    os.system('flask --app chispas run --debug')

@cli.command('serve-frontend')
def serve_frontend():
    """Run the Vue app."""

    os.system('pnpm run dev')

@cli.command('serve-dev')
def serve_dev():
    """Run both the Flask and Vue apps at the same time."""

    e = Event()

    p1 = Process(target=task_1, args=(e,))
    p1.start()

    p2 = Process(target=task_2, args=(e,))
    p2.start()

    e.set()

def task_1(event):
    event.wait()
    os.system('pipenv run cli serve')

def task_2(event):
    event.wait()
    os.system('pipenv run cli serve-frontend')
