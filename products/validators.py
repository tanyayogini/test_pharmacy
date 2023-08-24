from django.core.exceptions import ValidationError


def validate_ean13(value):
    """Проверяет корректность введения ean13. Использован алгоритм расчет контрольной суммы"""
    try:
        digit_list = list(map(int, value))
    except ValueError:
        raise ValidationError('Некорректный код ean13')

    last_digit = digit_list.pop()
    summa = 0
    for index, digit in enumerate(digit_list):
        if index % 2 == 0:
            summa += digit
        else:
            summa += digit * 3

    last_digit_contr = (summa // 10) * 10 + 10 - summa
    if last_digit != last_digit_contr:
        raise ValidationError('Некорректный код ean13')

