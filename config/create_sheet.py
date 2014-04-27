import mysql.connector
from mysql.connector import errorcode

DB_NAME= 'FLAT00'

TABLES= {}

TABLES['flatmates'] = (

    "CREATE TABLE flatmates ("
    "user_id int(2) NOT NULL AUTO_INCREMENT,"
    "name varchar(30) NOT NULL,"
    "PRIMARY KEY (user_id)"
    ") ENGINE=InnoDB"

    )

TABLES['budget_sheet'] = (

    "CREATE TABLE budget_sheet ("
    "expense_id int(11) NOT NULL AUTO_INCREMENT,"
    "item_bought varchar(30) NOT NULL,"
    "amount_spent int(6) NOT NULL,"
    "spender_id int(2) NOT NULL,"
    "shared_among_ids varchar(255) NOT NULL,"
    "date_spent date NOT NULL,"
    "PRIMARY KEY (expense_id),"
    "  CONSTRAINT spender_id_fk FOREIGN KEY (spender_id) "
    "     REFERENCES flatmates (user_id) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
    
    )




connection = mysql.connector.connect(user='root')
cursor = connection.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print "Failed creating database: {}".format(err)
        exit(1)

try:
    connection.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        connection.database = DB_NAME
    else:
        print err
        exit(1)


for name, ddl in TABLES.iteritems():
    try:
        print "Creating table {}: ".format(name)
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print "already exists."
        else:
            print err.msg
    else:
        print "OK"

cursor.close()
connection.close()
