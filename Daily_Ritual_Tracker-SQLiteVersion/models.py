from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db
from flask_login import UserMixin

""" #Old Syntax of SQLAlchemy
class Ritual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    begin_time = db.Column(db.String(100), nullable=False)
    finish_time = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(400), nullable=False)

 """

class Ritual(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="rituals")
    date: Mapped[str] = mapped_column(String(100), nullable=False)
    begin_time: Mapped[str] = mapped_column(String(100), nullable=False)
    finish_time: Mapped[str] = mapped_column(String(100), nullable=False)
    comment: Mapped[str] = mapped_column(String(400), nullable=False)

    def __repr__(self):
        return f'<Ritual id={self.id}>'

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    rituals: Mapped[list["Ritual"]] = relationship(back_populates=("user"))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)