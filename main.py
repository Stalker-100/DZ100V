count = int(input("Количество видеокарт: "))

cards = [int(input(f"{i + 1} Видеокарта: ")) for i in range(count)]

print(f"старый список видеокарт: {cards}")

max_card = max(cards)
new_cards = [card for card in cards if card != max_card]

print(f"новый список видеокарт: {new_cards}")
