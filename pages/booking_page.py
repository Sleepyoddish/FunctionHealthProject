from playwright.sync_api import Page, expect


class BookingPage():
    def __init__(self, page: Page):
        self.page = page

    #this method selects the first available location, date, and time for the appointment and continues to the next step
    def select_location_and_time(self):
        self.page.locator(".location-card").first.click()
        day_locator = self.page.locator('[data-testid="1-30-cal-day-content"]')
        day_locator.wait_for(state="visible")
        day_locator.click()
        appointment_locator = self.page.locator(".appointments__individual-appointment").first
        appointment_locator.wait_for(state="visible")
        appointment_locator.click()
        self.page.get_by_role("button", name= "Continue").click()


