# import random

# # Функция для вытягивания 4 случайных карт и проверки их масти
# def draw_and_check(cards_per_suit, total_cards):
#     # Создаем колоду с 36 картами, представленную списком
#     deck = ['пики'] * cards_per_suit + ['черви'] * cards_per_suit + ['бубны'] * cards_per_suit + ['трефы'] * cards_per_suit
    
#     # Вытягиваем 4 случайные карты из колоды
#     hand = random.sample(deck, 4)
    
#     # Проверяем, все ли карты одной масти
#     return all(card == hand[0] for card in hand)

# # Количество карт одной масти
# cards_per_suit = 9

# # Общее количество карт в колоде
# total_cards = 36

# # Количество экспериментов
# num_experiments = 100000  # Вы можете увеличить это число для более точных результатов

# # Счетчик успешных экспериментов (все 4 карты одной масти)
# success_count = 0

# # Проводим серию экспериментов
# for _ in range(num_experiments):
#     if draw_and_check(cards_per_suit, total_cards):
#         success_count += 1

# # Рассчитываем вероятность
# probability = success_count / num_experiments

# # Выводим результат
# print(f"Вероятность того, что 4 случайно выбранные карты будут одной масти: {probability:.2%}")

# cards = [i for i in range(1, 10)]

# print(cards)
# cards2 = [i for i in range(10,18)]
# print(cards2)

