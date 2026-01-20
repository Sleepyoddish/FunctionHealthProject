from pytest_playwright.pytest_playwright import page

from pages.booking_page import BookingPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.scan_page import ScanPage
from utils.login_data import email, password, url
from utils.payment_data import card_number, cvc, expiration_date, zip_code

#this test covers the full booking flow from login to appointment confirmation
def test_successful_booking_flow(page):
    login = LoginPage(page)
    scan = ScanPage(page)
    payment = PaymentPage(page)
    booking = BookingPage(page)
    login.navigate_to_login(url)
    login.login(email, password)
    login.go_to_booking()
    scan.select_scan()
    booking.select_location_and_time()
    payment.enter_payment_info_and_confirm(card_number, expiration_date, cvc, zip_code)
    payment.verify_appointment_confirmed()