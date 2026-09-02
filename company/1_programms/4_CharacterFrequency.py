class CharacterFrequency:
    def inputdata(self):
        input_string=input("Enter Your String: ")
        return input_string

    def countfrequency(self,string_data):
        freq_dict={}
        for ch in string_data:
            if ch in freq_dict:
                freq_dict[ch]+=1
            else:
                freq_dict[ch]=1
        return freq_dict


# main programm
obj_data=CharacterFrequency()
input_data=obj_data.inputdata()
result=obj_data.countfrequency(input_data)
print(result)