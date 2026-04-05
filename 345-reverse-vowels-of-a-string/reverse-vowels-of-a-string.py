class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        dict = {}
        for index, letter in enumerate(s):
            if letter in vowels:
                dict[index] = letter
        keys = sorted(dict.keys())
        values = [dict[k] for k in keys]
        for key, value in zip(keys, reversed(values)):
            dict[key] = value
        text_str = list(s)

        # 2. Iterate and replace
        for index, char in dict.items():
            if 0 <= index < len(text_str):
                text_str[index] = char

        # 3. Join back to string
        new_text = "".join(text_str)   
        return(new_text)