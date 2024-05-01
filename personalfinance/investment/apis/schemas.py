"""This class has schemas for api responses
"""

from datetime import datetime
from typing import List
from pydantic import BaseModel


class InvestmentSchema(BaseModel):
    """This method represents the schema for Investment model."""

    name: str
    amount: int
    years: int
    interest: float


class FutureValueInvestmentSchema(BaseModel):
    """This method represents the schema for FutureValueInvestment model."""

    id: str | None = None
    name: str
    amount: int
    years: int
    interest: float
    futurevalue: float
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        """This method represents the configuration for the schema."""

        orm_mode = True
        allow_population_by_field_name = True


class ListFutureValueInvestmentSchema(BaseModel):
    """This method represents the schema for ListFutureValueInvestment model."""

    results: List[FutureValueInvestmentSchema]

