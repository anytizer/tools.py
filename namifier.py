#/bin/python
# https://github.com/anytizer/initials.php/blob/master/src/anytizer/names.php
from NameDTO import NameDTO


class namifier:

    def namify(self, name="") -> NameDTO:
        n = NameDTO()

        parts = name.lower().split(" ")
        for p, part in enumerate(parts):
            parts[p] = part.strip().title()
            if parts[p] == "":
                del parts[p]

        if parts:
            if len(parts) >= 3:
                n.first = parts[0]
                n.last = parts[-1]
                n.middle = " ".join(parts[1:len(parts)-1])
            elif len(parts) == 2:
                n.first = parts[0]
                n.last = parts[1]
            else:
                n.first = name.lower().title()

        return n
