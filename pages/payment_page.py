import re

from playwright.sync_api import Page, expect


class PaymentPage():
    def __init__(self, page: Page):
        self.page = page


    #this method fills in the payment info inside the stripe iframe and submits the payment
    def enter_payment_info_and_confirm(self, card_number: str, expiration_date: str, cvc: str, zip_code: str):
        stripe_frame = self.page.frame_locator('iframe[title="Secure payment input frame"]').nth(0)
        self.page.wait_for_load_state()
        expect(stripe_frame.locator("#Field-numberInput")).to_be_visible()
        stripe_frame.locator("#Field-numberInput").fill(card_number)
        stripe_frame.locator("#Field-expiryInput").fill(expiration_date)
        stripe_frame.locator("#Field-cvcInput").fill(cvc)
        stripe_frame.locator("#Field-postalCodeInput").fill(zip_code)
        self.page.get_by_role("button", name= "Continue").click()

    #this method verifies that the appointment has been successfully booked by checking for the presence of the questionnaire button
    def verify_appointment_confirmed(self):
        expect(self.page.get_by_role("button", name= "Begin Medical Questionnaire")).to_be_visible()

    def verify_incomplete_payment_info(self):
        stripe_frame = self.page.frame_locator('iframe[title="Secure payment input frame"]').nth(0)
        self.page.wait_for_load_state()
        expect(stripe_frame.locator("#Field-numberInput")).to_be_visible()
        self.page.get_by_role("button", name="Continue").click()
        expect(stripe_frame.get_by_text("Your card number is incomplete.")).to_be_visible()
        expect(stripe_frame.get_by_text("Your card’s expiration date is incomplete.")).to_be_visible()
        expect(stripe_frame.get_by_text("Your card’s security code is incomplete.")).to_be_visible()
        expect(stripe_frame.get_by_text("Your ZIP is invalid.")).to_be_visible()