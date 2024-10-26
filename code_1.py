def custom_string_order(order,arr):
    
    char_rank_from_order_input={}

    for position, char in  enumerate(order):
        char_rank_from_order_input[char]=position
    #print(char_rank_from_order_input)

    
    def get_word_rank(word):
        word_rank_from_arr=[]
        
        for char in word:
            rank_as_per_order = char_rank_from_order_input[char]
            word_rank_from_arr.append(rank_as_per_order)
            #print(word_rank_from_arr)
        return word_rank_from_arr
    
    return sorted(arr, key=get_word_rank)

if __name__ == "__main__":
    order = "7BbAz"
    arr = ["Abb", "A7z", "z7AAAA", "BbbABB"]
    print(custom_string_order(order,arr))
   
