"""
Additional parts for logistic system!!!
"""
import random
from typing import List


class Item:
    """
    A class used to represent an Item
    ...
    Attributes
    ----------
    name : str
        the name of the Item
    price : float
        the price of the Item
    """

    def __init__(self, name: str, price: float):
        """
        This function gets the needed information from the paraments
        Parameters
        ----------
        name : str
        the name of the Item
        price : float
            the price of the Item
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        This function returns the object in text form
        >>> 
        >>> item = Item('Socks', 25.50)
        >>> print(item)
        Name: Socks | Price: 25.5
        """
        return f'Name: {self.name} | Price: {self.price}'


class Location:
    """
    A class used to represent the Location
    ...
    Attributes
    ----------
    city : str
            the location of the city
    postoffice : int
        the number of a postoffice
    """

    def __init__(self, city: str, postoffice: int):
        """
        This function gets the needed information from the paraments
        Parameters
        ----------
        city : str
            the location of the city
        postoffice : int
            the number of a postoffice
        """
        self.city = city
        self.postoffice = postoffice


class Vehicle:
    """
    A class used to represent the Vehicle
    ...
    Attributes
    ----------
    vehicleNo : int
        the number of the vehicle
    isAvailable : bool
        the status of availability of the vehicle
    """

    def __init__(self, vehicleNo: int):
        """
        This function gets the needed information from the paraments
        Parameters
        ----------
        vehicleNo : int
            the number of the vehicle
        isAvailable : bool
            the status of availability of the vehicle
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    """
    A class used to represent an Order
    ...
    Attributes
    ----------
    user_name : str
        the user_name of the Order
    city : str
        the city of the Order
    items: list
        the items of the Order
    postoffice: int
        the postoffice of the Order
    """

    def __init__(self, user_name: str, city: str, items: List[Item], postoffice: int):
        """
        This function gets the needed information from the paraments
        Parameters
        ----------
        user_name : str
            the user_name of the Order
        city : str
            the city of the Order
        items: list
            the items of the Order
        postoffice: int
            the postoffice of the Order
        """
        order_id = random.randint(100000000, 999999999)
        self.orderId = order_id
        self.city = city
        self.user_name = user_name
        self.items = items
        self.postoffice = postoffice
        self.vehicle = None
        self.location = Location(city, postoffice)

    def __str__(self):
        """
        This function returns the object in text form
        """
        return f'Your order number is {self.orderId}.'

    def calculateAmount(self):
        """
        Returns and calculates the sum of the order
        """
        summa = 0
        for item in self.items:
            summa += item.price
        return summa

    def assignVehicle(self, vehicle: Vehicle):
        '''
        Function returns True if the vehicle is available and False otherwise
        '''
        return vehicle.isAvailable
