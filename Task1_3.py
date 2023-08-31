def explode_chains(encoded_lists):
   
    def find_consecutive(lst):
        sequences=[]
        consecutive=[lst[0]]
        for i in range(1,len(lst)):
            if lst[i]==lst[i-1]+1:
                consecutive.append(lst[i])
            else:
                sequences.append(consecutive)
                consecutive=[lst[i]]
        sequences.append(consecutive)
        return sequences

    for i,encode_list in enumerate(encoded_lists):
        sequences=find_consecutive(encode_list)
        new_list=[]
        for seq in sequences:
            if len(seq)>=3:
                new_list.extend(seq[3:])
            else:
                new_list.extend(seq)
        encoded_lists[i]=new_list
    
    return encoded_lists
    
encoded_lists=[[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]
result=explode_chains(encoded_lists)
print(result)