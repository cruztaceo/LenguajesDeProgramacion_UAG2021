def compute_overtime(hours, rate):
    extra = hours - 40
    if extra < 0:
        extra = 0
    total = hours - extra
    overtime = extra * 1.5 * rate

    return (total * rate) + overtime


input_hrs = float(input('Enter hours: '))
input_rate = float(input('Enter rate: '))

print(compute_overtime(input_hrs, input_rate))
