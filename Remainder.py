import datetime
import time


def set_reminder():
    reminder_time = input("Введите время напоминания в формате ЧЧ:ММ: ")
    reminder_text = input("Введите текст напоминания: ")

    current_time = datetime.datetime.now().strftime("%H:%M")
    while current_time != reminder_time:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M")

    print("Напоминание:", reminder_text)


set_reminder()
