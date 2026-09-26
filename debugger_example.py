
'''
В нас є список [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
потрібно написати функцію, 
яка буде проходити по цьому списку 
та вводити лише непарні числа з цього списку.
'''
def is_odd(number: int) -> bool: # типізація агументу і результату функції
    ''' 
    A function that checks if a number is odd.'''
    if number % 2 == 1:
        return True
    else:
        return False


def print_odd_numbers(number_list: list[int]):
    '''
    A function that takes a list of numbers 
    and prints only the odd numbers from that list.
    '''
    for number in number_list: # Проходимо по списку
        if number % 2 != 0: # Перевіряємо, чи число непарне
            print(number) # Виводимо непарне число

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Наш список чисел
print_odd_numbers(number_list) # Викликаємо функцію з нашим списком

# Ctrl / - Швидке коментування рядків коду
# Ctrl L - to clear the terminal

print(4 % 2) # Перевірка, чи число 3 непарне (повинно вивести 1)

print(is_odd(4)) # Викликаємо функцію is_odd з числом 3 (повинно вивести True)

print(3 % 2 != 0) 

# Спрощений варіант функції is_odd
def is_odd(number: int) -> bool:
    '''
    A function that checks if a number is even.
    '''
    return number % 2 != 0
 
print(is_odd(4)) # Викликаємо функцію is_odd з числом 3 (повинно вивести True)

print_odd_numbers({1, 2, 3, 4, 5}) # Викликаємо функцію з нашим списком