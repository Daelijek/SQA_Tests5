from behave import *
import requests
import time

BASE_URL = "https://api.github.com"
context.headers = {}

@given('I have valid GitHub credentials')
def step_auth(context):
    context.headers = {
        "Authorization": f"Bearer {context.config.userdata['github_token']}",
        "Accept": "application/vnd.github+json"
    }

@when('I create a repository named "{repo_name}"')
def step_create_repo(context, repo_name):
    payload = {
        "name": repo_name,
        "description": "Initial description",
        "private": False
    }
    context.response = requests.post(
        f"{BASE_URL}/user/repos",
        json=payload,
        headers=context.headers
    )
    context.repo_name = repo_name

@then('the repository "{repo_name}" should exist')
def step_verify_repo_exists(context, repo_name):
    response = requests.get(
        f"{BASE_URL}/repos/{context.config.userdata['github_username']}/{repo_name}",
        headers=context.headers
    )
    assert response.status_code == 200

@when('I update the repository description to "{new_description}"')
def step_update_repo(context, new_description):
    payload = {
        "description": new_description
    }
    context.response = requests.patch(
        f"{BASE_URL}/repos/{context.config.userdata['github_username']}/{context.repo_name}",
        json=payload,
        headers=context.headers
    )

@then('the repository description should be "{expected_description}"')
def step_verify_description(context, expected_description):
    response = requests.get(
        f"{BASE_URL}/repos/{context.config.userdata['github_username']}/{context.repo_name}",
        headers=context.headers
    )
    assert response.json()['description'] == expected_description

@when('I delete the repository')
def step_delete_repo(context):
    context.response = requests.delete(
        f"{BASE_URL}/repos/{context.config.userdata['github_username']}/{context.repo_name}",
        headers=context.headers
    )
    # GitHub API needs time to process deletion
    time.sleep(5)

@then('the repository "{repo_name}" should not exist')
def step_verify_repo_deleted(context, repo_name):
    response = requests.get(
        f"{BASE_URL}/repos/{context.config.userdata['github_username']}/{repo_name}",
        headers=context.headers
    )
    assert response.status_code == 404