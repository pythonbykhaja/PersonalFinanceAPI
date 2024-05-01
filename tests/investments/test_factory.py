"""This module tests the factory implemenation of investment calculator
"""

import pytest
from personalfinance.investment.factory import InvestmentFactory


def test_factory_returns_correct_calculator():
    """This test checks if the factory returns the correct calculator"""
    factory = InvestmentFactory()
    calculator = factory.get_calculator(
        calctype="sip", interest_rate=18, investment_amount=10000, investment_duration=15
    )
    assert calculator.name == "sip"

    calculator = factory.get_calculator(
        calctype="lumpsum",
        interest_rate=18,
        investment_amount=10000,
        investment_duration=15,
    )
    assert calculator.name == "lumpsum"
    with pytest.raises(ValueError):
        factory.get_calculator(
            calctype="unknown",
            interest_rate=18,
            investment_amount=10000,
            investment_duration=15,
        )
