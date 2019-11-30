#fist way to solve this problem
def counts(lis):
    i=0
    count=0
    #run the while loop till all switch become on
    while(all(ele == lis[0] for ele in lis)!=True):
        #if switch is off make it on and reverse all next switch
        #and increase the count by 1
        if lis[i] == 0:
            lis=lis[0:i]+list(map(lambda x:int(not(x)),lis[i:]))
            count+=1
        #if switch is already on the move to next switch
        else:
            pass
        i=i+1

    return count
l=list(map(int,input("Enter states 0 or 1 separated by space\n").split()))
print(counts(l))


#second way to solve this problem

def counts(lis): 
	
	count = 0

	for i in range(len(lis)): 
		#if switch is on count%2==0 no need to turn on
		if (lis[i] == 1 and count % 2 == 0): 
			pass
		#if switch is off and is at count%2!=0(i.e
		#pos like 1,3,5 ) no need to press switch
		#it will be aleady on
		elif(lis[i] == 0 and count % 2 != 0): 
			pass
		#switch is on and at pos index 1,3,5.. need to turn on
		#as is cuurently off
		elif (lis[i] == 1 and count % 2 != 0): 
			count +=1
		#switch is off and at pos index like 0,2,4 ...
		#is in off state need to turn on the switch
		elif (lis[i] == 0 and count % 2 == 0): 
			count += 1
	return count 

print( counts(l)) 

