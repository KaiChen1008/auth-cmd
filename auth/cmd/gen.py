import click
import csv
import pyperclip
from auth.utils.params import TOKEN_PATH
from auth.utils.utils import generate_totp


@click.command()
@click.argument("name")
def gen(name: str):
    """
    Generate TOTP password
    """
    click.echo(f"Generating token for {name}.")

    with open(TOKEN_PATH, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                secret, digit = row[1], int(row[2])
                totp = generate_totp(secret, digit)
                pyperclip.copy(totp)
                click.echo(f"Token(copied to clipboard): {totp}")
                return

        click.echo(f"Token {name} not found.")
    return
