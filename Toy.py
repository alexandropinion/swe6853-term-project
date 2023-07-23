#!/usr/bin/env python3

"""
This file is responsible for showing a tutorial example of the builder design pattern.
"""

#: Imports
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


#: Classes
class ToyBuilder(ABC): # BUILDER 
    """
    The techniques for generating the various components of the Product are specified in the Builder interface. 
    It describes typical steps to build the Product and abstracts the building process. 
    It typically contains instructions on how to configure options, set attributes, and assemble the finished product.
    """

    @property
    @abstractmethod
    def construct(self) -> None:
        pass

    @abstractmethod
    def add_hair(self) -> None:
        pass

    @abstractmethod
    def add_clothes(self) -> None:
        pass

    @abstractmethod
    def add_shoes(self) -> None:
        pass


class ActionFigureBuilder(ToyBuilder):  # CONCRETE BUILDER
    """
    The classes that implement the Builder interface are called Concrete Builders. 
    Each Concrete Builder gives the Product specific implementations for building. 
    They contain the state and logic required to assemble the various Product components.
    """
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._action_fig_blueprint = BluePrint()

    @property
    def construct(self) -> ActionFigure:
        finished_blueprint = self._action_fig_blueprint
        self.reset()
        action_fig = ActionFigure(finished_blueprint)
        return action_fig

    def add_hair(self, type: str) -> ActionFigureBuilder:
        self._action_fig_blueprint.modify("Hair", type)
        return self

    def add_clothes(self, type: str) -> ActionFigureBuilder:
        self._action_fig_blueprint.modify("Clothes", type)
        return self

    def add_shoes(self, type: str) -> ActionFigureBuilder:
        self._action_fig_blueprint.modify("Shoes", type)
        return self
    
class ActionFigure(): # PRODUCT
    """
    Using the Builder pattern, you should produce this sophisticated object. 
    It normally consists of a number of components or characteristics, and it may come in a variety of forms or variations.
    """

    def __init__(self, blueprint: BluePrint) -> ActionFigure:
        self._action_fig = blueprint

    def describe(self) -> str:
        return f'ActionFigure: {self._action_fig}'

class BluePrint(): # COMPLEX OBJECT
    
    def __init__(self) -> BluePrint:
        self._blueprint = {}

    def modify(self, part: str, description: str) -> None:
        self._blueprint[part] = description
    
    def __str__(self):
        return str(self._blueprint)

class Client():
    """
    It is the Client's responsibility to build the Product using the Builder pattern. 
    To build the Product step-by-step, it either constructs a Builder object and provides it to the Director (if one is available) 
    or utilizes the Builder's methods directly.
    """

    def create_a_toy(self, config: dict) -> str:
        """
        The Director, which is optional, offers a more advanced interface for building the Product with the Builder. 
        It conceals the specifics of the building procedure and offers instructions for building the Product in a particular sequence or with a particular configuration.
        """
        director = ActionFigureBuilder()
        action_figure = director.add_hair(config['hair']).add_clothes(config['clothes']).add_shoes(config['shoes']).construct 
        return action_figure.describe()

#: Variables
toy_configurations = {
    "superman": {"hair" : "Short Brown", "clothes": "Superman Outfit", "shoes": "None"},
    "batman": {"hair" : "Short Black", "clothes": "Batman Outfit", "shoes": "Black Boots"},
    "wonderwoman": {"hair" : "Long Black", "clothes": "Wonder Woman Outfit", "shoes": "Brown Leather Boots"}
}

if __name__ == "__main__":
    client = Client()
    print(client.create_a_toy(config=toy_configurations["superman"]))
    print(client.create_a_toy(config=toy_configurations["batman"]))
    print(client.create_a_toy(config=toy_configurations["wonderwoman"]))
    