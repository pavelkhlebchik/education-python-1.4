number = int(input('Введите пятизначное целое число: '))

units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = number // 10000

result = (tens ** units) * (hundreds * 100) / (ten_thousands - thousands)

print(f'Результат: {result}')
