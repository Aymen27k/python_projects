from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db
from flask_login import UserMixin

class Ritual(db.Model):
    __tablename__ = "rituals"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="rituals")
    date: Mapped[str] = mapped_column(String(100), nullable=False)
    begin_time: Mapped[str] = mapped_column(String(100), nullable=False)
    finish_time: Mapped[str] = mapped_column(String(100), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self):
        return f'<Ritual id={self.id}>'

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    rituals: Mapped[list["Ritual"]] = relationship(back_populates=("user"))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)