'''
goal:
perform add/aubtract operations on circular array and count number of times it lands on 0

input:
instruction set
circular array

output:
int times it lands on zero

constraints:
values 0-99
'''

def rotate(item, dial_points_at):
    direction = item[0]
    step = int(item[1:])
    times_hit_zero = 0

    if direction == "R":
        for i in range(step):
            dial_points_at += 1
            if dial_points_at % 100 == 0:
                times_hit_zero += 1
                dial_points_at = dial_points_at % 100
    else:
        for i in range(step):
            dial_points_at -= 1
            if dial_points_at == 0:
                times_hit_zero += 1
            if dial_points_at < 0:
                dial_points_at = 99

    return dial_points_at, times_hit_zero

def main():
    dial_points_at = 50
    hit_zero = 0

    with open("input", "r") as file:
        for i in file:
            dial_points_at, times_hit_zero= rotate(i, dial_points_at)
            hit_zero += times_hit_zero

    print(f"hit_zero: {hit_zero}")




if __name__ == "__main__":
    main()
