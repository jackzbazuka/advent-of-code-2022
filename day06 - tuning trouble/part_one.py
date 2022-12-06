with open("datastream.in", "r") as f:
    raw_data = f.readline()
    data = raw_data.strip()

    marker_idx = -1
    trace = []

    for count, char in enumerate(data):
        if len(trace) >= 4:
            if len(set(trace)) == len(trace):
                marker_idx = count
                break
            else:
                trace = trace[1:]

        trace.append(char)

print(marker_idx)

# Solution -> 1896
