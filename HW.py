result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as ve:
        print(f"ValueError: первое число менше  другого")
    except IndexError as ie:
        print(f"IndexError: второе число більше 100 ")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: ділити на ноль")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Other Error: {e}")

print(result)
