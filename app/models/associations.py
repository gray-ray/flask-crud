from sqlalchemy import Table, Column, Integer, ForeignKey
from . import db


# 中间表定义：多对多关系
user_roles = Table(
    "user_roles",
    db.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)