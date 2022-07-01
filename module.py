from datetime import datetime


class Event:
    def __init__(self, guest_list, bring_list):
        self.date = None
        self.location = None
        self.description = None
        self.guest_list = guest_list
        self.bring_list = bring_list

    def print_bring_list(self):
        self.bring_list.print_bring_list()

    def add_item_to_bring_list(self):
        self.bring_list.add_item_to_bring_list()

    def take_item_from_bring_list(self, guest_list):
        self.bring_list.take_item_from_bring_list(guest_list)

    def print_guests_items(self):
        self.guest_list.print_guests_items()

    def set_event_infos(self):
        date = input("Gib das Datum und die Uhrzeit deines Events ein (Format: dd.mm.yy hh:mm):")
        self.date = datetime.strptime(date, '%d.%m.%y %H:%M')
        self.location = input("Gib die Adresse deines Events ein:")
        self.description = input("Gib die Beschreibung deines Events ein:")

    def print_event_infos(self):
        print("Datum: ", self.date.strftime('%d.%m.%y'))
        print("Uhrzeit: ", self.date.strftime('%H:%M Uhr'))
        print("Ort: ", self.location)
        print("Beschreibung: ", self.description)


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.guests_bring_list = None


class Guest(User):
    def __init__(self, name, id, guests_bring_list=None):
        super().__init__(name, id)
        self.guests_bring_list = guests_bring_list

    def print_guests_bring_list(self):
        print(f"{self.name}:")
        for item in self.guests_bring_list:
            print(item.to_string())


class Host(User):
    def __init__(self, name, id):
        super().__init__(name, id)


class BringList:
    def __init__(self, list=None):
        self.list = list

    def print_bring_list(self):
        print("\n", "Mitbringliste: ")
        for item in self.list:
            print(item.to_string())
        print("\n")

    def add_item_to_bring_list(self):
        new_item = input("Gib den Namen des Items ein, welches du hinzufügen möchtest: ")
        new_amount = int(input("Gib die Menge des Items ein, welches du hinzufügen möchtest: "))
        self.list.append(Item(new_item, new_amount))

    def take_item_from_bring_list(self, guest_list):
        self.print_bring_list()
        guest_name = input("Gib deinen Namen ein: ")
        current_guest = None
        for guest in guest_list.list:
            if guest.name == guest_name:
                current_guest = guest
                break
        if current_guest is None:
            return print("Du bist nicht auf der Gästeliste!")
        take_name = input("Gib den Namen des Items ein, welches du mitbringen möchtest: ")
        take_amount = int(input("Gib die Menge des Items ein, welches du mitbringen möchtest: "))
        for item in self.list:
            if take_name == item.name:
                item.amount = item.amount - take_amount
                if item.amount <= 0:
                    self.list.remove(item)
                current_guest.guests_bring_list.append(Item(item.name, item.amount + take_amount))
                break


class GuestList:
    def __init__(self, list=None):
        self.list = list

    def print_guests_items(self):
        print("\n")
        for guest in self.list:
            if guest.guests_bring_list is not None:
                guest.print_guests_bring_list()
        print("\n")


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def to_string(self):
        return f"- {self.amount} x {self.name}"
