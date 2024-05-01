"""This module contains the factory pattern implementation for the 
investment calculators
"""

import threading
from personalfinance.investment.calculators import (
    SipInvestmentCalculator,
    LumpsumInvestmentCalculator,
)




# create a singleton class for the factory pattern
class InvestmentFactory:
    """This class implements the factory pattern for the investment
    calculators
    """

    # implement singleton using __new__
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        """This is singleton implementation for the factory pattern
        for the investment calculators which is thread safe
        """
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = object.__new__(cls)
        return cls.__instance

    # create a method to get the investment calculator
    def get_calculator(
        self, calctype, investment_amount, investment_duration, interest_rate
    ):
        """This method gets the investment calculator

        Args:
          type: type of investment calcultor

        Raises: ValueError for unsupported types
        """
        if calctype == "sip":
            return SipInvestmentCalculator(
                interest_rate=interest_rate,
                investment_amount=investment_amount,
                investment_duration=investment_duration,
            )
        elif calctype == "lumpsum":
            return LumpsumInvestmentCalculator(
                interest_rate=interest_rate,
                investment_amount=investment_amount,
                investment_duration=investment_duration,
            )
        else:
            raise ValueError("Unsupported type of investment calculator")
