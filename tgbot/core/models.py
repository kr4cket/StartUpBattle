from peewee import *
from tgbot.core.db_conn import DBConnection


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        database = DBConnection().get_handle()


class Language(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=255, unique=True)


class Theme(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=255, unique=True)


class LanguageLevel(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=255)
    lang = ForeignKeyField(Language, backref="langs")


class Chat(BaseModel):
    id = BigIntegerField(primary_key=True, null=False)
    theme = ForeignKeyField(Theme, backref="chat", null=True)
    lang = ForeignKeyField(Language, backref="chat", null=True)
    lvl = ForeignKeyField(LanguageLevel, backref="chat", null=True)
