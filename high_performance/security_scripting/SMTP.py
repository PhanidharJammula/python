import smtplib

s = smtplib.SMTP("192.168.0.160", 25)

try:
    m = "\nThis is message"
    s.sendmail("phanidhar22@gmail.com", "phanidhar22@gmail.com", m)
    print("Finished sending")
except Exception as e:
    print("Unable to send message: ", e)

s.quit()