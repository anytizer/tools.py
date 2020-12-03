class NameDTO:
    first = ""
    middle = ""
    last = ""

    def __repr__(self):
        return f"[{self.first} - {self.middle} - {self.last}]"
