Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
---------------------------------------------


def sum_num(n=int(input('Ввести элементы: ')), el=1.0, sum_n=0.0, count_n=0):
    if n <= 0:
        return f'Количество элементов - {count_n}, их сумма - {sum_n}'
    return sum_num(n-1, el/-2, sum_n+el, count_n+1)


print(sum_num())