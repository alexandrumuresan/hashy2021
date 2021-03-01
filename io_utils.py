import networkx as nx
import matplotlib.pyplot as plt


def read_input(input_file):
    print("reading input")
    file = open(input_file, 'r')

    d, intersection, s, v, f = file.readline().rstrip("\n").rstrip("\r").split(' ')

    DG = nx.DiGraph()

    street_lengths = {}

    for i in range(int(s)):
        # streets
        b, e, name, l = file.readline().rstrip("\n").rstrip("\r").split(' ')
        DG.add_weighted_edges_from([(int(b), int(e), int(l))])
        DG[int(b)][int(e)]['label'] = name
        street_lengths[name] = l

    # nx.draw(DG, with_labels=True, font_weight='bold')
    # plt.show()

    cars = []
    for i in range(int(v)):
        # cars
        streets = file.readline().rstrip("\n").rstrip("\r").split(' ')[1:]
        cars.append(streets)

    file.close()

    return d, intersection, s, v, f, DG, cars, street_lengths


def write_output(output_file, content):
    print("writing output")
    f = open(output_file, "w")

    nr_lights = len(content)

    f.write(str(nr_lights))
    f.write("\n")

    for i in range(nr_lights):
        f.write(str(content[i]['intersection_index']))
        f.write("\n")

        f.write(str(content[i]['nr_streets']))
        f.write("\n")

        nr_street_lights = len(content[i]['street_data'])
        for j in range(nr_street_lights):
            f.write(content[i]['street_data'][j][0] + ' ' + str(content[i]['street_data'][j][1]))
            f.write("\n")

    f.close()
