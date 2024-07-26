# import smtplib

# my_email = "butterflyirises@gmail.com"
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addr="maydeng111@yahoo.com", 
#         msg="Hello")
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2024:
    print("wear a face mask")
print(year)