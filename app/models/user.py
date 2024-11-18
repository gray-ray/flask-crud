
from . import db

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, Integer

from .associations import user_roles

class User(db.Model): 
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer,primary_key=True,)

    username: Mapped[str] = mapped_column(String(80), nullable=False, unique= True)

    email: Mapped[str] = mapped_column(String(120),nullable=False, unique= False)

    # 与 Role 的多对多关系
    roles: Mapped[list["Role"]] = relationship(
        "Role",
        secondary=user_roles,  # 中间表
        back_populates="users"  # 反向关系
    )


    def __init__(self, username, email):
        self.username = username
        self.email = email

    # 输出转换
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'roles': [role.to_dict() for role in self.roles] 
        }

    def __repr__(self):
        return f"<User {self.username}>"