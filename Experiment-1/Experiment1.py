# Kavin Zhu
# 20167040
# “I confirm that this submission is my own work and is consistent with the Queen’s regulations on Academic Integrity”

def main():
    n_list = [1000, 2000, 4000, 8000, 16000]
    trin_avg = []
    bin_avg = []
    
    # for every n 
    for k in n_list:
        # generate an array 'A' from 0 to n
        A = list(range(0,k))
        # keep track of total comparisons for bin and trin searches
        total_bin = 0
        total_trin = 0
        # for every value in the array 'A', perform a trinary and binary search
        for i in A:
            # store the total amount of comparisons for every value in 'A'
            total_bin += bin_search(A,i) 
            total_trin += trin_search(A,i)
        # for every list generated from 'n', find the average number of comparisons for every value of 'A'
        bin_avg.append(total_bin/len(A))
        trin_avg.append(total_trin/len(A))
        
    print(n_list)
    print(bin_avg)
    print(trin_avg)
        
        
def bin_search(A,target):
	# returns index of target in A, if present
	# returns -1 if target is not present in A
	done = False
	first = 0
	last = len(A)-1
	counter = 0
	while not done:
		if first > last:
			done = True
		else:
			mid = (first+last)//2
			if A[mid] == target:
				counter += 1
				done = True
			elif A[mid] > target:
				counter += 2
				last = mid-1
			else:
				counter += 2
				first = mid+1
	return counter

def trin_search(A,target):
	# returns index of target in A, if present
	# returns -1 if target is not present in A
	done = False
	first = 0
	last = len(A)-1
	counter = 0
	while not done:
		if first > last:	
			done = True
		else:
			one_third = first + (last-first)//3
			if A[one_third] == target:
				counter += 1
				done = True
			elif A[one_third] > target:
				counter += 2
				# search the left-hand third
				last = one_third-1
			else:
				two_thirds = first + 2*(last-first)//3
				if A[two_thirds] == target:
					# start fresh with the counter because it's a new branch
					counter += 3
					done = True
				elif A[two_thirds] > target:
					counter += 4
					# search the middle third
					first = one_third + 1
					last = two_thirds - 1
				else:
					counter += 4
					# search the right-hand third
					first = two_thirds + 1
	return counter

if __name__ == "__main__":
    main()
