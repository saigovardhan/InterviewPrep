def frog_jump(nums):
    ind = len(nums)-1
    sol = memoization(ind, nums)
    print(sol)

def memoization(ind, nums):
    if ind ==0: return 0

    if ind <0 : return 1e9

    one_jump = memoization(ind-1, nums) + abs(nums[ind]-nums[ind-1])

    two_jump = 1e9
    if ind >1:
        two_jump = memoization(ind-2, nums)+ abs(nums[ind]-nums[ind-2])

    return min(one_jump, two_jump)

frog_jump([10 , 20, 30, 10])