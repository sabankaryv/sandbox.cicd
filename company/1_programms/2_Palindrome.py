#WAP to check the string is palindrome or not
class PalindromeString:
    def input_data(self):
        input_string=input("Enter Your String to check Palindrome or not: ")
        return input_string

    def palindromecheck(self,string):
        temp=""
        for ch in string:
            temp=ch+temp
        if string==temp:
            return "Entered String is Palindrome"
        else:
            return "Entered String is Not Palindrome"

#main programm
obj_data=PalindromeString()
data=obj_data.input_data()
result=obj_data.palindromecheck(data)
print(result)