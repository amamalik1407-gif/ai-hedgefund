"""Backtesting metrics calculation."""

import logging
from typing import Dict, List
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class BacktestMetrics:
    """Calculates backtesting metrics."""

    @staticmethod
    def calculate_returns(portfolio_values: List[float]) -> np.ndarray:
        """Calculate daily returns.
        
        Args:
            portfolio_values: List of portfolio values
            
        Returns:
            Array of daily returns
        """
        return np.diff(portfolio_values) / portfolio_values[:-1]

    @staticmethod
    def calculate_sharpe_ratio(returns: np.ndarray, 
                              risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio.
        
        Args:
            returns: Array of returns
            risk_free_rate: Risk-free rate
            
        Returns:
            Sharpe ratio
        """
        excess_returns = returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    @staticmethod
    def calculate_max_drawdown(portfolio_values: List[float]) -> float:
        """Calculate maximum drawdown.
        
        Args:
            portfolio_values: List of portfolio values
            
        Returns:
            Maximum drawdown
        """
        cummax = np.maximum.accumulate(portfolio_values)
        drawdown = (np.array(portfolio_values) - cummax) / cummax
        return drawdown.min()
