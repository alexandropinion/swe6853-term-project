#!/usr/bin/env python3

"""
This file is responsible for showing a tutorial example of the singleton design pattern.
"""

#: Imports
import random

#: Classes
class Antenna():  # Singleton class
    """
    Lets say we have a class, Antenna, that can handle the direction of a singlular antenna. Since we do not
    have multiple antennas, and we only have one resource available, we will want to ensure that the class
    controlling our one resource cannot be instantiated multiple times - this would cause a conflict with
    our one resource, and could break something!
    """
 
    __singleton_instance: int = None # Keeps up with the instance for this class.

    def __new__(cls):
        """
        This method acts as a static method that will create a new instance of the class by taking in the 
        current instance of the class that it was called by.  This is how we can ensure that only one 
        instance of the class is used, and how we can instantiate the singleton.
        """
        if cls.__singleton_instance is None:
            cls.__singleton_instance = super(Antenna, cls).__new__(cls)
        return cls.__singleton_instance

 
    def __init__(self):
        """
        Constructor used to initialize class-specific variables.
        """
        self.__x_direction: float = 0.0
        self.__y_direction: float = 0.0
        self.__z_direction: float = 0.0

    def release_singleton(self) -> None:
        self.__singleton_instance = None

    @staticmethod
    def current_inst() -> int:
        """
        This is a static method that allows a user to obtain the private handle used to ensure
        that the instance is unique.
        """
        if Antenna.__singleton_instance == 1:
            Antenna()
        return Antenna.__singleton_instance
    
    @classmethod
    def get_instance(cls):
        """
        This is the method that should be called in order to instantiate the singleton class.
        """
        if cls.__singleton_instance is None:
            print('Creating new instance')
            cls.__singleton_instance = cls.__new__(cls)
        return cls._instance
    
    # def get_instance(self) -> int:
    #     self.__singleton_instance = 1
    #     return self.__singleton_instance
    
    def current_direction(self) -> tuple:
        """
        Returns the current direction of the antenna
        """
        return (self.__x_direction, self.__y_direction, self.__z_direction)
    
    def update_direction(self, x: float, y: float, z: float) -> None:
        """
        Updates the current direction of the antenna.
        """
        self.__x_direction = x
        self.__y_direction = y
        self.__z_direction = z

class User():
    def tutorial_example(self) -> None:
        
        antenna: Antenna = None
        
        print(f"---------FIRST EXAMPLE (START) - ATTEMPT MULTIPLE INSTANTIATIONS ON SINGLETON--------")
        antenna1 = Antenna()
        antenna2 = Antenna()
        print(f"Antenna1 object = {antenna1}  <=========\nAntenna2 object = {antenna2}  <=========\nThey are the same: {antenna1 is antenna2}")
        print(f"--------------------------------FIRST EXAMPLE (END) ---------------------------------\n\n")

        print(f"--------------SECOND EXAMPLE (START) - UPDATE RESOURCE IN SINGLETON CLASS------------")
        print(f"Reading antenna 1 and 2's direction, then passing antenna1 a new antenna direction. Lastly, we will read back antenna 2's direction.")
        print(f"Current antenna 1 direction: {antenna1.current_direction()}\nCurrent antenna 2 direction: {antenna2.current_direction()}")
        print(f"Updating antenna 1's direction...")
        self.__new_antenna_direction(Antenna=antenna1)
        print(f"Reading back antenna 2's direction: {antenna2.current_direction()}")
        print(f"--------------------------------SECOND EXAMPLE (END) --------------------------------\n\n")

    def __new_antenna_direction(self, Antenna: Antenna) -> None:
        """
        We will update the resources inside the singleton and ensure that the updated resource(s) remain
        for the singular allowable instance of the singleton class.
        """
        print(f"new_antenna_direction(): Current antenna direction: {Antenna.current_direction()}")
        new_x: float = random.random()
        new_y: float = random.random()
        new_z: float = random.random()
        print(f"new_antenna_direction(): The new desired x, y, and z direction for the antenna is: {new_x}, {new_y}, {new_z}")
        Antenna.update_direction(x=new_x, y=new_y, z=new_z)
        print(f"new_antenna_direction(): New antenna direction: {Antenna.current_direction()}")


if __name__ == "__main__":
    user = User()
    user.tutorial_example()
