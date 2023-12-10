from enum import Enum

class DictKeys(Enum):
    TITLE = "title"
    DEVELOPER = "developer"
    YEAR = "year"
    ADD = "+"
    REMOVE = "-"

game_info = {
    DictKeys.TITLE: "Conway's Game of Life",
    DictKeys.DEVELOPER: "Nicholas St-Jacques",
    DictKeys.YEAR: "2023"
}

ui_string = {
    DictKeys.ADD: "+",
    DictKeys.REMOVE: "-"
}