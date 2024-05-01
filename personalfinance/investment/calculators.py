"""This module contains the concrete implementations of investments
"""

from personalfinance.investment.base import BaseInvestmentCalculator


class SipInvestmentCalculator(BaseInvestmentCalculator):
    """This class calculates the sip investment"""

    def __init__(self, investment_amount, investment_duration, interest_rate):
        super().__init__(investment_amount, investment_duration, interest_rate, "sip")

    def future_value(self):
        """This method calculates the sip investment"""
        n = self.investment_duration * 12
        if self.interest_rate == 0:
            return self.investment_amount
        i = (self.interest_rate / 12) / 100

        future_value = self.investment_amount * (((1 + i) ** (n) - 1) / i) * (1 + i)
        return future_value


class LumpsumInvestmentCalculator(BaseInvestmentCalculator):
    """This class calculates the lumpsum investment"""

    def __init__(self, investment_amount, investment_duration, interest_rate):
        super().__init__(
            investment_amount, investment_duration, interest_rate, "lumpsum"
        )

    def future_value(self):
        """This method calculates the lumpsum investment"""
        return self.investment_amount * (1 + self.interest_rate / 100) ** (
            self.investment_duration
        )
