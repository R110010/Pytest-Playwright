import pytest
from pathlib import Path

AUTH_FILE = Path("auth.json")
LOGIN_URL = "https://rahulshettyacademy.com/loginpagePractise/"

@pytest.fixture(scope="session")
def auth_context(browser):
    if AUTH_FILE.exists(): # if logges in previously
        context = browser.new_context(storage_state=str(AUTH_FILE))
        yield context
        context.close()
        return
    # if not logged in earlier, then fresh login is required
    context=browser.new_context()
    page=context.new_page()
    page.goto(LOGIN_URL)
    page.locator("//input[@id='username']").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
    page.locator("//input[@value='user']").check()
    page.locator("#okayBtn").click()
    page.locator("//div[@class='form-group']/select[@class='form-control']").select_option(label="Consultant")
    page.get_by_role("checkbox",name="terms").check()
    page.locator("#signInBtn").click()
    page.wait_for_url("https://rahulshettyacademy.com/angularpractice/shop")

    context.storage_state(path=str(AUTH_FILE))
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(auth_context):
    page=auth_context.new_page()
    yield page
    page.close()
