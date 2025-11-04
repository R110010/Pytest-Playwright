def test_view_products(page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    products = page.locator(".card-title")
    count = products.count()
    assert count > 0
    print(f"\n🛒 Found {count} products")
