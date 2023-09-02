"""
rod cutting problem 
5
2 5 7 8 10

"""
def rod_cutting(n, profit):
    ind = n-1
    weight = [i+1 for i in range(n)]
    sol = memoization(ind,n, weight, profit)
    print(sol)

def memoization(ind, cap, weight, profit):
    if ind < 0:
        return 0

    if ind ==0:
        return profit[ind]* cap
    

    take = 0
    if weight[ind] >=cap:
        take = profit[ind]+ memoization(ind-1, cap-weight[ind], weight, profit)
    not_take = 0 + memoization(ind-1, cap, weight, profit)

    return max(take, not_take)

rod_cutting(5, [2, 5, 7, 8, 10])
