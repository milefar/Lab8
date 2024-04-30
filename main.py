with open("data.csv") as file:
    next(file)
    c_count = 0
    s_count = 0
    q_count = 0

    c_sum = 0
    s_sum = 0
    q_sum = 0
    for line in file:
        data = line.strip().split(',')
        if float(data[10]) == 0:
            continue
        if data[-1] == "C":
            c_count += 1
            c_sum += float(data[10])
        elif data[-1] == "S":
            s_count += 1
            s_sum += float(data[10])
        elif data[-1] == "Q":
            q_count += 1
            q_sum += float(data[10])

    print("Средняя цена билета при посадке из C: ", c_sum / c_count)
    print("Средняя цена билета при посадке из S: ", s_sum / s_count)
    print("Средняя цена билета при посадке из Q: ", q_sum / q_count)