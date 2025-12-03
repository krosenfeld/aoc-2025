from project import paths


def parse(s: str) -> int:
    if s[0] == "R":
        factor = +1
    else:
        factor = -1
    return factor * int(s[1:])


def main():
    print("starting")
    inputs_file = paths.inputs / "day01.txt"
    code_list = []
    with open(inputs_file, "r") as f:
        code_list = f.readlines()

    ans = 0
    location = 50
    for code in code_list:
        location = (location + parse(code)) % 100
        if location == 0:
            ans += 1

    print(f"Answer is: {ans}")


if __name__ == "__main__":
    main()
