import numpy as np

from project import paths


def parse(a: int) -> bool:
    num_digits = np.floor(np.log10(a)) + 1
    # If odd number of digits, necessarily valid
    if (num_digits % 2) == 1:
        return True
    else:
        first_half = int(a / (10 ** (num_digits // 2)))
        second_half = a - first_half * (10 ** (num_digits // 2))
        if first_half == second_half:
            return False
        else:
            return True


def main():
    file_name = paths.inputs / "day02.txt"
    with open(file_name, "r") as file:
        id_list = file.readlines()[0].split(",")
    print(id_list)
    ans = 0
    for id_range in id_list:
        first_last_id = id_range.split("-")
        for id in range(int(first_last_id[0]), int(first_last_id[1]) + 1):
            if not parse(id):
                ans += id
    print(f"Answer: {ans}")


if __name__ == "__main__":
    main()
