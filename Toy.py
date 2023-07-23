#!/usr/bin/env python3

"""
This file is responsible for showing a tutorial example of the builder design pattern.
"""

#: Imports
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


#: Classes
class Toy(ABC): # BUILDER CLASS

    @property
    @abstractmethod
    def build(self) -> None:
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


class ActionFigureBuilder(Toy):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._action_fig_blueprint = BluePrint()

    @property
    def build(self) -> ActionFigure:
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

class BluePrint():

    def __init__(self) -> BluePrint:
        self._blueprint = {}

    def modify(self, part: str, description: str) -> None:
        self._blueprint[part] = description
    
    def __str__(self):
        return str(self._blueprint)

class ActionFigure():

    def __init__(self, blueprint: BluePrint) -> ActionFigure:
        self._action_fig = blueprint

    def describe(self) -> str:
        return f'ActionFigure: {self._action_fig}'

#: Functions
def make_a_toy(config: dict) -> str:
    builder = ActionFigureBuilder()
    action_figure = builder.add_hair(config['hair']).add_clothes(config['clothes']).add_shoes(config['shoes']).build
    return action_figure.describe()

#: Variables
toy_configurations = {
    "superman": {"hair" : "Short Brown", "clothes": "Superman Outfit", "shoes": "None"},
    "batman": {"hair" : "Short Black", "clothes": "Batman Outfit", "shoes": "Black Boots"},
    "wonderwoman": {"hair" : "Long Black", "clothes": "Wonder Woman Outfit", "shoes": "Brown Leather Boots"}
}

if __name__ == "__main__":
    print(make_a_toy(config=toy_configurations["superman"]))
    print(make_a_toy(config=toy_configurations["batman"]))
    print(make_a_toy(config=toy_configurations["wonderwoman"]))
    