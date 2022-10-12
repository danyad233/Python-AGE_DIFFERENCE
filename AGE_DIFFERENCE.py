def get_age_difference(a, b):
    if a>b: 
        return 'Разница года \n' + str(a - b)
    elif b>a:
        return 'Разница года \n' + str(b - a)
    else:
        return 'Разница года \n' + str(b - a)
def main():
    print(get_age_difference(int(input('Первый год рождения ')), int(input('Второй год рождения ' ))))

if __name__ == '__main__':
    while True:
        main()