import numpy as np
btc_close_data=[2,33,45]
close_dataArray=np.array(btc_close_data) #Convert your data into an array
close_sum=np.sum(close_dataArray)
close_average=close_sum/len(close_dataArray)
print(close_average)
