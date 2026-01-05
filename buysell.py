prices = [3,2,6,5,1,3]
max = prices[0]
min = prices[0]

for i in range(len(prices)):
    if i == len(prices):
        break
    
    if prices[i] > max:
        max = prices[i]
    if prices[i] <= min:
        min = prices[i]
        if  prices.index(max) < prices.index(min):
            max = min
        else:
            continue
if prices.index(max) > prices.index(min):
    print(max - min)
else:
    print(0)

