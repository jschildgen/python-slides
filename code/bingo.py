# 9 unique random numbers from 1 to 31 in list

import random

def to_bool(nums):
    SOLUTION = [4, 17, 2, 21, 15]
    bools = []
    # for each num
    for num in nums:
        # check if num is in SOLUTION
        if num in SOLUTION:
            bools.append(True)
        else:
            bools.append(False)
    return bools

def num_matches(nums):
    bools = to_bool(nums)
    count = 0
    for bool in bools:
        if bool:
            count += 1
    return count

def has_bingo(nums):
    bools = to_bool(nums)
    if bools[0] and bools[1] and bools[2]:
        return True
    if bools[3] and bools[4] and bools[5]:
        return True
    if bools[6] and bools[7] and bools[8]:
        return True
    if bools[0] and bools[3] and bools[6]:
        return True
    if bools[1] and bools[4] and bools[7]:
        return True
    if bools[2] and bools[5] and bools[8]:
        return True
    if bools[0] and bools[4] and bools[8]:
        return True
    if bools[2] and bools[4] and bools[6]:
        return True
    return False   
    

def main():
    nums = []
    while len(nums) < 9:
        num = random.randint(1, 31)
        if num not in nums:
            nums.append(num)
    #if num_matches(nums) < 2: return
    if has_bingo(nums): return
    print(str(nums) + " " + str(has_bingo(nums)) + " " + str(num_matches(nums)))

if __name__ == "__main__":
    for i in range(1000):
      main()
