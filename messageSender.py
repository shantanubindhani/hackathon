
import smtplib
import datetime

from random import randint

def gen_otp(len = 6):
    otp = 0
    for i in range(len):
        otp *= 10
        otp += randint(0, 9)
    return otp


def main():
    port = 587

    my_email = "mail.sender.codewithshan@gmail.com"
    mypwd = "ndkxodtbirvkzyel"

    client = ["shantanubindhani1805@gmail.com", ]

    subject = "test run of email sender"

    date = datetime.datetime.now().strftime( "%d|%m|%Y %H:%M" )

    otp = str(gen_otp())

    message = f"""Your feedback verification OTP is {otp}.
    
    
    Dt : {date}
    """

    sender = smtplib.SMTP('smtp.gmail.com', port)
    sender.ehlo()
    sender.starttls()
    sender.login(my_email, mypwd)


    res = sender.sendmail(my_email, client[0], message)
    inp = input("Enter your recieved OTP : ")
    if(inp == otp):
        print("you are verified")
    sender.quit()


if __name__ == "__main__":
    print("hola")
    main()