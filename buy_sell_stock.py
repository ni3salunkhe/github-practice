def buy_sell_stock(prices:list[int])->int:
    l,r=0,1 # l->buy, r->sell
    maxP=0
    while r<len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l]
            maxP=max(maxP, profit)
        else:
            l=r
        r+=1
    return maxP
print(buy_sell_stock([7,1,5,3,6,4])) # 5