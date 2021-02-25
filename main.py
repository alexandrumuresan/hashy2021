from io_utils import read_input, write_output

INPUT_CHAR = 'f'


def main():
    duration, intersection, streets, nr_cars, bonus, DG, car_routes = read_input(INPUT_CHAR + '.txt')

    traffic = []
    for i in range(int(intersection)):
        if DG.in_degree(i) == 1:
            street_name = list(DG.in_edges(i, data=True))[0][2]['label']
            traffic.append({
                'intersection_index': i,
                'nr_streets': 1,
                'street_data': [(street_name, 1)]
            })

    write_output(INPUT_CHAR + '_out.txt', traffic)


if __name__ == "__main__":
    main()
