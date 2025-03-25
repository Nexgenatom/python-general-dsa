
stockprice=[7,6,4,3,1]
def maxProfit(stockprice):
    profit=0
    num = stockprice[0]
    dic ={}
    for i in stockprice:
        if i> num :
             num =i
        profit = max(profit,num-i)
    #    if stockprice[i]<min: 
    #       min = stockprice[i]
    #       print(min)
    #    if stockprice[i]>max: 
    #       max = stockprice[i]
    #       print(max)
    return profit
      #for j in range(i+1,days):
           
        #  if stockprice[i]>stockprice[j] and  i<j and (stockprice[i]-stockprice[j]) > max:            
        #     max = stockprice[i]-stockprice[j]
        #     dic = {max:(i,j)}
        #  elif stockprice[i]<stockprice[j] and i<j and stockprice[j]-stockprice[i] >max:            
        #     max = stockprice[j]-stockprice[i]
        #     dic = {max:(i,j)}
        #  else:
        #      continue
    return max

print(maxProfit(stockprice))