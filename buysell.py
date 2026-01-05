

prices = [7,6,5,4,3,2,1]
min = prices[0]
diff = 0
for i in range(len(prices)):
    if prices[i] < min:
        min = prices[i]
    elif prices[i] >= min:
        if prices[i] - min >diff:
            diff = prices[i] - min
print(diff)

