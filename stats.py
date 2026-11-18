def makeInt(letterlist):
    newlist = []
    for word in letterlist:
        newlist.append(float(word))
    return newlist

def mean(thislist):
    summation = 0
    for val in thislist:
        summation += val
    return summation/len(thislist)

def median(listymclistface):
    listymclistface.sort()
    if(len(listymclistface) % 2 == 0):
        median = (listymclistface[len(listymclistface)//2] +listymclistface[len(listymclistface)//2 -1]) / 2
    else:
        median = listymclistface[len(listymclistface)//2]
    return median

def q1(mylist):
    anothaList = []
    theMedian = median(mylist)
    for nums in mylist:
        if(nums < theMedian):
            anothaList.append(nums)
    return median(anothaList)

def q3(mylist):
    anothaList = []
    theMedian = median(mylist)
    for nums in mylist:
        if(nums > theMedian):
            anothaList.append(nums)
    return median(anothaList)

def mode(lastlist):
    highestCount = 0
    modeList = []
    for nums in lastlist:
        if(lastlist.count(nums) > highestCount):
            modeList.clear()
            modeList.append(nums)
            highestCount = lastlist.count(nums)
        elif(lastlist.count(nums) == highestCount and nums not in modeList):
            modeList.append(nums)
            highestCount= lastlist.count(nums)
    return modeList
        
if __name__ == "__main__":
    vals = input("Enter values:")
    vraw = vals.split()
    values = makeInt(vraw)
    print("The mean is %0.1f" % (mean(values)))
    print("The median is %0.1f" % (median(values)))
    print("The first quartile is %0.1f" % (q1(values)))
    print("The second quartile is %0.1f" % (q3(values)))
    print("The mode(s) is/are", mode(values))