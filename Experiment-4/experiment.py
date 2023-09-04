import random
"""""
Kavin Zhu
20167040
“I confirm that this submission is my own work and is consistent with the Queen’s regulations on Academic Integrity” 
"""

class MaxHeap():
    def __init__(self, val):
        self.A = [0]
        for i in range(1, 21):
            self.A.append([0,0])
        self.increment_value = val


    # inserting value function
    def insert(self,x):
        if self.A[0] == len(self.A) - 1:
            print("Max-heap is full; cannot insert")
        else:
            self.A[0] += 1
            temp_pos = self.A[0]
            while temp_pos > 1:
                parent = temp_pos // 2
                if self.A[parent][0] >= x[0]:
                    break
                else:
                    self.A[temp_pos] = self.A[parent]
                    temp_pos = parent
            self.A[temp_pos] = x
        return 

    # removing max value function
    def remove_max_priority(self):
        if self.A[0] == 0:
            print("Cannot remove from empty max-heap")
        else:
            max_value = self.A[1]
            mover = self.A[self.A[0]] # the value from the last leaf on the bottom level
            self.A[0] = self.A[0] - 1 # size of the heap goes down by 1
            temp_pos = 1
            left_child = temp_pos * 2
            right_child = left_child + 1
        # now push the value down until it reaches a proper location
        while left_child <= self.A[0]:
            max_child = left_child
            if right_child <= self.A[0] and self.A[right_child][0] > self.A[left_child][0]:
                                max_child = right_child
            if mover[0] >= self.A[max_child][0]:
                break # we have found the proper location
            else:
                # promote the larger child up, and move down one level of the tree
                self.A[temp_pos] = self.A[max_child]
                temp_pos = max_child
                left_child = temp_pos*2
                right_child = left_child + 1
        self.A[temp_pos] = mover # store the moving value in its proper location
        return max_value # return the value that was at the top of the heap

    def incrementPriorities(self):
        for index in range(1,len(self.A)):
            self.A[index][0] = self.A[index][0] + self.increment_value

    def new_item(self, num_items):
        priority_list = [10, 20, 30, 40]
        initial_items = random.choices(priority_list, weights = [0.4, 0.3, 0.2, 0.1], k = num_items)
        for item in initial_items:
            value = [item, item]
            self.insert(value)


def main():
    increment_value = 1.3

    for _ in range(20):
        p_q = MaxHeap(increment_value)
        p_q.new_item(20)
        waitTimes = []
        for _ in range(8000):
            val = p_q.remove_max_priority()
            if val[1] == 40:
                waitTime = (val[0] - 40)/increment_value
                waitTimes.append(waitTime)
            p_q.incrementPriorities()
            p_q.new_item(1)

        sum = 0
        for time in waitTimes:
            sum = sum + time

        averageWaitTime = sum/len(waitTimes)
        print("Average weight times for priority 40 items is: ", averageWaitTime)


if __name__ == "__main__":
    main()

