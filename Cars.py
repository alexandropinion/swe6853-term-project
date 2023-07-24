#!/usr/bin/env python3

"""
This file is responsible for showing a tutorial example of the abstract factory design pattern.
"""

#: Imports
from abc import ABC, abstractmethod

#: Classes
class Cars(ABC): # ABSTRACT FACTORY
    """
    The primary interface that declares a collection of procedures for constructing abstract product objects is this one. 
    It normally consists of a number of factory processes, each of which is in charge of producing a certain product type. 
    An interface or an abstract class can both be used for the Abstract Factory.
    """

    @abstractmethod
    def create_car(self, suv: bool):
        pass


class Sedan(ABC): # ABSTRACT PRODUCT
    """
    These are interfaces or abstract classes that specify the shared methods for the various family members' products. 
    A family of products has a corresponding Abstract Product for each product type.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    # Interface
    @abstractmethod
    def create_car(self, suv: bool):
        pass


class SUV(ABC): # ABSTRACT PRODUCT
    """
    These are interfaces or abstract classes that specify the shared methods for the various family members' products. 
    A family of products has a corresponding Abstract Product for each product type.

    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    @abstractmethod
    def create_car(self, suv: bool):
        pass


class FordFusion(Sedan): # CONCRETE PRODUCT A1
    """
    The Abstract Product interface is implemented by Concrete Product classes. 
    Each Concrete Factory is in charge of producing a certain range of Concrete Products. 
    The real objects that the client programs will use are represented by these products.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    def create_car(self, suv: bool):
        self.name: str = "Ford Fusion"
        self.type: str = "Sedan"


class HondaCivic(Sedan): # CONCRETE PRODUCT A2
    """
    The Abstract Product interface is implemented by Concrete Product classes. 
    Each Concrete Factory is in charge of producing a certain range of Concrete Products. 
    The real objects that the client programs will use are represented by these products.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    def create_car(self, suv: bool):
        self.name: str = "Honda Civic"
        self.type: str = "Sedan"


class FordExplorer(SUV): # CONCRETE PRODUCT B1
    """
    The Abstract Product interface is implemented by Concrete Product classes. 
    Each Concrete Factory is in charge of producing a certain range of Concrete Products. 
    The real objects that the client programs will use are represented by these products.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    def create_car(self, suv: bool):
        self.name: str = "Ford Explorer"
        self.type: str = "SUV"


class HondaPilot(SUV): # CONCRETE PRODUCT B2
    """
    The Abstract Product interface is implemented by Concrete Product classes. 
    Each Concrete Factory is in charge of producing a certain range of Concrete Products. 
    The real objects that the client programs will use are represented by these products.
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.type: str

    def create_car(self, suv: bool):
        self.name: str = "Honda Pilot"
        self.type: str = "SUV"




class DomesticCar(Cars): # CONCRETE FACTORY 1
    """
    The Abstract Factory interface is implemented by Concrete Factory classes. 
    Each concrete plant is in charge of producing a group of connected goods. 
    """
    
    def create_car(self, suv: bool):
        if suv:
            return FordExplorer()
        else:
            return FordFusion()


class InternationalCar(Cars): # CONCRETE FACTORY 2
    """
    The Abstract Factory interface is implemented by Concrete Factory classes. 
    Each concrete plant is in charge of producing a group of connected goods.
    """
    def create_car(self, suv: bool):
        if suv:
            return HondaPilot()
        else:
            return HondaCivic()

    

def client(): 
    """
    The client code is in charge of building families of related objects using the Abstract Factory and Abstract Product interfaces. 
    It is unaware of the specific product classes or the methods used in their production. 
    Instead, it uses the objects' abstract interfaces to interact with them.
    """
    for factory in (DomesticCar(), InternationalCar()):
        product1 = factory.create_car(suv=True)
        product2 = factory.create_car(suv=False)
        print(f"This is factory # {factory.__class__} <-----\nProduct A: {product1}\nProduct B: {product2}\n\n\n")


if __name__ == "__main__":
    client()