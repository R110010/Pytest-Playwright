from playwright.sync_api import expect

def test_products_in_dashboard(page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    products=page.locator('h4.card-title')
    count=products.count()
    assert count >0,"No products are available"

    print("product are available on the page")