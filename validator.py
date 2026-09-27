def get_mark(prompt, maximum):
    while True:
        try:
            mark = int(input(prompt))

            if 0 <= mark <= maximum:
                return mark

            print("Please enter marks between 0 and", maximum)

        except ValueError:
            print("Please enter a valid number.")