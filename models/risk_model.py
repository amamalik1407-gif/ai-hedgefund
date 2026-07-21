"""Risk model module."""

import logging
from typing import Dict, Optional
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class RiskModel:
    """Calculates and manages trading risks."""

    def __init__(self, var_percentile: float = 0.95):
        """Initialize risk model.
        
        Args:
            var_percentile: Percentile for VaR calculation
        """
        self.var_percentile = var_percentile
        logger.info(f'Initialized {self.__class__.__name__}')

    def calculate_var(self, returns: pd.Series) -> float:
        """Calculate Value at Risk.
        
        Args:
            returns: Series of returns
            
        Returns:
            VaR value
        """
        return returns.quantile(1 - self.var_percentile)

    def calculate_cvar(self, returns: pd.Series) -> float:
        """Calculate Conditional Value at Risk.
        
        Args:
            returns: Series of returns
            
        Returns:
            CVaR value
        """
        var = self.calculate_var(returns)
        return returns[returns <= var].mean()

    def calculate_sharpe_ratio(self, returns: pd.Series, 
                              risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio.
        
        Args:
            returns: Series of returns
            risk_free_rate: Risk-free rate
            
        Returns:
            Sharpe ratio
        """
        excess_returns = returns - risk_free_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)
