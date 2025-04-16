from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1️⃣ Open Playwright Documentation
    page.goto("https://playwright.dev/python/")

    # 2️⃣ Wait until the page is loaded
    page.wait_for_selector("footer")

    # 3️⃣ Scroll to the "Contact" section in the footer
    contact_link = page.get_by_text("Contact", exact=True)
    contact_link.scroll_into_view_if_needed()

    # 4️⃣ Wait to see the effect
    page.wait_for_timeout(3000)

    browser.close()
