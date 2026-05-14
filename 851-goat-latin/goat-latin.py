class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
        new_list = sentence.split()
        for i in range(len(new_list)):
            if new_list[i].startswith(vowels):
                new_list[i] = new_list[i]+"ma"+"a"*(i+1)
            else:
                temp = new_list[i]
                new_list[i] = temp[1:] + temp [0]+"ma"+"a"*(i+1)
        return " ".join(new_list)
                
                
