# WAP Take String From User and Reverse it
class ReverseString:
    def reversestring(self,string):
        temp=""
        for ch in string:
            temp=ch+temp
        return temp
    
    def inputdata(self):
        input_string=input("Enter Your String to Reverse: ")
        return input_string



obj_data=ReverseString()
input_data=obj_data.inputdata()
result=obj_data.reversestring(input_data)
print(f"Reversed String is: {result}")

