def is_leap(year):
    # leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year")
                # leap = True
                return True
            else:
                # print("Not leap year")
                # leap = False
                return False
        else:
            # print("Leap year")
            # leap = True
            return True
    else:
        # print("Not leap year")
        # leap = False
        return False
    # return leap


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month -1]


# print(is_leap(int(input("Enter a year: "))))

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year=year, month=month)
print(days)