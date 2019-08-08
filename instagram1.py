 #script to download photos from instagram

import click
import os
from splinter import Browser
from bs4 import BeautifulSoup as bs4


@click.command()
@click.argument("username", type=click.STRING)
@click.option('--username', '-u', default=0, help="Enter username of instagram account that is public")
def insta(username):
    link = "https://www.instagram.com/" + username
    print("Downloading images {}...".format(username))

    if os.name == "posix":
        geckodriver_path = "./geckodriver/geckodriver"
    else:
        geckodriver_path = "./geckodriver/geckodriver.exe"

    with Browser("firefox", headless=True, executable_path=geckodriver_path) as browser:
        browser.visit(link)
        html = browser.html
        soup = bs4(html, "html.parser")

    data = soup.findAll("img")

    for x in data:
        x = x.get("src")
        os.system("wget --no-check-certificate -c -N -P ./Images/" + username + " " + x)
        print("Downloaded {}".format(x))

    print("\n\nFiles downloaded into photos/{}".format(username))
