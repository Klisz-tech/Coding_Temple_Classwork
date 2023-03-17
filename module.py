'''def lst_combo():
    lst1 = ["Frodo", "Bilbo", "Gandalf", "Oakenshield", "Legolas"]
    lst2 = ["Hobbit","Hobbit","Wizard","Dwarf","Elf"]
    lst3 = ["Toyota", "Honda", "Lexus","Acura", "Chevy"]
    lst4 = ["4runner","Civic", "LS300", "NSX" ,"1970 SS Chevelle hardtop" ]

    first_dict = dict(zip(lst1,lst2))
    second_dict = dict(zip(lst3,lst4))
    return first_dict, second_dict
print(lst_combo())
'''

class CarOne():
    model = "sports"
    
    def __init__(self, doors=2,seats=6, color="Hot pink"):
        self.color = color
        self.doors = doors
        self.seats = seats
    
honda = CarOne(4,6,"yellow")
print(honda.doors, honda.color, honda.seats, honda.model)

#How do I index an attribute item within invoking paranthesis to make the change

class SecondCar():
    model = "Coupe"
    top_speed = 165
    interior = 'velvet'
    accessories = "Fuzzy dice"

    def __init__(self, color, doors, seats):
        self.color = color
        self.doors = doors
        self.seats = seats
crown_vic = SecondCar('bright orange', '4-door', '1 racing seat')
print(crown_vic.model, crown_vic.interior, crown_vic.accessories)
print(crown_vic())
