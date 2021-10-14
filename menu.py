menu_text = """Válassz a menüpontok közül!
1. Új név rögzítése
2. Nevek listázása
3. Kilépés
"""

menu_input = "1"
menu_print = "2"
menu_exit = "3"

names = []

selected_menu = 0
while selected_menu != menu_exit:
    selected_menu = input(menu_text)
    print("Valasztott menüpont: " + selected_menu)
    if selected_menu == menu_input:
        name = input("Írd be a nevet!\n")
        names.append(name)
    elif selected_menu == menu_print:
        for name in names:
            print(name)
    elif selected_menu == menu_exit:
        print("Good by")
    else:
        print("Ismeretlen menüpont!")
