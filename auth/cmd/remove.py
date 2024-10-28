import click
import csv
from auth.utils.params import TOKEN_PATH


@click.command()
@click.argument("name")
def remove(name: str):
    """
    Remove a token
    """
    click.echo("Remove a token.")

    res = []
    with open(TOKEN_PATH, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != name:
                res.append(row)

    with open(TOKEN_PATH, mode="w") as f:
        writer = csv.writer(f)
        writer.writerows(res)
