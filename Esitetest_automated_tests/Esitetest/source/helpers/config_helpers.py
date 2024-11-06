
import os
from dotenv import load_dotenv

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://localhost:8888/Esite'
    elif env.lower() == 'prod':
        return 'http://localhost:8888/prod/Esite'
    else:
        raise Exception(f'Unknown environment: {env}')

def get_database_credentials():

    load_dotenv()

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    print(f"DB_USER: {db_user}, DB_PASSWORD: {db_password}")

    if not db_user or not db_password:
        raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD' must be set.")

    env = os.environ.get('ENV', 'test')
    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    else:
        raise  Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}

    return db_info


