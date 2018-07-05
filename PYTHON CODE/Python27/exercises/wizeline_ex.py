
"""
Problem statement:
http://www.informatik.uni-ulm.de/acm/Locals/2003/html/histogram.html
"""
def largeRectangule(numbers):
    maxnum = max(numbers)

    largeRect = 0
    for i in range(1,maxnum+1):
        #print i
        count = 0
        for num in (numbers):
            #print "num: " + str(num)
            if(i <= num):
                count += 1
                #print "count ++: %i",count
            else:
                #print "count %i, %i",(count, count*i)
                count = count * i
                if(count > largeRect):
                    largeRect = count
                count=0

        count = count * i
        if (count > largeRect):
            largeRect = count
        #print "- largeRect: %i, count:%i -"%(largeRect,count)

    return largeRect


def test_largeRectangule():
    input = [2,1,5,6,2,3]
    print "Big Count: %i"%largeRectangule(input)

    input = [1,2,2,4,6,2,2]
    print "Big Count: %i" % largeRectangule(input)

    input = [1, 2, 3, 4, 5]
    print "Big Count: %i" % largeRectangule(input)

if __name__ == '__main__':
    print "test1"
    test_largeRectangule()

