from peewee import Model, IntegerField, TextField, ForeignKeyField, DateField, SqliteDatabase

db = SqliteDatabase('spbgti.db')


class BaseModel(Model):
    class Meta:
        database = db


class Group(BaseModel):
    number = IntegerField(unique=True)


class Pair(BaseModel):
    group = ForeignKeyField(Group, related_name='pairs')
    name = TextField()
    date = DateField()
    duration = IntegerField()

db.create_tables([Group, Pair], True)
