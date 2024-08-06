from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.schema import PrimaryKeyConstraint


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    date_registered = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    region = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)
    verified = Column(Boolean, nullable=False, server_default="FALSE")
    date_verified = Column(
            TIMESTAMP(timezone=True), nullable=True, server_default=None
        )


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    city_name = Column(String, nullable=False, unique=True)


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, nullable=False)
    country_name = Column(String, nullable=False, unique=True)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False)
    category_name = Column(String, nullable=False, unique=True)


class Subcategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, nullable=False)
    subcategory_name = Column(String, nullable=False, unique=True)


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, nullable=False)
    type_name = Column(String, nullable=False, unique=True)


class GiveOut(Base):
    __tablename__ = "give_outs"

    id = Column(Integer, primary_key=True, nullable=False)
    published_date = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    due_date = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=None
    )
    

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    give_out_id = Column(Integer, ForeignKey('give_outs.id'), nullable=False)
    interaction_time = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )

