"""Data processing module."""

import logging
from typing import Dict, Optional
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes and prepares data for model training."""

    def __init__(self):
        """Initialize the data processor."""
        self.scaler = StandardScaler()
        logger.info(f'Initialized {self.__class__.__name__}')

    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate technical indicators.
        
        Args:
            df: OHLCV DataFrame
            
        Returns:
            DataFrame with technical indicators
        """
        # Moving averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['EMA_12'] = df['Close'].ewm(span=12).mean()
        df['EMA_26'] = df['Close'].ewm(span=26).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        df['MACD'] = df['EMA_12'] - df['EMA_26']
        df['Signal_Line'] = df['MACD'].ewm(span=9).mean()
        df['MACD_Histogram'] = df['MACD'] - df['Signal_Line']
        
        # Bollinger Bands
        df['BB_Middle'] = df['Close'].rolling(window=20).mean()
        df['BB_Std'] = df['Close'].rolling(window=20).std()
        df['BB_Upper'] = df['BB_Middle'] + (df['BB_Std'] * 2)
        df['BB_Lower'] = df['BB_Middle'] - (df['BB_Std'] * 2)
        
        # Volume indicators
        df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
        
        return df

    def prepare_features(self, df: pd.DataFrame, 
                        lookback: int = 252) -> Optional[pd.DataFrame]:
        """Prepare features for model.
        
        Args:
            df: DataFrame with technical indicators
            lookback: Number of days to look back
            
        Returns:
            DataFrame with features ready for model
        """
        df_clean = df.dropna()
        if len(df_clean) < lookback:
            logger.warning(f'Insufficient data: {len(df_clean)} < {lookback}')
            return None
        
        return df_clean
