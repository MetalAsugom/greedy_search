from best_station import *



def greedy_search_station(stations, needed_states):
    covered_states = set()
    stations_chosen = []
    while covered_states < needed_states:
        best_station = find_best_station(stations, covered_states)
        covered_states |= stations[best_station]
        stations_chosen.append(best_station)
        del stations[best_station]
    return stations_chosen

stations_chosen = greedy_search_station(stations, needed_states)
print(stations_chosen)