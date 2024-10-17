import pymysql
from pymysql import connect
from Esitetest.source.helpers.config_helpers import get_database_credentials
from Esitetest.source.configs.generic_configs import GenericConfigs


def read_from_db(sql):

    db_creds = get_database_credentials()
    connection = pymysql.connect(host=db_creds['db_host'], port= db_creds['db_port'],
                                 user = db_creds['db_user'], password= db_creds['db_password'])

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data


def get_order_from_db_by_order_no(order_no):

    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX

    sql = f"SELECT * FROM {schema}.{table_prefix}posts WHERE id = {order_no} AND post_type = 'shop_order_placehold';"

    db_order = read_from_db(sql)

    return db_order

def get_user_from_db_by_email(user_email):
    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX

    sql = f"SELECT * FROM {schema}.{table_prefix}users WHERE user_email = '{user_email}';"

    db_user_email = read_from_db(sql)

    return db_user_email



