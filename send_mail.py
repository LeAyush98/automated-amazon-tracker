import smtplib
import datetime

EMAIL = "ayu.sharma798@gmail.com"
PASSWORD = "password_changed"

def send_mail(price: int, url: str):
    if datetime.datetime.now().hour == 14:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Low Price!\n\n{price} INR is the price of the item you wanted!\nPlease use this URL:\n{url}\n\nThanks and regards,\nPython Bot,\nAyush's Personal Assistant,\nInside the HDD,\nDelhi 110051,\nIndia"
        )
        connection.close()
