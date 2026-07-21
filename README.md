# AI Hedgefund - Automated Trading System

A comprehensive AI-powered automated trading system for hedgefunds with machine learning models, real-time data processing, and risk management.

## Project Structure

```
ai-hedgefund/
├── data/                      # Data pipeline and management
├── models/                    # ML/AI models
├── trading/                   # Trading engine
├── backtesting/               # Backtesting framework
├── infrastructure/            # Cloud and system setup
├── config/                    # Configuration files
├── tests/                     # Unit and integration tests
├── docs/                      # Documentation
└── requirements.txt           # Python dependencies
```

## Features

- **Real-time Market Data** - Ingestion and processing of market data
- **ML Models** - Price prediction, risk assessment, sentiment analysis
- **Trading Engine** - Order execution and position management
- **Backtesting** - Historical performance evaluation
- **Risk Management** - Portfolio optimization and risk controls
- **Monitoring** - Real-time alerts and performance tracking

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/amamalik1407-gif/ai-hedgefund.git
cd ai-hedgefund
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure your settings
```bash
cp config/example.yaml config/config.yaml
```

4. Run backtesting
```bash
python -m backtesting.runner
```

## Architecture

### Data Pipeline
- Market data collection
- Data validation and cleaning
- Feature engineering
- Data storage (PostgreSQL/TimescaleDB)

### ML Models
- Time series forecasting (LSTM, Transformer)
- Risk prediction
- Sentiment analysis
- Portfolio optimization

### Trading Engine
- Order routing
- Execution management
- Position tracking
- P&L calculation

### Risk Management
- Stop-loss and take-profit
- Position sizing
- Portfolio hedging
- Drawdown monitoring

## Tech Stack

- **Language**: Python 3.9+
- **ML Frameworks**: TensorFlow, PyTorch, Scikit-learn
- **Data**: Pandas, NumPy, PolARS
- **Databases**: PostgreSQL, Redis, TimescaleDB
- **APIs**: FastAPI, Alpaca, Interactive Brokers
- **Cloud**: AWS/GCP (optional)
- **Monitoring**: Prometheus, Grafana

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Edit `config/config.yaml` with your trading parameters:

```yaml
trading:
  symbols: ['AAPL', 'MSFT', 'GOOGL']
  initial_capital: 1000000
  max_drawdown: 0.20
  risk_per_trade: 0.02

models:
  prediction_horizon: 5
  lookback_window: 252
  confidence_threshold: 0.65

broker:
  api_key: ${BROKER_API_KEY}
  api_secret: ${BROKER_API_SECRET}
```

## Development

### Running Tests
```bash
pytest tests/
```

### Running Backtests
```bash
python backtesting/runner.py --config config/config.yaml --start-date 2020-01-01
```

### Starting Trading Agent
```bash
python trading/agent.py --mode live
```

## API Reference

See [API Documentation](docs/API.md)

## Performance Metrics

- Sharpe Ratio
- Sortino Ratio
- Max Drawdown
- Win Rate
- Profit Factor

## Risk Disclaimers

⚠️ **WARNING**: This is an experimental trading system. Trading and investing involve substantial risk of loss. Past performance is not indicative of future results. Only trade with capital you can afford to lose.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE)

## Support

For issues and questions, please create a GitHub issue or contact the maintainers.
