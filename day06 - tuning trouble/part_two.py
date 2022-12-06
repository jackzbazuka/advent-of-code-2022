with open("datastream.in", "r") as f:
    raw_data = f.readline()
    data = raw_data.strip()

    print(data)

    message_marker_idx = -1
    trace = []

    for count, char in enumerate(data):
        if len(trace) >= 14:
            if len(set(trace)) == len(trace):
                message_marker_idx = count
                break
            else:
                trace = trace[1:]

        trace.append(char)


print(message_marker_idx)

# Solution -> 3452
