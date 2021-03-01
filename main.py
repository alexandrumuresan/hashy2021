import queue

from io_utils import read_input, write_output

INPUT_CHAR = 'f'


def main():
    duration, intersection, streets, nr_cars, bonus, DG, car_routes, street_lengths = read_input(INPUT_CHAR + '.txt')
    duration = int(duration)

    traffic = []

    # street_traffic_lights = []
    # for i in range(duration):
    #     street_traffic_lights.append({})
    #     for start, end in list(DG.edges):
    #         street_name = DG[start][end]['label']
    #         street_traffic_lights[i][street_name] = {
    #             'light_status': False,
    #             'car_queue': queue.Queue()
    #         }
    #
    # for car_index in range(len(car_routes)):
    #     street_traffic_lights[0][car_routes[car_index][0]]['car_queue'].put(car_index)

    for i in range(int(intersection)):
        if DG.in_degree(i) == 1:
            street_name = list(DG.in_edges(i, data=True))[0][2]['label']
            traffic.append({
                'intersection_index': i,
                'nr_streets': 1,
                'street_data': [(street_name, 1)]
            })
        else:
            traffic.append({
                'intersection_index': i,
                'nr_streets': len(list(DG.in_edges(i))),
                'street_data': []
            })
            for edge in range(len(list(DG.in_edges(i)))):
                street_name = list(DG.in_edges(i, data=True))[edge][2]['label']
                traffic[i]['street_data'].append((street_name, 1))

            # for timestep in range(duration):
            #     street_traffic_lights[timestep][street_name]['light_status'] = True

    # print()
    #
    # score = calculate_score(duration, street_traffic_lights, car_routes, bonus, street_lengths)
    # print(score)

    write_output(INPUT_CHAR + '_out.txt', traffic)


def calculate_score(duration, street_traffic_lights, car_routes, bonus, street_lengths):
    score = 0
    for timestep in range(duration):
        for route in street_traffic_lights[timestep]:
            car_index = street_traffic_lights[timestep][route]['car_queue'].get()
            current_street_index = car_routes[car_index].index(route)

            if current_street_index == len(car_routes[car_index]) - 1:
                score += bonus + (duration - timestep)

            elif street_traffic_lights[timestep][route]['light_status']:
                next_street_name = car_routes[car_index][current_street_index + 1]
                street_traffic_lights[timestep + street_lengths[next_street_name]][next_street_name]['car_queue'].put(
                    car_index)

            while not street_traffic_lights[timestep][route]['car_queue'].empty():
                car_index = street_traffic_lights[timestep][route]['car_queue'].get()
                current_street_index = car_routes[car_index].index(route)

                if current_street_index == len(car_routes[car_index]) - 1:
                    score += bonus + (duration - timestep)
                else:
                    street_traffic_lights[timestep + 1][route]['car_queue'].put(car_index)

    return score


if __name__ == "__main__":
    main()
