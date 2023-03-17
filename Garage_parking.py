
class ParkingGarage:
    def __init__(self, tickets=list, parking_spaces=list):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}

    def ticket_machine(self):
        self.tickets -= 1
        self.parking_spaces -= 1
        self.current_ticket[self.tickets] = {'paid': False}

    def pay_for_parking(self):
        payment = input("Enter payment amount: ")
        if payment:
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.current_ticket[self.tickets]['paid'] = True

    def leave_garage(self):
        if self.current_ticket[self.tickets]['paid']:
            print("Thank you, have a nice day!")
            self.parking_spaces += 1
            self.tickets += 1
        else:
            payment = input("Please pay for your ticket: ")
            if payment:
                print("Thank you, have a nice day!")
                self.parking_spaces += 1
                self.tickets += 1
                self.current_ticket[self.tickets]['paid'] = True

my_garage = ParkingGarage(10, 10)
my_garage.ticket_machine()
my_garage.pay_for_parking()
my_garage.leave_garage()
