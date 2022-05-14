import numpy as np
def confidence_interval(array,confidence): #99% Confidence interval
    count=len(array)
    dataArray=np.array(array) #Convert your data into an array
    sum=np.sum(dataArray)
    average=sum/count
    stdev=np.std(dataArray)
    z_value=confidence     #Confidence value in Z_distribution e.g. 95%=1.96
    sqrt_n=np.sqrt(count)
    variation=z_value*(stdev/sqrt_n)
    lower_CI=average-variation
    upper_CI=average+variation
    return lower_CI,upper_CI

print(confidence_interval(btc_close_data,4.417)) #for 99.999% Confidence interval
