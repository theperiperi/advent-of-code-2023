from functools import cache

@cache
def fit(size, record):    
    remainders = []
    for start in range(1, len(record) - size):
        end = start + size
        if record[start - 1] != '#' and record[end] != '#' and \
                all(record[i] != '.' for i in range(start, end)):
            remainders.append('.' + record[end + 1:])
        if record[start] == '#':
            break
    return tuple(remainders)

@cache
def repair(record, sizes):
    if not sizes:
        return int('#' not in record)
    return sum(repair(r, sizes[1:]) for r in fit(sizes[0], record))

def normalize(record):
    return '.' + '.'.join(record.replace('.', ' ').split()) + '.'

def main():
    with open("C:\\Users\\pri\\Desktop\\sample.txt", 'r') as file:
        lines = file.readlines()

    records = [(record, tuple(map(int, numbers.split(',')))) for record, numbers in (line.split() for line in lines)]
    result1 = sum(repair(normalize(r), n) for r, n in records)
    result2 = sum(repair(normalize('?'.join([r] * 5)), n * 5) for r, n in records)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
