def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
s1="silent"
s2="listen"
if are_anagrams(s1,s2):
    print("are anagrams")
else:
    print("are not anagrams")