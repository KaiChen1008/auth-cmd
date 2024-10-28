import click
import csv
from auth.utils.utils import config_exists
from auth.utils.params import TOKEN_PATH


@click.command()
def list():
    """
    List existing tokens
    """
    if not config_exists():
        click.ClickException("No token exist.")
        return

    click.echo("List existing tokens.")
    with open(TOKEN_PATH, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            click.echo(row[0])
