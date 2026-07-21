"""Market data fetcher module."""

import logging
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


class MarketDataFetcher:
    """Fetches market data from various sources."""

    def __init__(self, symbols: List[str], data_source: str = 'yfinance'):
        """Initialize the data fetcher.
        
        Args:
            symbols: List of stock symbols
            data_source: Data source (yfinance, alpha_vantage, etc.)
        """
        self.symbols = symbols
        self.data_source = data_source
        logger.info(f'Initialized {self.__class__.__name__} with {len(symbols)} symbols')

    def fetch_ohlcv(self, 
                    start_date: datetime, 
                    end_date: datetime,
                    interval: str = '1d') -> Dict[str, pd.DataFrame]:
        """Fetch OHLCV data.
        
        Args:
            start_date: Start date for data
            end_date: End date for data
            interval: Data interval (1d, 1h, 5m, etc.)
            
        Returns:
            Dictionary of DataFrames for each symbol
        """
        data = {}
        for symbol in self.symbols:
            try:
                logger.info(f'Fetching data for {symbol}')
                df = yf.download(symbol, start=start_date, end=end_date, interval=interval)
                data[symbol] = df
            except Exception as e:
                logger.error(f'Error fetching data for {symbol}: {e}')
        return data

    def fetch_fundamental_data(self, symbol: str) -> Dict:
        """Fetch fundamental data for a symbol.
        
        Args:
            symbol: Stock symbol
            
        Returns:
            Dictionary of fundamental data
        """
        try:
            ticker = yf.Ticker(symbol)
            return {
                'pe_ratio': ticker.info.get('trailingPE'),
                'pb_ratio': ticker.info.get('priceToBook'),
                'dividend_yield': ticker.info.get('dividendYield'),
                'market_cap': ticker.info.get('marketCap'),
                'revenue': ticker.info.get('totalRevenue'),
            }
        except Exception as e:
            logger.error(f'Error fetching fundamental data for {symbol}: {e}')
            return {}
