import re
'''
goal: find the sum of all the invalid numbers

input: list of range of ids

output: int sum of all invalid numbers
    invalid number:
        repeating sequence within the range
        must be even

constraints: no negative ranges
'''
def find_invalid_ids(first, second):
    sum_of_invalids = 0
    for i in range(first, second + 1):
        stringify = str(i)
        if len(stringify) % 2 != 0:
            continue
        elif len(stringify) == 2:
            if stringify[0] == stringify[1]:
                sum_of_invalids += i
        else:
            if stringify[:int(len(stringify)/2)] == stringify[int(len(stringify)/2):]:
                sum_of_invalids += i
            else:
                continue

    return sum_of_invalids


def main():
    sun = 0
    with open("input", "r") as file:
        for f in file:
            array_of_ranges = re.split(",", f)
    for range in array_of_ranges:
        first, second = re.split("-", range)
        sun += find_invalid_ids(int(first), int(second))
    print(sun)

if __name__ == "__main__":
    main()
