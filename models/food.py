from database import Base

from sqlalchemy import String, Column, Integer, ForeignKey


class Food(Base):
    """
        Таблица с блюдами
    """

    __tablename__ = "food"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    structure = Column(String, nullable=False)
    restaurant = Column(Integer, ForeignKey("restaurant.id"), nullable=False)
