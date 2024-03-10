from datetime import datetime

# Об'єкт datetime, що містить поточну дату та час
now = datetime.now()

# Формат  H:M:S
dt_string = now.strftime("%S")
sec = int(dt_string) * 6
print(" secounds in real time =", dt_string)

