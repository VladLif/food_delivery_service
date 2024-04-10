from database import Base

from sqlalchemy import Column, Integer, ForeignKey, DateTime


class Order(Base):
    """
        Таблица с заказами
    """

    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    order_time = Column(DateTime, nullable=False)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    food = Column(Integer, ForeignKey("food.id"), nullable=False)
