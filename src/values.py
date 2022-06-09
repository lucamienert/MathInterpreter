class Number:
    def __init__(self, value: any = None) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"