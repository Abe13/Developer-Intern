
#Merge sorting algorithm for a list of numbers with O(nlogn) complexity
def mergeing(ml, mr,index):
    result = []
    i ,j = 0, 0
    while i < len(ml) and j < len(mr):
        if index==0:
            mlc=ml[i]
            mrc=mr[j]
        else:
            mlc=ml[i][index]
            mrc=mr[j][index]
            
        if mlc >= mrc:
            result.append(ml[i])
            i += 1
        else:
            result.append(mr[j])
            j += 1
    result += ml[i:]
    result += mr[j:]
    return result
    


	
def sorting(m,index):
    
    if len(m) <= 1:
        return m
    middle = int( len(m) / 2 )
    ml = sorting(m[:middle],index)
    mr = sorting(m[middle:],index)
    return mergeing(ml, mr,index)



if __name__ == "__main__":
    m=[1.4,1.4, 2,2,2,2,2, 5,5,5, 67 ,7, 0,0,8 ,9 ] #number array


#sorting the list
    ms=sorting(m,0) #sorted list
    
#making a list of number of occurrence

    cv=ms[0] #current value
    fc=1 #Frequncy of current value
    freq={} #Frequency dictionary
    
    for i in range(1,len(ms)):
        if ms[i]==cv: # if the number is repeated
            fc+=1 #incresing the counter
        else: #if there is a new number
            
            freq[cv]=fc #aading the Freq. counter to the list
            cv=ms[i]
            fc=1
        freq[cv]=fc
    #print ms           #sorted list
    d=freq.items()      # list of freq's (key, value) pairs, as 2-tuples
    freqS=sorting(d,1) #sorting dictionary
    print "Sorted list based on number of occurrences:\n"
    print  [x for [x, y] in freqS] #printing the result
            
	
