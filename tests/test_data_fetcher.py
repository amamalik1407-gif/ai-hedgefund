"""Tests for data fetcher module."""

import pytest
from datetime import datetime, timedelta
from data.fetcher import MarketDataFetcher


class TestMarketDataFetcher:
    """Test cases for MarketDataFetcher."""

    @pytest.fixture
    def fetcher(self):
        """Create a fetcher instance."""
        return MarketDataFetcher(['AAPL', 'MSFT'])

    def test_initialization(self, fetcher):
        """Test fetcher initialization."""
        assert fetcher.symbols == ['AAPL', 'MSFT']
        assert fetcher.data_source == 'yfinance'

    def test_fetch_ohlcv(self, fetcher):
        """Test OHLCV data fetching."""
        start_date = datetime.now() - timedelta(days=30)
        end_date = datetime.now()
        data = fetcher.fetch_ohlcv(start_date, end_date)
        
        assert isinstance(data, dict)
        # Add more assertions based on expected behavior
