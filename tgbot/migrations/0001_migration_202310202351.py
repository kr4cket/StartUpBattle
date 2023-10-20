# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Theme(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255, unique=True)
    class Meta:
        table_name = "theme"


@snapshot.append
class Language(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255, unique=True)
    class Meta:
        table_name = "language"


@snapshot.append
class LanguageLevel(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255)
    lang = snapshot.ForeignKeyField(backref='langs', index=True, model='language')
    class Meta:
        table_name = "languagelevel"


@snapshot.append
class Chat(peewee.Model):
    id = BigIntegerField(primary_key=True)
    theme = snapshot.ForeignKeyField(backref='chat', index=True, model='theme', null=True)
    lang = snapshot.ForeignKeyField(backref='chat', index=True, model='language', null=True)
    lvl = snapshot.ForeignKeyField(backref='chat', index=True, model='languagelevel', null=True)
    class Meta:
        table_name = "chat"


