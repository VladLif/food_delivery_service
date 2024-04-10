from database import Base

from sqlalchemy import String, Column, Integer


class Restaurant(Base):
    """
        Таблица с ресторанами
    """

    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    food_category = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
