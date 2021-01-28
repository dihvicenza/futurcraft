"""
Various functions used by the web app: connection to a database, handling multilingual content and so on.
"""
from os import environ
from os.path import expanduser


def db_credentials(pgpass="~/.pgpass", pgpass_num=0, db="RDS_DB_NAME", user="RDS_USERNAME", password="RDS_PASSWORD",
                   host="RDS_HOSTNAME", port="RDS_PORT"):
    if 'RDS_HOSTNAME' in environ:
        DB = environ[db]
        USER = environ[user]
        PASSWORD = environ[password]
        HOST = environ[host]
        PORT = environ[port]
    else:
        with open(expanduser(pgpass), "r") as f:
            for i, line in enumerate(f):
                line = line.replace("\n", "")  # remove a newline character
                if i == pgpass_num:  # read a line with a specific number
                    HOST, PORT, DB, USER, PASSWORD = line.split(':')
    return HOST, PORT, DB, USER, PASSWORD
