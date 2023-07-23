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
 
    __public_inst: int = 1 # Keeps up with the instance for this class.

 
    def __init__(self, enforce_singleton: bool):
        """
        Constructor that will enforce the class to only have one instance.
        """
        if enforce_singleton:
            if Antenna.__public_inst != 1:
                raise TypeError("Cannot instantiate class - class is desined to be a singleton class.")
            else:
                Antenna.public_inst = self
        self.__x_direction: float = 0.0
        self.__y_direction: float = 0.0
        self.__z_direction: float = 0.0

    def release_singleton(self) -> None:
        self.__public_inst = None

    @staticmethod
    def current_inst() -> int:
        """
        This is a static method that allows a user to obtain the private handle used to ensure
        that the instance is unique.
        """
        if Antenna.public_inst == 1:
            Antenna()
        return Antenna.public_inst
    
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
        antenna = Antenna(enforce_singleton=True)
        print(f"---------FIRST EXAMPLE (START) - ATTEMPT MULTIPLE INSTANTIATIONS ON SINGLETON--------")
        self.__create_two_antennas(Antenna=antenna)
        print(f"--------------------------------FIRST EXAMPLE (END) ---------------------------------\n\n")

        print(f"--------------SECOND EXAMPLE (START) - UPDATE RESOURCE IN SINGLETON CLASS------------")
        self.__new_antenna_direction(Antenna=Antenna(enforce_singleton=False))
        print(f"--------------------------------SECOND EXAMPLE (END) --------------------------------\n\n")
        
        print(f"--------------THIRD EXAMPLE (START) - SHOW SAME OBJECT FOR TWO INSTANCES------------")
        print(f"current antenna object reference: {antenna.current_inst()} <========")
        new_antenna = Antenna(enforce_singleton=False)
        print(f"new antenna object reference: {antenna.current_inst()} <========")

    def __create_two_antennas(self, Antenna: Antenna) -> None:
        """
        Example function of a user trying to make two instances of the singleton class, Antenna.
        We should expect to see an exception being thrown, if the Antenna class has been constructed properly
        as a singleton.
        """
        try:
            print(f"create_two_antennas(): Direction of the current antenna: {Antenna.current_direction()}")
            Additional_Antenna = Antenna()
        except Exception as e:
            print(f"create_two_antennas(): Error occured: {e} <========")

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
        print(f"new_antenna_direction(): instance handle: {Antenna.current_inst()}")


if __name__ == "__main__":
    user = User()
    user.tutorial_example()
