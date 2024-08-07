from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class GiveOut(Base):
    __tablename__ = "give_outs"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    published_date = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    due_date = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=None
    )
    mode = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="give_outs")
    interactions = relationship("Interaction", back_populates="give_out", cascade="all, delete-orphan")


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
    region = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False, server_default="FALSE")
    date_verified = Column(
            TIMESTAMP(timezone=True), nullable=True, server_default=None
        )

    give_outs = relationship("GiveOut", back_populates="owner")
    interactions = relationship("Interaction", back_populates="user")


class Object(Base):
    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, nullable=False)
    object_name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category", back_populates="objects")
    pictures = relationship("Picture", back_populates="object", cascade="all, delete-orphan")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    country_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False
    )
    city_name = Column(String, nullable=False, unique=True)

    country = relationship("Country", back_populates="cities")


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, nullable=False)
    country_name = Column(String, nullable=False, unique=True)

    cities = relationship("City", back_populates="country")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False)
    category_name = Column(String, nullable=False, unique=True)

    objects = relationship("Object", back_populates="category")
    subcategories = relationship("Subcategory", back_populates="category")


class Subcategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, nullable=False)
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    subcategory_name = Column(String, nullable=False, unique=True)

    category = relationship("Category", back_populates="subcategories")
    types = relationship("Type", back_populates="subcategory")


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, nullable=False)
    subcategory_id = Column(
        Integer, ForeignKey("subcategories.id", ondelete="CASCADE"), nullable=False
    )
    type_name = Column(String, nullable=False, unique=True)

    subcategory = relationship("Subcategory", back_populates="types")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    give_out_id = Column(Integer, ForeignKey('give_outs.id'), nullable=False)
    interaction_time = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )

    user = relationship("User", back_populates="interactions")
    give_out = relationship("GiveOut", back_populates="interactions")


class Picture(Base):
    __tablename__ = "pictures"

    id = Column(Integer, primary_key=True, nullable=False)
    object_id = Column(
        Integer, ForeignKey("objects.id", ondelete="CASCADE"), nullable=False
    )
    image_url = Column(Text, nullable=False)

    object = relationship("Object", back_populates="pictures")
