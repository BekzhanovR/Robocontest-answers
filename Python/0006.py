def DateFormating(year: int):
    """Kiritilgen jildi 4 xanali qilip qaytaradi"""
    if year >= 1000:
        result = year
    elif 999 >= year >= 100:
        result = f"0{year}"
    elif 99 >= year >= 10:
        result = f"00{year}"
    elif 10 >= year:
        result = f"000{year}"
    return result

year = int(input())
formatDate = DateFormating(year)
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"12/09/{formatDate}")
else:
    print(f"13/09/{formatDate}")