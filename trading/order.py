"""Order management module."""

import logging
from typing import Dict, Optional
from enum import Enum
from datetime import datetime

logger = logging.getLogger(__name__)


class OrderType(Enum):
    """Order types."""
    MARKET = 'market'
    LIMIT = 'limit'
    STOP = 'stop'
    STOP_LIMIT = 'stop_limit'


class OrderStatus(Enum):
    """Order statuses."""
    PENDING = 'pending'
    FILLED = 'filled'
    PARTIALLY_FILLED = 'partially_filled'
    CANCELLED = 'cancelled'
    REJECTED = 'rejected'


class OrderManager:
    """Manages trading orders."""

    def __init__(self):
        """Initialize order manager."""
        self.orders = []
        self.order_id_counter = 0
        logger.info(f'Initialized {self.__class__.__name__}')

    def create_order(self, symbol: str, quantity: float, 
                    order_type: OrderType, side: str,
                    price: Optional[float] = None) -> Dict:
        """Create a new order.
        
        Args:
            symbol: Stock symbol
            quantity: Order quantity
            order_type: Type of order
            side: buy or sell
            price: Price (for limit orders)
            
        Returns:
            Order dictionary
        """
        self.order_id_counter += 1
        order = {
            'id': self.order_id_counter,
            'symbol': symbol,
            'quantity': quantity,
            'type': order_type,
            'side': side,
            'price': price,
            'status': OrderStatus.PENDING,
            'timestamp': datetime.now(),
        }
        self.orders.append(order)
        logger.info(f'Created order #{order["id"]}: {side} {quantity} {symbol}')
        return order

    def cancel_order(self, order_id: int) -> bool:
        """Cancel an order.
        
        Args:
            order_id: Order ID
            
        Returns:
            True if successful
        """
        for order in self.orders:
            if order['id'] == order_id:
                order['status'] = OrderStatus.CANCELLED
                logger.info(f'Cancelled order #{order_id}')
                return True
        logger.warning(f'Order #{order_id} not found')
        return False
