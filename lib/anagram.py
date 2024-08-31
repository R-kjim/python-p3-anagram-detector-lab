# your code goes here!
class Anagram:
    pass
    def __init__(self,word):
        self.name=word

    def match(self,input_list):
        pass
        match_list=[]
        output_list=[]
        word_list=[n for n in self.name]
        for item in input_list:
            match_list=[d for d in item]
            if sorted(match_list)==sorted(word_list):
                output_list.append(item)
        return output_list

