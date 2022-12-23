def isPalindrome(self, x):
        for i in range(0,int(len(str(x))/2)):
            if(str(x)[i] != str(x)[::-1][i]):
                return False
        return True