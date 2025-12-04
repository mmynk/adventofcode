from pathlib import Path
def count_zeros(rotations):
    num_zeros = 0
    cur = 50
    for rotation in rotations:
        distance = int(rotation[1:])
        distance = distance % 100
        if rotation[0] == 'L':
            cur -= distance
            if cur < 0:
                cur += 100
        elif rotation[0] == 'R':
            cur += distance
            if cur >= 100:
                cur -= 100
        print('DEBUG:', cur)
        if cur == 0:
            num_zeros += 1
    return num_zeros

def main():
    is_example = False
    if is_example:
        rotations = ['L68',
        'L30',
        'R48',
        'L5',
        'R60',
        'L55',
        'L1',
        'L99',
        'R14',
        'L82'
        ]
        print(count_zeros(rotations))
        return
    dir_path = Path(__file__).parent / 'inputs'
    input_file = 'day1.in'
    file_path = dir_path / input_file
    rotations = file_path.read_text().strip().split('\n')
    print(count_zeros(rotations))

if __name__ == '__main__':
    main()
