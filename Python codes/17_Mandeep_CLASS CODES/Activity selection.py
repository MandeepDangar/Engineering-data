def activityselect(s,f):
    #sorting as per ascii order of finish time
    index = [i for i in range(len(s))] 
    index.sort(key = lambda i:f[i]) #sorting of finishing time
    activity = []
    activity += [index[0]]
    f_time = f[index[0]]
    
    for k in range(1,len(index)):
        ind = index[k]  #activity index
        if(s[ind] >= f_time):
            activity += [ind]
            f_time = f[ind]
    return activity
s = [1,3,0,5,8,5]
f = [5,4,6,6,9,7]
activity = activityselect(s,f)
print(activity)