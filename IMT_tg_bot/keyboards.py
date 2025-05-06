from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вычислить ИМТ")],
                                     [KeyboardButton(text="Узнать что такое ИМТ")],
                                     [KeyboardButton(text="Категории ИМТ")],
                                     [KeyboardButton(text="Упражнения для тренировки")]],
                           resize_keyboard=True,
                           input_field_placeholder="Чего желаете?")

trening = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Наклоны головой")],
                                        [KeyboardButton(text="Махи руками")],
                                        [KeyboardButton(text="Наклоны вдоль тела")],
                                        [KeyboardButton(text="Растяжка с замком за спиной")],
                                        [KeyboardButton(text="Подьем на носки и на пятки")],
                                        [KeyboardButton(text="Мах ногой вперед назад")],
                                        [KeyboardButton(text="Выход")]],
                              resize_keyboard=True)
