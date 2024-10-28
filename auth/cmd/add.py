import click
import csv
from auth.utils.params import TOKEN_PATH
from auth.utils.utils import has_token


@click.command()
@click.option(
    "--name",
    prompt="Enter a name for this token",
    help="Token name, e.g., 'GitHub token'.",
)
@click.option(
    "--digit",
    type=click.Choice(["4", "6", "8"]),
    prompt="Enter the numb  er of dig its for TOTP",
    help="Number of TOTP digits (usually 6 or 8).",
)
@click.option(
    "--secret",  # noqa
    prompt="Enter your secret",
    help="Secret key for TOTP generation.",
)
def add(name: str, secret: str, digit: str) -> None:
    """
    Add a new token to the database.
    """
    try:
        _add(name, secret, int(digit))
    except Exception as e:
        click.ClickException(f"Add token failed: {e}")

    click.echo(f"Token {name} added successfully.")
    return


def _add(name: str, secret: str, digit: int) -> None:
    # Make sure the name does not exist
    if has_token(name):
        raise ValueError(f"Token {name} already exists.")

    # Add token to .auth_cmd/secret.csv
    with open(TOKEN_PATH, mode="a") as f:
        writer = csv.writer(f)
        writer.writerow([name, secret, digit])
    return
