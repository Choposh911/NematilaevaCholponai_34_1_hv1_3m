CREATE_USER_TABLE_QUERY = """
         CREATE TABLE IF NOT EXISTS bot_users
         (
         ID INTEGER PRIMARY KEY,
         TELEGRAM_ID INTEGER,
         USERNAME VARCHAR(50),
         FIRST_NAME VARCHAR(50),
         LAST_NAME VARCHAR(50),
         UNIQUE (TELEGRAM_ID)
         )
         
"""


INSERT_USER_QUERY = """
INSERT INTO bot_users VALUES (?,?,?,?,?)
"""