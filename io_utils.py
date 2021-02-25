def read_input(input_file):
    print("reading input")
    file = open(input_file, 'r')

    d, i, s, v, f = file.readline().rstrip("\n").rstrip("\r").split(' ')

    for i in range(int(s)):
        b, e, name, l = file.readline().rstrip("\n").rstrip("\r").split(' ')

    for i in range(int(v)):
        car_data = file.readline().rstrip("\n").rstrip("\r").split(' ')
        p = car_data[0]
        streets = car_data[1:]
        print(streets)

    file.close()

    return d, i, s, v, f


def write_output(output_file, content):
    print("writing output")
    f = open(output_file, "w")

    f.write(content)

    f.close()
