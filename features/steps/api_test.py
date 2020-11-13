""" from behave import given, when, then
import requests

@given('we post a GET request')
def step_impl(context):
    context.request_type = 'GET'
@when('we set the content-type as "application/json"')
def step_impl(context):
    context.type = 'application/json'
@then('we recieve valid HTTP code 200')
def step_impl(context):
    context.response =  requests.get(url = 'http://localhost:5000')

 """