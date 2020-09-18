#   { 1, -2, 6, 4, -3, 2, -4, -3 }
#   The longest alternating sub array is { 4, -3, 2, -4 }
#   Note that answer might not be unique

def findLongestSubList(A):
    countStart = 0
    curLen = 0
    maxLen = 1

    for i in range(1, len(A)):
        decide = A[i-1] * A[i]

        if decide > 0:
            countStart = i
            curLen = 1

        elif decide < 0:
            curLen = curLen + 1
            if curLen > maxLen:
                maxLen = curLen

        print("\nCount Start {} \n".format(countStart))
        print("Count Max {}\n".format(maxLen))


if __name__ == '__main__':
    A = [1, -2, 6, 4, -3, 2, -4, -3]
    findLongestSubList(A)
