from pony.orm import Database, Required, Optional, Set, PrimaryKey

db = Database("sqlite", "../makersita.db", create_db=True)


class User(db.Entity):
    chatId = PrimaryKey(int, sql_type='BIGINT', size=64)
    firstName = Optional(str)
    lastName = Optional(str)
    username = Optional(str)
    lastStatus = Optional(str)
    messages = Set("Message")


class Message(db.Entity):
    user = Required(User)
    text = Optional(str)
    date = Required(int, sql_type='BIGINT', size=64)
    chatId = Required(int, sql_type='BIGINT', size=64)
    msgId = Required(int, sql_type='BIGINT', size=64)
    edited = Required(bool, default=False)


db.generate_mapping(create_tables=True)
