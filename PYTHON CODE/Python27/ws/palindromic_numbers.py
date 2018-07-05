
#------------------------------------------ ALGORITHM CODE -------------------------------------            
class palindrom:

    def __init__(self):
        self.dic_num = dict()
        
    def smallBase(self, number):
        """
        This method return the smallest base which return a palindrom number.
        input:
            number -> number in which you want to know the smallest base.
        """
        for i in range(2,number):
            numbase = num10ToBase(number, i)
            #print "num:" + str(numbase) + ", i:" + str(i)
            if isPalidrome(numbase):
                return i
        
        return number+1
        
    def smallBaseNumList(self, until = 1001):
        """
        This method will calculate the list of number with its smallest base.
        input:
            until -> until which num you want the list.
        """
        self.dic_num[0] = 2
        self.dic_num[1] = 2
        self.dic_num[2] = 3
        
        for i in range(3, until+1):
            self.dic_num[i] = self.smallBase(i)
        
    def printResult(self):
        """
        This method return the list of smallest base according to its number.
        """
        for i in sorted(self.dic_num):
            #print "Num:" + str(i) + ", Base:" + str(self.dic_num[i])
            print  str(i) + ":" + str(self.dic_num[i]) + ","
            

def isPalidrome( num):
    """
    This function return true if the number is palindrom, false in case of not be palindrome.
    input: 
        num -> number
    output: 
        boolean -> True or False
    """
    if type(num) is not str:
        num = str(num)
    
    len_num = len(num)
    if( len_num == 0):
        return False
    elif(len_num == 1):
        return True
        
    for i in range(0, len_num/2 ):
        if(num[i] != num[len_num-i-1]):
            return False
    
    return True
    
def num10ToBase(num, base=2):
    """
    This function make the conversion from a number base 10 to other base.
    input:
        num  ->  number in base 10
        base ->  base to convert
    output:
        String number which result from the conversion.
    """
    numbase = ''
    res = 0
    numdiv = 0
    
    while(True):
        
        res = num % base
        numdiv = num / base
        
        if(numdiv < base):
            numbase = str(numdiv) + str(res) + numbase
            break
            
        num = numdiv
        numbase =  str(res) + numbase
        
    return numbase    

#------------------------------------------  UNIT TESTS ------------------------------------------    
    
def num10ToBaseTest():
    assert num10ToBase(20,3) == '202'
    assert num10ToBase(20,2) == '10100'
    assert num10ToBase(20,3) == '202'
    assert num10ToBase(20,5) == '40'
    
def isPalidromeTest():
    assert isPalidrome('1234554321') == True
    assert isPalidrome('123455432') == False
    assert isPalidrome('14541') == True
    assert isPalidrome('32452') == False
    assert isPalidrome('11') == True
    assert isPalidrome('1') == True
    
def unitTestPalindrom(dic_test):
    pal = palindrom()
    
    assert pal.smallBase(10) == 3
    assert pal.smallBase(18) == 5
    assert pal.smallBase(19) == 18
    assert pal.smallBase(4) == 3
    
    pal.smallBaseNumList(19)
    
    for i in sorted(pal.dic_num):
        assert pal.dic_num[i] == dic_test[i]
            

#---------------------------------------- MAIN AND TEST CASES -------------------------------
def main(n=1000):
    """
    If you run this method, you will get the printed list of non negative number and small palindrome base.
    """
    pal = palindrom()
    pal.smallBaseNumList(n)
    pal.printResult()
    test_cases()
    
def test_cases():
    """
    This function provide the unit test.
    """
    dic_test = {
    0:2,
    1:2,
    2:3,
    3:2,
    4:3,
    5:2,
    6:5,
    7:2,
    8:3,
    9:2,
    10:3,
    11:10,
    12:5,
    13:3,
    14:6,
    15:2,
    16:3,
    17:2,
    18:5,
    19:18,
    20:3
    }
    
    num10ToBaseTest()
    isPalidromeTest()
    unitTestPalindrom(dic_test)

    pal = palindrom()
    pal.smallBaseNumList(19)
    
    for i in sorted(pal.dic_num):
        if pal.dic_num[i] == dic_test[i] :
            print "Test Case: " + str(i) + ", PASS!"
        else:
            print "Test Case: " + str(i) + ", FAIL!"
 

if __name__ == "__main__":
    main()