from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError
)

with sync_playwright() as p:

    # Step 1: Launch browser
    browser = p.chromium.launch(headless=False)

    try:
        # Step 2: Create new page
        page = browser.new_page()

        # Step 3: Navigate to Cricbuzz
        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded"
        )

        # Step 4: Use your inspected selector
        score_selector = "div.flex.items-center.gap-4.justify-between"

        try:
            # Step 5: Wait for score element
            page.wait_for_selector(
                score_selector,
                timeout=15000
            )

            # Step 6: Extract score
            score = page.locator(
                score_selector
            ).first.inner_text()

            # Step 7: Print score
            print("Live Cricket Score:")
            print(score)

            # Step 8: Save screenshot
            page.screenshot(
                path="score.png",
                full_page=True
            )

            print("Screenshot saved: score.png")

        except PlaywrightTimeoutError:
            print("No live score element found within 15 seconds.")

    finally:
        # Step 9: Close browser
        browser.close()