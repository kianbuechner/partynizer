import module as m

# Alle Gäste bringen etwas mit und es wird sich darüber abgestimmt, wer was mitbringt.


# Gäste zur Gästeliste hinzufügen (Felix)
# Zugriffsverwaltung (bswp. nur der Gastgeber kann Gäste zur Gästeliste hinzufügen) (Kian)
# Zu- und Absagen (Felix)
# Event Informationen eintragen und darstellen (Gastgeber only) (Kian)
# Event erstellen
# Kategorien für Items/Produkte


guest_list = m.GuestList(
    [m.Host("Moriarty", 0), m.Guest("Sherlock", 1),
     m.Guest("John", 2, [m.Item("Vodka", 3)]),
     m.Guest("Mary", 3, [m.Item("Bier", 8)]),
     m.Guest("Mycroft", 4),
     m.Guest("Molly", 5)])

bring_list = m.BringList([
    m.Item("Cola", 4),
    m.Item("Chips", 2),
    m.Item("Salzstangen", 2),
    m.Item("Fanta", 3)])

event = m.Event(guest_list, bring_list)

menuList = ["",
            "1. Mitbringliste ausgeben",
            "2. Item hinzufügen",
            "3. Item/s zum mitbringen auswählen",
            "4. Items, die die Gäste mitbringen ausgeben",
            "5. Menü ausgeben",
            "6. Programm schließen",
            "7. Eventinformationen bearbeiten",
            "8. Eventinformationen ausgeben"]


def menu():
    printMenu()
    while True:
        selection = input("Wähle eine Nummer für einen Menüpunkt: ")
        if selection == "1":
            print("1. Mitbringliste ausgeben")
            event.print_bring_list()
        elif selection == "2":
            print("2. Item hinzufügen")
            event.add_item_to_bring_list()
        elif selection == "3":
            print("3. Item/s zum mitbringen auswählen")
            event.take_item_from_bring_list(guest_list)
        elif selection == "4":
            print("4. Items, die die Gäste mitbringen ausgeben")
            event.print_guests_items()
        elif selection == "5":
            printMenu()
        elif selection == "6":
            break
        elif selection == "7":
            print("7. Eventinformationen bearbeiten")
            event.set_event_infos()
        elif selection == "8":
            print("8. Eventinformationen ausgeben")
            event.print_event_infos()
        else:
            print("Unbekannte Option gewählt!")


def printMenu():
    print("Menü:")
    for a in menuList:
        print(a)


if __name__ == '__main__':
    menu()
