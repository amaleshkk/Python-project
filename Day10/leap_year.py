def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year")
                leap = True
            else:
                # print("Not leap year")
                leap = False
        else:
            # print("Leap year")
            leap = True
    else:
        # print("Not leap year")
        leap = False
    return leap


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# print(is_leap(int(input("Enter a year: "))))

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))