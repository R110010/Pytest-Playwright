import pytest
from pathlib import Path

AUTH_FILE = Path("auth.json")
LOGIN_URL = "https://rahulshettyacademy.com/loginpagePractise/"

@pytest.fixture(scope="session")
def auth_context(browser):
    # If we already have a saved session, reuse it
    if AUTH_FILE.exists():
        context = browser.new_context(storage_state=str(AUTH_FILE))
        yield context
        context.close()
        return

    # Otherwise, do a fresh login
    context = browser.new_context()
    page = context.new_page()
    page.goto(LOGIN_URL)

    # Perform login
    page.fill("#username", "rahulshettyacademy")
    page.fill("#password", "learning")

    # Choose user type (student) and accept alert
    page.locator("input[value='user']").check()
    page.locator("#okayBtn").click()

    # Select role dropdown
    page.select_option("select.form-control", label="Consultant")

    # Agree to terms and login
    page.locator("#terms").check()
    page.click("#signInBtn")

    # Wait for dashboard to load
    page.wait_for_url("**/angularpractice/shop")

    # Save session to file
    context.storage_state(path=str(AUTH_FILE))
    print("\n✅ Saved new auth session to auth.json")

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(auth_context):
    # For each test, open a new page with existing auth
    page = auth_context.new_page()
    yield page
    page.close()
