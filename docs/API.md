# API Documentation

## Overview

The AI Hedgefund system exposes RESTful APIs for portfolio management, trading, and analytics.

## Base URL

```
http://localhost:8080/api/v1
```

## Authentication

All requests require an API key in the header:

```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### Portfolio Endpoints

#### Get Portfolio
```
GET /portfolio
```

Response:
```json
{
  "total_value": 1000000,
  "cash": 500000,
  "positions": [
    {
      "symbol": "AAPL",
      "quantity": 100,
      "entry_price": 150.00,
      "current_price": 160.00
    }
  ]
}
```

#### Get Position
```
GET /portfolio/positions/{symbol}
```

### Trading Endpoints

#### Place Order
```
POST /orders
```

Request Body:
```json
{
  "symbol": "AAPL",
  "quantity": 100,
  "side": "buy",
  "type": "market"
}
```

#### Get Orders
```
GET /orders
```

#### Cancel Order
```
DELETE /orders/{order_id}
```

### Analytics Endpoints

#### Get Performance
```
GET /analytics/performance
```

Response:
```json
{
  "total_return": 0.15,
  "sharpe_ratio": 1.5,
  "max_drawdown": -0.08
}
```

## Error Handling

Errors are returned with appropriate HTTP status codes:

- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Internal Server Error

Error response:
```json
{
  "error": "Error message",
  "code": "ERROR_CODE"
}
```
