# from typing import Optional
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy import MetaData, Table, String, Integer, Column, DateTime
# from datetime import datetime
#
#
# def create_table():
#     metadata = MetaData()
#     Table('users_account', metadata,
#           Column('id', Integer(), primary_key=True),
#           Column('user_id', Integer(), nullable=False),
#           Column('created_on', DateTime(), default=datetime.now),
#           Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
#           )
#
#
# def create_user():
#     engine = create_engine("sqlite://", echo=True)
#     with Session(engine) as session:
#         session.add(User(
#             name="spongebob",
#             fullname="Spongebob Squarepants",
#         ))
#         session.commit()
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class User(Base):
#     __tablename__ = "users_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
