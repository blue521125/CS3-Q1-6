Lab = "302"
Technician = "Mr. Cruz"
class Lab:
    def __init__(self, room_number: str | int):
        self.room_number = room_number

    def __repr__(self) -> str:
        return f"Lab(room_number={self.room_number!r})"

class Technician:
    def __init__(self, name: str):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj) -> None:
        self.assigned_lab = lab_obj

    def __repr__(self) -> str:
        return f"Technician(name={self.name!r}, assigned_lab={self.assigned_lab!r})"

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assigned_lab.room_number)
