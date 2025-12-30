import re
'''
goal: find the sum of all the invalid numbers

input: list of range of ids

output: int sum of all invalid numbers
    invalid number:
        repeating sequence within the range
        must repeat at least twice

constraints: no negative ranges, no leading zeroes
'''
def find_invalid_ids(first, second):
    total = 0

    for item in range(first, second + 1):
        s = str(item)
        n = len(s)

        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue

            pattern = s[:k]
            if pattern * (n // k) == s:
                total += item
                break

    return total

def main():
    sun = 0
    with open("input", "r") as file:
        for f in file:
            array_of_ranges = re.split(",", f)
    for item in array_of_ranges:
        first, second = re.split("-", item)
        sun += find_invalid_ids(int(first), int(second))
    print(sun)

if __name__ == "__main__":
    main()
