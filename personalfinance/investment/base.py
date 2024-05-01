"""This module contains the base abstract classes for investment implementation
"""

from abc import ABC, abstractmethod


class BaseInvestmentCalculator(ABC):
    """This is the base class for investment calculation"""

    def __init__(self, investment_amount, investment_duration, interest_rate, name):
        self.investment_amount = investment_amount
        self.investment_duration = investment_duration
        self.interest_rate = interest_rate
        self.name = name

    @abstractmethod
    def future_value(self):
        """This method calculates the investment return"""
