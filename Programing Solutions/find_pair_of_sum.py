'''

Given an unsorted array of integers, find a pair with a given sum in it

Example, arr=[8,7,2,5,3,1] & sum=10
Found pair at index 0 and 2 (8+2)
Found pair at index 1 and 4 (7+3)

'''


arr = [1,1,1,1,1,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
sum = 10
flag = False
dict ={}

for i,e in enumerate(arr):
    if (sum - e) in dict:
        print("Found pair at index {} and {} ".format(dict.get(sum-e),i))
        flag = True
    dict[e]=i

if not flag:
    print("No pair found")
