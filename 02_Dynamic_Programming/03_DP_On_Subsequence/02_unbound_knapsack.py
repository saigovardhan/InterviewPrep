"""
A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items of infinite supply. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal. He can take a single item any number of times he wants and put it in his knapsack.
"""
def unbound(wt, val, c):
    p = val
    dp = [[0 for _ in range(c+1)] for _ in range(len(wt))]
    ind = len(wt)-1
    # sol = memoization(ind, wt, val, c, dp)
    sol = tabulation(ind, wt, p, c, dp)
    print(sol)

def memoization(ind, wt, val, c, dp):

    if c <=0 : return 0

    if ind ==0: 
        if wt[0]<=c:
            return c//wt[0]*val[0]
        return 0
    
    if dp[ind][c] !=0: return dp[ind][c]

    pick =0
    if wt[ind]<=c:
        pick = val[ind]+memoization(ind, wt, val, c-wt[ind], dp)
    not_pick = 0+memoization(ind-1, wt, val, c, dp)

    dp[ind][c] = max(pick, not_pick)
    return dp[ind][c]

def tabulation(ind, wt, p, c , dp):
    for i in range(c):
        if wt[0]<=i:
            dp[0][i] = i//wt[0]*p[0]

    
    for ind in range(1, len(wt)):
        for cap in range(1,c+1):
            
            pick = 0
            if wt[ind]<=cap:
                pick = p[ind]+dp[ind][cap-wt[ind]]

            not_pick = 0 + dp[ind-1][cap]

            dp[ind][cap] = max(pick, not_pick)
        
    print(dp)
    return dp[len(wt)-1][c]



unbound([2, 4, 6], [5, 11, 13], 10)
