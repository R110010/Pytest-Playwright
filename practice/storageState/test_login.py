def test_login_and_save_auth(page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    assert page.title() == "ProtoCommerce"
