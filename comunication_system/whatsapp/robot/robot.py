from .browser import Browser

from urllib import parse

class Robot:
    def __init__(self):
        self.browser = Browser()
        self.browser.go_to("https://web.whatsapp.com/")

    def send_message(self, params):
        query_params = parse.urlencode(params)
        self.browser.go_to(
            f"https://web.whatsapp.com/send?{query_params}")
        self.browser.click_selector("button[aria-label='Enviar']")
