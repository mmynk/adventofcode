from pathlib import Path


def part1(rotations, verbose=False):
    num_zeros = 0
    cur = 50
    for rotation in rotations:
        distance = int(rotation[1:])
        distance = distance % 100
        if rotation[0] == "L":
            cur -= distance
            if cur < 0:
                cur += 100
        elif rotation[0] == "R":
            cur += distance
            if cur >= 100:
                cur -= 100
        if verbose:
            print("DEBUG:", cur)
        if cur == 0:
            num_zeros += 1
    return num_zeros


def part2(rotations, verbose=False):
    num_zeros = 0
    cur = 50
    for rotation in rotations:
        distance = int(rotation[1:])
        full_rotations = distance // 100
        num_zeros += full_rotations
        distance = distance % 100
        if rotation[0] == "L":
            prev = cur
            cur -= distance
            if cur < 0:
                if prev != 0:
                    # need this condition, otherwise we count extra 0s
                    # eg: at 0, move left 5
                    # this should not add zero
                    # but without this check, it will
                    num_zeros += 1
                cur += 100
        elif rotation[0] == "R":
            cur += distance
            if cur > 100:
                cur -= 100
                num_zeros += 1
            if cur == 100:
                cur = 0
        if cur == 0:
            num_zeros += 1
        if verbose:
            print("DEBUG:", cur, num_zeros)
    return num_zeros


def main():
    use_example = False

    verbose = False
    if use_example:
        verbose = True
        rotations = [
            "L568",
            "L230",
            "R748",
            "L5",
            "R960",
            "L155",
            "L501",
            "L199",
            "R14",
            "L6582",
        ]
    else:
        dir_path = Path(__file__).parent / "inputs"
        input_file = "day1.in"
        file_path = dir_path / input_file
        rotations = file_path.read_text().strip().split("\n")

    print(part2(rotations, verbose))


if __name__ == "__main__":
    main()
