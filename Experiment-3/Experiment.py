import math
"""""
Kavin Zhu
20167040
“I confirm that this submission is my own work and is consistent with the Queen’s regulations on Academic Integrity” 
"""

# function that uses the Dan Bernstein method for hashing Strings

def djb2_converter(s):                                                                                                                                
    key = 5381
    c = 33
    for x in s:
        key = key*c + ord(x)
    return key

# class for hash table
class HashTable():
    def __init__(self, size):
        self.m = size
        self.T = [None] * self.m
    

    def hash(self, k):    
        # return k after applying modulo m hashing function
        return k % self.m


    def hash2(self, k):    
        # return k after applying the multiplication hashing function
        V = 0.61803398875
        x = V*k 
        return math.floor(self.m*x)


    # function that inserts key into hash table 
    # using linear probing to deal with collisions
    def Linear_Probing_Insert(self, k):
        i = 0
        v = self.hash(k)
        steps = 0

        while (i < self.m):
            # selecting index
            a = (v+i) % self.m
            steps = steps + 1
            # if address is empty
            if (self.T[a] == None) or (self.T[a] == 0):
                self.T[a] = k
                break
            # if k already exists in table
            elif (self.T[a] == k):
                print("Attempt to insert duplicate key")
                break
            # increment step by 1
            else:
                i=i+1 

        # if table is full
        if (i == self.m):
            print("Table full, insert failed")
    
        return steps

    # function that searches for key in hash table 
    def Linear_Probing_Search(self, k):
        i = 0
        v = self.hash(k)
        while (i < self.m):
            a = (v+i) % self.m
            # if address is empty
            if (self.T[a] == None) or (self.T[a] == 0):
                print("Search value not found")
                i=i+1
            # if address contains key
            elif (self.T[a] == k):
                return a 
            else:
                i=i+1

        # if end of table is reached 
        if (i == self.m):
            print("Search value not found")

    # function that inserts key into hash table 
    # using quadratic probing to deal with collisions
    def Quadratic_Probing_Insert(self, k):
        i = 0
        v = self.hash(k)
        c1 = 5
        c2 = 7
        steps = 0
        while (i < self.m):
            a = (int)(v + c1*i + c2*i**2) % self.m
            steps = steps + 1
            # if address is full
            if (self.T[a] == k):
                print("Attempt to insert duplicate key")
                break
            # if address is empty
            elif (self.T[a] == 0) or (self.T[a] == None):
                self.T[a] = k
                break
            # increment step by 1
            else:
                i = i+1

        # if table is full
        if (i == self.m):
            print("Table full, insert failed")

        return steps

    # function that searches for key in hash table 
    def Quadratic_Probing_Search(self, k):
        i = 0
        v = self.hash(k)
        c1 = 5
        c2 = 7
        steps = 0
        while (i < self.m):
            a = (int)(v + c1*i + c2*i**2) % self.m
            steps = steps + 1
            # if address is empty
            if (self.T[a] == 0) or (self.T[a] == None):
                print("Search value not found")
                return -1
            # if address contains key
            elif (self.T[a] == k):
                return a
            # increment step by 1
            else:
                i=i+1

        # if end of table is reached
        if (i == self.m):
            print("Search value not found")

    # function that inserts key into hash table 
    # using double hashing to deal with collisions
    def Double_Hashing_Insert(self, k):
        i = 0
        v = self.hash(k)
        d = self.hash2(k)
        steps = 0
        while (i < self.m):
            a = (v + d*i) % self.m
            steps = steps + 1
            # if address is full
            if (self.T[a] == k):
                print("Attempt to insert duplicate key")
                break
            # if address is empty 
            elif (self.T[a] == 0) or (self.T[a] == None):
                self.T[a] = k
                break
            # increment step by 1
            else:
                i = i + 1

        if (i == self.m) :
            print("Table full, insert failed")
        
        return steps

    # function that searches for key in hash table 
    def Double_Hashing_Search(self, k):
        i = 0
        v = self.hash(k)
        d = self.hash2(k)
        while (i < self.m):
            a = (v + d*i) % self.m
            if (self.T[a] == 0) or (self.T[a] == None):
                print("Search value not found")
                break
            elif (self.T[a] == k):
                return a
            else:
                i = i + 1

        if (i == self.m):
            print("Search value not found")


def main():

    file = open("HOTNCU_project_names.txt", "r")
    movieTitles = []
    keys = []
    for l in file:
        movieTitles.append(l)
    # convert movie names into key value integers
    for t in movieTitles:
        key = djb2_converter(t)
        keys.append(key)

    # run linear Probing
    linear_probing = HashTable(6301)
    LP = 0
    for i in range(len(keys)):
        LP = LP + linear_probing.Linear_Probing_Insert(keys[i])
    print("Average search sequence length for Linear Probing: ", LP/4000)
    print("Table size: ", 6301)

    # run quadratic Probing
    quadratic_probing = HashTable(6131)
    QP = 0
    for i in range(len(keys)):
        QP = QP + quadratic_probing.Quadratic_Probing_Insert(keys[i])
    print("Average search sequence length for Quadratic Probing: ", QP/4000)
    print("Table size: ", 6131)

    # run double Hashing
    double_hashing = HashTable(5167)
    DH = 0
    for i in range(len(keys)):
        DH = DH + double_hashing.Double_Hashing_Insert(keys[i])
    print("Average search sequence length for Double Hashing: ", DH/4000)
    print("Table size: ", 5167)


if __name__ == "__main__":
    main()