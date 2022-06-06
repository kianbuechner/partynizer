import module as m

# Alle Gäste bringen etwas mit und es wird sich darüber abgestimmt, wer was mitbringt.

host = m.Host("Moriarty", 0)

guest_list = m.GuestList(
    [m.Guest("Sherlock", 0),
     m.Guest("John", 1, [m.Item("Vodka", 3)]),
     m.Guest("Mary", 2, [m.Item("Bier", 8)]),
     m.Guest("Mycroft", 3),
     m.Guest("Molly", 4)])

bring_list = m.BringList([
    m.Item("Cola", 4),
    m.Item("Chips", 2),
    m.Item("Salzstangen", 2),
    m.Item("Fanta", 3)])

menuList = ["",
            "1. Mitbringliste ausgeben",
            "2. Item hinzufügen",
            "3. Item/s zum mitbringen auswählen",
            "4. Items, die die Gäste mitbringen ausgeben",
            "5. Menü ausgeben",
            "6. Programm schließen"]


def menu():
    printMenu()
    while True:
        selection = input("Wähle eine Nummer für einen Menüpunkt: ")
        if selection == "1":
            print("1. Mitbringliste ausgeben")
            bring_list.print_bring_list()
        elif selection == "2":
            print("2. Item hinzufügen")
            bring_list.add_item_to_bring_list()
        elif selection == "3":
            print("3. Item/s zum mitbringen auswählen")
            bring_list.take_item_from_bring_list(guest_list)
        elif selection == "4":
            print("4. Items, die die Gäste mitbringen ausgeben")
            guest_list.print_guests_items()
        elif selection == "5":
            printMenu()
        elif selection == "6":
            break
        else:
            print("Unbekannte Option gewählt!")


def printMenu():
    print("Menü:")
    for a in menuList:
        print(a)


if __name__ == '__main__':
    menu()
