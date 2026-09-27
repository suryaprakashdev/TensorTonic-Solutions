def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here\
    cur_sum=0
    arr=[]
    for i in range(len(series)):
        if i>0 :
            if series[i-1]!=0:
                frac=(series[i]-series[i-1])/series[i-1]
            else : 
                frac=0
            arr.append(frac)
    return arr
            
            
            
        
        
        