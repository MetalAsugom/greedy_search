needed_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

covered_states = set()

def find_best_station(stations, covered_states):
    best_station = ""
    covered = 0

    for station, state_in_stations in stations.items():
        
        new_state = state_in_stations - covered_states
        if len(new_state) > covered:
            best_station = station
            covered = len(new_state)
    return best_station

        
        
        
        
