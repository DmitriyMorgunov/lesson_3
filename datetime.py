
from datetime import datetime, timedelta
import calendar

date_now = datetime.now()
days_in_month = calendar.monthrange(date_now.year, date_now.month)[1]

print('Вчера: ' + datetime.strftime(date_now + timedelta(days=-1), '%d-%m-%Y'))
print('Сегодня: ' + datetime.strftime(date_now, '%d-%m-%Y'))
print('Завтра: ' + datetime.strftime(date_now + timedelta(days=1), '%d-%m-%Y'))
""" Ниже намеренно решил отнимать количество дней в текущем месяце, т.к. у этой задачки могут быть самые разные решения,
всё зависит от решаемой задачи. Можно было бы сделать так, чтобы выводилось то же число, но месяц назад, либо если это
31 марта, тогда выводить 29 или 28 февраля, т.е. максимальное количество дней в прошлом месяце."""
print('Месяц назад: ' + datetime.strftime(date_now + timedelta(days=-days_in_month), '%d-%m-%Y'))

datetime_from_string = datetime.strptime("01/01/17 12:10:03.234567", '%d/%M/%y %H:%m:%S.%f')
