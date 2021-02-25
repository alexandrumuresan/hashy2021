import networkx as nx
import matplotlib.pyplot as plt


def read_input(input_file):
    print("reading input")
    file = open(input_file, 'r')

    d, i, s, v, f = file.readline().rstrip("\n").rstrip("\r").split(' ')

    DG = nx.DiGraph()

    for i in range(int(s)):
        # streets
        b, e, name, l = file.readline().rstrip("\n").rstrip("\r").split(' ')
        DG.add_weighted_edges_from([(int(b), int(e), int(l))])
        DG[int(b)][int(e)]['label'] = name

    nx.draw(DG, with_labels=True, font_weight='bold')
    plt.show()

    cars = []
    for i in range(int(v)):
        # cars
        streets = file.readline().rstrip("\n").rstrip("\r").split(' ')[1:]
        cars.append(streets)

    file.close()

    return d, i, s, v, f, DG, cars


def write_output(output_file, content):
    print("writing output")
    f = open(output_file, "w")

    f.write(content)

    f.close()
