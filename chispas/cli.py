import os
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
    """Run the app."""

    os.system('flask --app chispas run --debug')
