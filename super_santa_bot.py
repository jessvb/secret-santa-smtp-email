########################################################
### This was made with help from freecodecamp.org <3 ###
########################################################

# smtplib is for creating an smtp client for emailing :)
import smtplib
# mimetext for emailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# for randomly selecting a secret recipient <3
import random

FILENAME_NAMES_EMAILS = "names_emails.csv"
FILENAME_EMAIL_OUTLINE = "email.txt"
FILENAME_HOST_EMAIL_AUTH = "host_email_auth.txt"
COUPLES = [['jon jessi0', 'elise jessicav'], [
    'ness jess.vanb mit', 'parv jess csail']]


def get_names_emails(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as csv_file:
        for line in csv_file:
            names.append(line.split(",")[0])
            emails.append(line.split(",")[1].split("\n")[0])
        return names, emails
# print(get_names_emails(FILENAME_NAMES_EMAILS))


def read_email_outline(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_txt = template_file.read()
    return template_file_txt
# print(read_email_outline(FILENAME_EMAIL_OUTLINE))


def get_host_email_password(filename):
    with open(filename, 'r', encoding='utf-8') as txt_file:
        txt = txt_file.read()
        email = txt.split('\n')[0]
        password = txt.split('\n')[1]
    return (email, password)
# print(get_host_email_password(FILENAME_HOST_EMAIL_AUTH))

# make sure couples aren't paired up
def is_couple(name1, name2):
    isCoup = False
    for couple in COUPLES:
        if(name1 == couple[0] and name2 == couple[1] or name1 == couple[1] and name2 == couple[0]):
            isCoup = True
    return isCoup

# the secret santa selection!
def make_the_magic(names):
    done = False

    while (done == False):
        secret_names = []
        temp_names = names.copy()
        while len(temp_names) > 1:
            ind = random.randrange(len(temp_names))
            receiver = temp_names[ind]
            giver = names[len(secret_names)]
            # make sure that the giver name != receiver name
            # and that there are no couples paired together TODO
            while receiver == giver:
                print('same same! ' + str(ind))
                print(giver)
                print(receiver)
                ind = random.randrange(len(temp_names))
                receiver = temp_names[ind]
            # add the receiver to the secret_names list
            # and remove the receiver from temp_names
            secret_names.append(temp_names.pop(ind))
        # if the last two names aren't the same, then we're done!
        # otherwise, restart
        if (temp_names[0] != names[-1]):
            secret_names.append(temp_names.pop())
            done = True

    return secret_names


def main():
    # couples check
    print('couples:')
    for couple in COUPLES:
        print(couple)
    y_n = input('these are your couples? (y/n) ')
    if (y_n == 'y' or y_n == 'yes' or y_n == 'Y' or y_n == 'Yes'):
        # get the credentials for the host email address
        (HOST_EMAIL, PASSWORD) = get_host_email_password(FILENAME_HOST_EMAIL_AUTH)
        # get the names and email addresses of those you want to send to
        (names, emails) = get_names_emails(FILENAME_NAMES_EMAILS)
        # get the outline/template of the email you want to send
        email_outline = read_email_outline(FILENAME_EMAIL_OUTLINE)

        # print(email_outline.replace("${REC_NAME}", 'the beautiful rec name'))

        print("trues:")
        print(is_couple('jon jessi0', 'elise jessicav'))
        print(is_couple('elise jessicav', 'jon jessi0'))
        print(is_couple('ness jess.vanb mit', 'parv jess csail'))
        print(is_couple('parv jess csail', 'ness jess.vanb mit'))

        print("falses:")
        print(is_couple('parv jess csail', 'jon jessi0'))
        print(is_couple('jess jess.vanb', 'ness jess.vanb mit'))
        print(is_couple('elise jessicav', 'ness jess.vanb mit'))
        print(is_couple('jon jessi0', 'ness jess.vanb mit'))
        print(is_couple('jon jessi0', 'parv jess csail'))

        # receiver_names = make_the_magic(names)
        # print(names)
        # print(receiver_names)

        # # set up the smtp client
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login(HOST_EMAIL, PASSWORD)

        # # personalize all the messages per-contact
        # for name, email in zip(names, emails):
        #     msg = MIMEMultipart()
        #     # substitute the ${GIVE_NAME} and ${REC_NAME} in the text
        #     text = email_outline.replace("${GIVE_NAME}", name.title())
        #     text = text.replace("${REC_NAME}", "TODO")

        #     # set up the rest of the email parameters
        #     msg['From']=HOST_EMAIL
        #     msg['To']=email
        #     msg['Subject']="Test email 3"
        #     msg.attach(MIMEText(text, 'plain'))

        #     # SEND IT!
        #     s.send_message(msg)

        #     del msg

        # # quit the smtp session and close the connection
        # s.quit()

        # print('MERRY CHRISTMAS! The Secret Santa Bot has done its Super Secret Send!')
    else:
        print("Oh no! Santa Bot messed up! Edit COUPLES in the super_santa_bot.py file to fix his memory.")


if __name__ == '__main__':
    main()
