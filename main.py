#!/usr/bin/env python
"""Main entry point for AI Hedgefund."""

import logging
import argparse
from datetime import datetime

from data.fetcher import MarketDataFetcher
from data.processor import DataProcessor
from backtesting.backtest import Backtester
from trading.engine import TradingEngine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/hedgefund.log'),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='AI Hedgefund Trading System')
    parser.add_argument('--mode', choices=['backtest', 'live'], default='backtest',
                       help='Trading mode')
    parser.add_argument('--symbols', nargs='+', default=['AAPL', 'MSFT', 'GOOGL'],
                       help='Stock symbols to trade')
    parser.add_argument('--start-date', type=str, default='2023-01-01',
                       help='Start date for backtesting')
    parser.add_argument('--end-date', type=str, default='2023-12-31',
                       help='End date for backtesting')
    parser.add_argument('--initial-capital', type=float, default=1000000,
                       help='Initial capital')
    
    args = parser.parse_args()
    
    logger.info(f'Starting AI Hedgefund - Mode: {args.mode}')
    
    if args.mode == 'backtest':
        logger.info(f'Running backtest from {args.start_date} to {args.end_date}')
        
        # Initialize components
        fetcher = MarketDataFetcher(args.symbols)
        processor = DataProcessor()
        backtester = Backtester(args.initial_capital)
        
        # Fetch data
        start = datetime.strptime(args.start_date, '%Y-%m-%d')
        end = datetime.strptime(args.end_date, '%Y-%m-%d')
        data = fetcher.fetch_ohlcv(start, end)
        
        # Process data
        processed_data = {}
        for symbol, df in data.items():
            processed_data[symbol] = processor.prepare_features(df)
        
        # Run backtest
        results = backtester.backtest(processed_data, start, end)
        
        logger.info(f'Backtest complete. Results: {results}')
        
    elif args.mode == 'live':
        logger.info('Starting live trading mode')
        # Implementation for live trading
        pass


if __name__ == '__main__':
    main()
