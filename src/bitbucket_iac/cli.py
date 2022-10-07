"""
This file demonstrates how to authenticate and use the bitbucket Cloud APIs.

Here are my notion notes which explain somewhat how we arrived at this file:
https://quickest-trail-808.notion.site/Bitbucket-d499c8355937443db89c63e41b4fb1ff

To execute this file:

# arrive in the __main__ if statement
$ python -m bitbucket_iac.cli

# run the CLI
$ bitbucket
"""

from functools import lru_cache
from typing import Generator, Literal, TypedDict
from typer import Typer
from dotenv import load_dotenv
from os import environ
from atlassian.bitbucket import Cloud, Bitbucket
from atlassian.bitbucket.cloud.workspaces import Workspace
from atlassian.bitbucket.cloud.workspaces.projects import Projects, Project
from rich import print
import requests
from requests import Response

load_dotenv()

BITBUCKET_CLIENT_ID = environ["BITBUCKET_CLIENT_ID"]
BITBUCKET_CLIENT_SECRET = environ["BITBUCKET_CLIENT_SECRET"]
BITBUCKET_WORKSPACE_ID = "eriddoch1"

class Token(TypedDict):
    """Response from Bitbucket Cloud's /access-token OAuth endpoint."""
    access_token: str
    scopes: str
    token_type: Literal["bearer"]
    expires_in: int
    state: str
    refresh_token: str

def run():
    cli = Typer()
    cli.command()(create_repo)
    cli()


def create_repo():
    project: Project = get_project("LEAR")

    

def get_project(project_key: str) -> Project:
    bitbucket: Cloud = get_cloud_client()
    workspace: Workspace = bitbucket.workspaces.get(workspace=BITBUCKET_WORKSPACE_ID)
    projects: Projects = workspace.projects
    project: Project = projects.get(project_key)
    return project

@lru_cache
def fetch_token(client_id: str, client_secret: str) -> Token:
    """
    Fetch a token using the client_credentials OAuth grant.
    
    See here: https://developer.atlassian.com/cloud/bitbucket/oauth-2/#3--client-credentials-grant--4-4-
    """
    data = {
        "grant_type": "client_credentials",
    }
    response: Response = requests.post('https://bitbucket.org/site/oauth2/access_token', data=data, auth=(client_id, client_secret))
    return response.json()


def get_bitbucket_client() -> Bitbucket:
    client_credentials: dict = get_credentials()
    return Bitbucket("https://api.bitbucket.org/", oauth2=client_credentials)

def get_cloud_client() -> Cloud:
    client_credentials: dict = get_credentials()
    return Cloud(oauth2=client_credentials)

def get_credentials() -> dict:
    token: Token = fetch_token(client_id=BITBUCKET_CLIENT_ID, client_secret=BITBUCKET_CLIENT_SECRET)
    client_credentials = {
        "client_id": BITBUCKET_CLIENT_ID,
        "token": token,
    }
    return client_credentials

if __name__ == "__main__":
    create_repo()
