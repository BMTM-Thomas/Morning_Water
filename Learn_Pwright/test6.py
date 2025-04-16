from playwright.sync_api import sync_playwright

def highlight_element(page, locator):
    element_handle = locator.element_handle()
    if element_handle:
        page.evaluate("""
            element => {
                element.style.outline = '2px dashed red';
                element.style.backgroundColor = 'white';
                element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        """, element_handle)
    else:
        raise Exception("Element not found or not visible")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    h1 = page.locator("h1")
    highlight_element(page, h1)

    page.wait_for_timeout(3001110)
    browser.close()
