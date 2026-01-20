from playwright.sync_api import Page


class LoginPage():
    def __init__(self, page: Page):
        self.page = page

    #this method navigates to the login page
    def navigate_to_login(self, url: str):
        self.page.goto(url)

    #this method fills in the login fields and logins
    def login(self, email: str, password: str):
        self.page.locator("#email").fill(email)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Submit").click()

    #this method clicks the Book Scan button to go to the booking page
    def go_to_booking(self):
        self.page.get_by_role("button", name= "Book a Scan").click()
