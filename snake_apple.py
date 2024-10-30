def findMinimumTime(k, position):
    position.sort()
    times_needed =[]

    for i in position:
        time = abs(0 - i)
        times_needed.append(time)
        print(times_needed)

    tt=sum(times_needed[:k])

    return tt




test_k = 3
test_position = [-20, 5, 10]
result = findMinimumTime(test_k, test_position)
print(f"Minimum time required: {result}")