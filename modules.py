class Parking:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.vehicles=int(file.read())

    def welcome(self):
        print("Welcome back boss. Just reminding you the possible commands.")

    def limit(self, spots):
        self.spots=spots
        print("At the moment there are {} trucks parked in your facility.".format(self.vehicles))
        print("Keep in mind that you can only handle {} trucks on your facility".format(spots))

    def plus(self, entrances):
        if self.vehicles + int(entrances) <= self.spots:
            self.vehicles = self.vehicles + entrances
            print("The new number of parked trucks is: {}. \n".format(self.vehicles))
        else:
            print("Be careful! The limit is only: ",self.spots)
            print("You can only add {} more trucks!".format(self.spots - self.vehicles))

    def minus(self, entrances):
        if self.vehicles-entrances >= 0:
            self.vehicles=self.vehicles-entrances
            print("The new number of parked trucks is: {}. \n".format(self.vehicles))
        else:
            print("Are you sure about that?")
            print("I can see that there are are only {} trucks parked at the moment. \n".format(self.vehicles))

    def check(self):
        a = self.vehicles
        print("The number of parked trucks at the moment is: {} ".format(a))

    def help(self):
        print("\n 1) In order to add a truck, please type plus\n 2) In order to remove a truck, please type minus")
        print(" 3) In order to check the number of trucks parked at the moment, please type check")
        print(" 4) In order to check the total limit of your parking, plese type limit")
        print(" 5) In order to get some help, please type help\n")

    def exit(self):
        print("Until next time...")

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.vehicles))

parking=Parking("spots.txt")