class Guest:
    def __init__(self, name, id, bring_list=None):
        self.name = name
        self.id = id
        self.bring_list = bring_list

    def print_guests_bring_list(self):
        print(f"{self.name}:")
        for item in self.bring_list:
            print(item.to_string())


class Host:
    def __init__(self, name, id):
        self.name = name
        self.id = id


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
                current_guest.bring_list.append(Item(item.name, item.amount + take_amount))
                break


class GuestList:
    def __init__(self, list=None):
        self.list = list

    def print_guests_items(self):
        print("\n")
        for guest in self.list:
            if guest.bring_list is not None:
                guest.print_guests_bring_list()
        print("\n")


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def to_string(self):
        return f"- {self.amount} x {self.name}"
