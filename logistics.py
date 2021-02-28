"""
Logistics app module!!!
"""
import random
from typing import List
from logistic_help import Location, Item, Vehicle, Order


class LogisticSystem:
    """
    A class used to represent the logistic system with all functions
    """

    def __init__(self, vehicles: List[Vehicle]):
        """
        This function gets the needed information from the paraments
        """
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order: Order):
        """
        This function places the order into the available vehicle if there is
        one, otherwise returns 'There is no available vehicle to deliver an
        order.'
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                vehicle.isAvailable = False
                break
            else:
                return 'There is no available vehicle to deliver an order.'

    def trackOrder(self, orderId: int):
        """
        This function tracks the order if it exists, if not - returns "No such
        order"
        """
        for order in self.orders:
            if orderId == order.orderId:
                return f'Your order #{orderId} is sent to {order.city}. Total \
price: {order.calculateAmount()} UAH.'
            else:
                return "No such order"
