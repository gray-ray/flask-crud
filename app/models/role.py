
from . import db

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, Integer, Column, Table, ForeignKey


# from .user import User

from .associations import user_roles


class Role(db.Model): 
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True,)

    role_name: Mapped[str] = mapped_column(String(80), nullable=False, unique= True)



    # 与 User 的多对多关系
    users: Mapped[list["User"]] = relationship(
        "User",
        secondary=user_roles,  # 中间表
        back_populates="roles"  # 反向关系
    )

    def __init__(self, role_name):
        self.role_name = role_name

    # 输出转换
    def to_dict(self):
        return {
            'id': self.id,
            'roleName': self.role_name,
        }

    def __repr__(self):
        return f"<Role {self.role_name}>"