# Railway Management System

class Train:
    def __init__(self, train_number, name, source, destination, seats):
        self.train_number = train_number
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.booked_seats = 0

    def book_ticket(self, num_seats):
        if self.booked_seats + num_seats <= self.seats:
            self.booked_seats += num_seats
            return True
        else:
            return False

    def available_seats(self):
        return self.seats - self.booked_seats


class RailwaySystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train_number, name, source, destination, seats):
        train = Train(train_number, name, source, destination, seats)
        self.trains.append(train)
        print(f"Train {name} added successfully!")

    def display_trains(self):
        if not self.trains:
            print("No trains available.")
            return
        print("\nAvailable Trains:")
        for train in self.trains:
            print(f"Train Number: {train.train_number}, Name: {train.name}, Source: {train.source}, "
                  f"Destination: {train.destination}, Available Seats: {train.available_seats()}")

    def find_train(self, train_number):
        for train in self.trains:
            if train.train_number == train_number:
                return train
        return None

    def book_ticket(self, train_number, num_seats):
        train = self.find_train(train_number)
        if train:
            if train.book_ticket(num_seats):
                print(f"Successfully booked {num_seats} seat(s) on Train {train.name}.")
            else:
                print("Booking failed. Not enough available seats.")
        else:
            print("Train not found.")

    def view_booked_tickets(self):
        print("\nBooked Tickets:")
        for train in self.trains:
            if train.booked_seats > 0:
                print(f"Train {train.name} (Train Number: {train.train_number}): "
                      f"{train.booked_seats} seat(s) booked.")
        print()


def main():
    system = RailwaySystem()

    while True:
        print("\nRailway Management System")
        print("1. Add Train")
        print("2. Display Trains")
        print("3. Book Ticket")
        print("4. View Booked Tickets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            train_number = input("Enter Train Number: ")
            name = input("Enter Train Name: ")
            source = input("Enter Source Station: ")
            destination = input("Enter Destination Station: ")
            seats = int(input("Enter Total Seats: "))
            system.add_train(train_number, name, source, destination, seats)

        elif choice == "2":
            system.display_trains()

        elif choice == "3":
            train_number = input("Enter Train Number: ")
            num_seats = int(input("Enter Number of Seats to Book: "))
            system.book_ticket(train_number, num_seats)

        elif choice == "4":
            system.view_booked_tickets()

        elif choice == "5":
            print("Exiting Railway Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
