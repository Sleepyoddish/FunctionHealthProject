from playwright.sync_api import Page

class ScanPage():
    def __init__(self, page: Page):
        self.page = page

    #this method selects the first available scan type and continues to the next step
    def select_scan(self):
        self.page.locator(".encounter-card").first.click()
        self.page.get_by_role("button", name="Continue").click()
