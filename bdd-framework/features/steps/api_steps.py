from behave import *
import requests

@given('I set API endpoint to "{endpoint}"')
def step_set_api_endpoint(context, endpoint):
    context.base_url = f"https://jsonplaceholder.typicode.com/{endpoint}"

@when('I send a GET request')
def step_send_get_request(context):
    context.response = requests.get(context.base_url)

@then('the response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain at least {count:d} items')
def step_verify_item_count(context, count):
    items = context.response.json()
    assert len(items) >= count, \
        f"Expected at least {count} items, got {len(items)}"