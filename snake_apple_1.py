def minimumtime(k,position):

    position.sort()
    n=len(position)

    time=[]

    # position_abs=[]
    # for i in position:
    #     p = abs(i)
    #     position_abs.append(p)

#calculate time for each consecutive set of k apples
    def calc_total_time(apple_set):
        current_pos=0
        total_time=0


        for i in apple_set:
            total_time=total_time + abs(i-current_pos) #0+ (-20-0) >> 20 + (-10--20) >>30 +(-10-5)=45
            print("TT",total_time)
            current_pos=i
            #print(total_time)


        
        return total_time
    
    

#get consecutive positions of k apples
    for i in range(n-k+1):         #n is total number of positions =
                                # 5-3+1 if n is 5 and k is 3 in python
                                # addition and substrction has equal precedence in python

        apple_set=position[i:i+k]
        print("apple set ", apple_set)
        #calc_total_time(0,apples_set)
        time.append(calc_total_time(apple_set))
        print("time for each set of consecutive apple intake by snake = " ,time)
    return min(time)      



k = 3
position = [-20, -10, 5, 10, 20]
print("minimum time = ",minimumtime(k,position))