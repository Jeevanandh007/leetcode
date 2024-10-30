def minimumtime(k,position):
    #position.abs()
    position.sort()
    print(position)

    time=[]

    for i in position:
        time.append(abs(i))
        print(time)

        #total_time=sum( )

    return total_time

k = 5
position = [-20, 5, 10,-5, 20]
minimumtime(k,position)
