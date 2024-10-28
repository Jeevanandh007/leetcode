def findMinimumTime(k, position):
    position.sort()
    #min_time=0
    times_needed =[]

    for i in position:
        time = abs(0 - i)
        times_needed.append(time)

    times_needed[:k]




    return




test_k = 3
test_position = [-20, 5, 10]
result = findMinimumTime(test_k, test_position)
print(f"Minimum time required: {result}")