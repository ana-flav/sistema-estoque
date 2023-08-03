import random
import string

def make_random_password(password_length):
    """Generate a random password string of letters and digits and special characters"""

    full_string = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(password_length):
        password += random.choice(full_string)
    return password

# def send_email_with_password(email, password):
#     """Send an email with the password to the user""" 