import random
import string
from venv import logger


def random_username():
    length = random.randint(5,10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return username

def generate_random_email_and_password(domain =None, email_prefix=None):

    if not domain:
        domain = 'esite.com'
    if not email_prefix:
        email_prefix ='testuser'

    random_email_string_length =10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    logger.info(f'Generated random email:{email}')

    random_pass_length = 20
    random_password =''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k =random_pass_length))

    random_info ={'email': email, 'password': random_password}
    return random_info





