import json

from behave import given, then, when

import Website







app = Website.create_app('testing')
app = app.test_client()

#Feature Login
@given('I want to login')
def step_impl(context):
    app = Website.create_app('testing')
    app = app.test_client()


@when('I try to login using {email} as email and {password} as password')
def step_impl(context, email, password):
    global result
    result = app.post('/login', data={'email': email, 'password': password})


@then('the login should be {LoginResult}')
def step_impl(context, LoginResult):
    if (result.status_code == 302 and result.location == '/u'):
        assert (LoginResult == True)
    else:
        assert (not LoginResult == LoginResult)

#Feature Sign Up
@given(u'I want to sign up')
def step_impl(context):
    app = Website.create_app('testing')
    app = app.test_client()


@when('I try to sign up using {email} as email and {Name} as name and {Password} as first password and {Password2} as second password')
def step_impl(context, email, Name, Password, Password2):
    global result
    result = app.post('/sign-up', data={'email': email, 'firstName': Name, 'password1': Password,'password2': Password2})


@then('the sign up result is {Result} with message: {Message}')
def step_impl(context, Result, Message):
    if result.status_code != 302 or result.location != '/u':
        assert (not Result == Result)
    else:
        if Message not in result.data:
            return
        assert (Result == True)


#Feature Note Deletion
noteId = None
@given('I want to delete a note')
def step_impl(context):
    app = Website.create_app('testing')
    app = app.test_client()
    app.get('/u')


@when('I try to delete the note with id {id}')
def step_impl(context, id):
    global result
    result = app.post('/delete-note', data=json.dumps({'noteId': id}))
    global noteId
    noteId = id


@then('the note deletion result is {Result}')
def step_impl(context, Result):
    notes = app.get('/u')
    Result = (noteId not in notes.data)
    assert (Result==True)


#Feature Note Creation
@given('I want to create a note')
def step_impl(context):
    app = Website.create_app('testing')
    app = app.test_client()


@when('I try to create the note with content {content}')
def step_impl(context, content):
    app.post('/u', data={'note': content})


@then('the note creation result is {Result} with message: {Message}')
def step_impl(context, Result, Message):
    notes = app.get('/u')
    assert (Message in notes.data, Result)


