def read_input(input_file):
    print("reading input")
    f = open(input_file, 'r')

    a, b, c = f.readline()

    for line in f:
        print(line)

    f.close()

    return a, b, c


def write_output(output_file, content):
    print("writing output")
    f = open(output_file, "w")

    f.write(content)

    f.close()
