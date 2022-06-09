from enum import Enum

class Type(Enum):
    NUMBER   = 0
    PLUS     = 1
    MINUS    = 2
    MULTIPLY = 3
    DIVIDE   = 4
    LPAREN   = 5
    RPAREN   = 6

class Token:
    def __init__(self, type: Type, value: any = None) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        return self.type.name + (f":{self.value}" if self.value != None else "")