from behave import given, when, then


@given('a user visits the login page')
def step_given_user_visits_login_page(context) -> None:
    context.browser.get('https://example.com/login')


@when('they submit valid credentials')
def step_when_submit_valid_credentials(context) -> None:
    context.browser.find_element_by_name('username').send_keys('user')
    context.browser.find_element_by_name('password').send_keys('pass')
    context.browser.find_element_by_name('login').click()


@then('they should see their dashboard')
def step_then_see_dashboard(context) -> None:
    assert 'Dashboard' in context.browser.title