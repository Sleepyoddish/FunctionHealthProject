from pytest_playwright.pytest_playwright import page

from pages.booking_page import BookingPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.scan_page import ScanPage
from utils.login_data import email, password, url
from utils.payment_data import card_number, cvc, expiration_date, zip_code

# this test verifies that incomplete payment information shows appropriate error messages
def test_incomplete_payment_info(page):
    login = LoginPage(page)
    scan = ScanPage(page)
    payment = PaymentPage(page)
    booking = BookingPage(page)
    login.navigate_to_login(url)
    login.login(email, password)
    login.go_to_booking()
    scan.select_scan()
    booking.select_location_and_time()
    payment.verify_incomplete_payment_info()