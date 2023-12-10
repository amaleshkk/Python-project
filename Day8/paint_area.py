import math

def paint_calc(height, width, cover):
    can_no = (height * width) / cover
    round_up_cans = math.ceil(can_no)
    print(f"The number of cans: {round_up_cans}")



test_h = int(input("Enter the height of the room: "))
test_w = int(input("Enter the width of the room: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)