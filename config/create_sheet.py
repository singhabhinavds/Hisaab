import config_DB as DB

DB.connection.close()

DB_NAME= 'FLAT00'

TABLES= {}
TABLES['budget_sheet'] = (

    "CREATE TABLE 'budget_sheet' ("
    "'expense_id' int(11) NOT NULL AUTO_INCREMENT,"
    "'item_bought' varchar(30) NOT NULL,"
    "'amount_spent' int(6) NOT NULL,"
    "'spender_name' varchar(30) NOT NULL,"
    "'shared_among' "
    "'date_spent' date NOT NULL,"
    "PRIMARY KEY ('expense_id')"
    ") ENGINE=InnoDB"
    
    )

TABLES['flatmates'] = (

    "CREATE TABLE 'flatmates' ("
    "'user_id' int(2) NOT NULL AUTO_INCREMENT,"
    "'name' varchar(30) NOT NULL,"
    "PRIMARY KEY ('user_id')"
    ") ENGINE=InnoDB"

    )
