"""This class contains database models
"""

from personalfinance.database import Base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE

class FutureValue(Base):
    """This class represents a future value database
    """
    __tablename__ = "futurevalues"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    interest = Column(Float, nullable=False)
    years = Column(Integer, nullable=False)
    futurevalue = Column(Float, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    