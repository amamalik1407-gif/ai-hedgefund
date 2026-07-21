"""Portfolio management module."""

import logging
from typing import Dict, Optional
import pandas as pd

logger = logging.getLogger(__name__)


class Portfolio:
    """Manages trading portfolio."""

    def __init__(self, initial_capital: float):
        """Initialize portfolio.
        
        Args:
            initial_capital: Initial capital in USD
        """
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}
        self.trades = []
        logger.info(f'Initialized {self.__class__.__name__} with capital ${initial_capital:,.2f}')

    def add_position(self, symbol: str, quantity: float, 
                    entry_price: float) -> bool:
        """Add a position to portfolio.
        
        Args:
            symbol: Stock symbol
            quantity: Number of shares
            entry_price: Entry price
            
        Returns:
            True if successful
        """
        try:
            cost = quantity * entry_price
            if cost <= self.cash:
                self.positions[symbol] = {
                    'quantity': quantity,
                    'entry_price': entry_price,
                    'current_price': entry_price,
                }
                self.cash -= cost
                logger.info(f'Added position: {quantity} {symbol} @ ${entry_price}')
                return True
            else:
                logger.warning(f'Insufficient cash: {cost} > {self.cash}')
                return False
        except Exception as e:
            logger.error(f'Error adding position: {e}')
            return False

    def get_total_value(self) -> float:
        """Get total portfolio value.
        
        Returns:
            Total value
        """
        total = self.cash
        for symbol, position in self.positions.items():
            total += position['quantity'] * position['current_price']
        return total
