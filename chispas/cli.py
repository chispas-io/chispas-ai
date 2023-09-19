import os
import click
from chispas.utils.database import initialize_database, erase_unknown_words_table

@click.group()
def cli():
    """Chispas CLI"""

@cli.command('init-db')
def init_db():
    """Clear the existing data and create new tables."""
    initialize_database()
    erase_unknown_words_table()
    click.echo('Initialized the database.')

@cli.command()
def serve():
    """Run the app."""
    os.system('FLASK_APP=chispas flask run')
