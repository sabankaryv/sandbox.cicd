# WAP Count the Vowels and Consonent

class VowelsAndConsonent:
    def inputData(self):
        input_string=input("Enter Your String: ")
        return input_string
    
    def countvowelsconsonent(self,string):
        vowels_count=0
        consonent_count=0
        for ch in string:
            if ch in "aeiou":
                vowels_count+=1
            elif ch.isalpha():
                consonent_count += 1
        return vowels_count,consonent_count
    



# main programm
obj_data=VowelsAndConsonent()
input_data=obj_data.inputData()
vowels_count,consonent_count=obj_data.countvowelsconsonent(input_data)
print(f"The Vowels count is:{vowels_count} And Consonent Count is {consonent_count}")
