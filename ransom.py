def main():
    ransomNote = input("Enter ransom: ")
    magazine = input("Enter magazine: ")
    print(check(ransomNote, magazine))
def check(ransomNote, magazine):
    for i in ransomNote:
        r = ransomNote.count(i)
        m = magazine.count(i)
        if ransomNote.count(i) <= magazine.count(i):
            continue
        else:
            return(False)
    return(True)
main()