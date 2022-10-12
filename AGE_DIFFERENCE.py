def get_age_difference(a: int, b: int):
    c = 0
    if a>b:
        c = a - b
    elif b>a:
        c = b - a
    else: # a equal b.
        c = 0

    return c

def main():
    age_diff = get_age_difference(int(input("First year of birth ")), int(input("Second birthday ")))
    print(f'\033[32mYear difference {str(age_diff)}\033[0m')

if __name__ == '__main__':
    while True:
        main()