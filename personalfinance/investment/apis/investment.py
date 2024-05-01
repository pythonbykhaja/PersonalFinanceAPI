from fastapi import Depends, HTTPException, status, APIRouter
from datetime import datetime
from personalfinance.investment.apis.schemas import (
    InvestmentSchema,
    FutureValueInvestmentSchema,
    ListFutureValueInvestmentSchema,
)
from personalfinance.investment.factory import InvestmentFactory
from personalfinance.database import get_database
from personalfinance.models import FutureValue
from sqlalchemy.orm import Session

router = APIRouter()
factory = InvestmentFactory()


# convert from FutureValueInvestmentSchema to FutureValue
def convert_to_future_value_schema(future_value: FutureValue):
    """This method converts FutureValue to FutureValueInvestmentSchema"""
    return FutureValueInvestmentSchema(
        name=future_value.name,
        interest=future_value.interest,
        amount=future_value.amount,
        years=future_value.years,
        futurevalue=future_value.futurevalue,
    )


@router.post(
    "/investment",
    response_model=FutureValueInvestmentSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_investment(
    investment: InvestmentSchema, db: Session = Depends(get_database)
):
    """This method creates a investment and returns FutureValue"""
    calculator = factory.get_calculator(
        calctype=investment.name,
        interest_rate=investment.interest,
        investment_amount=investment.amount,
        investment_duration=investment.years,
    )
    future_value = calculator.future_value()
    future_value_response = FutureValueInvestmentSchema(
        name=investment.name,
        interest=investment.interest,
        amount=investment.amount,
        years=investment.years,
        futurevalue=future_value,
    )
    new_future_value = FutureValue(**future_value_response.dict())
    db.add(new_future_value)
    db.commit()
    db.refresh(new_future_value)
    return future_value_response


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_investments(db: Session = Depends(get_database)):
    """This method returns all investments"""
    all_investments = db.query(FutureValue).all()
    future_values = [
        convert_to_future_value_schema(investment) for investment in all_investments
    ]
    return ListFutureValueInvestmentSchema(results=future_values)


@router.get("/amount", status_code=status.HTTP_200_OK)
def get_investment_by_amount(amount: float, db: Session = Depends(get_database)):
    """This method returns all investments"""
    all_investments = db.query(FutureValue).filter(FutureValue.amount == amount).all()
    return ListFutureValueInvestmentSchema(results=all_investments)
