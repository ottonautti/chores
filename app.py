import datetime

from peewee import (
    BooleanField,
    DateTimeField,
    Model as PeeweeModel,
    SqliteDatabase,
    Table,
    TextField,
    IntegerField,
    ForeignKeyField,
    Check,
)

db = SqliteDatabase("chores.db")


def initialize(passphrase):
    db.init("diary.db", passphrase=passphrase)
    db.create_tables([Chore, Task])


class BaseModel(PeeweeModel):
    class Meta:
        database = db


class Chore(BaseModel):
    name = TextField
    weight = IntegerField(constraints=[Check("0 > weight > 3")])


class Task(BaseModel):
    timestamp = DateTimeField(default=datetime.datetime.now)
    chore = ForeignKeyField(Chore, backref="completions")
    completed = BooleanField(default=False)
    frequency = IntegerField(default=1)
