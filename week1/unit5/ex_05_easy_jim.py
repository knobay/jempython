# E01
#
import sys
print("\n--------------------------------------------------------------")
print("\n------------------------     E02     -------------------------\n")
str1 = "     London"
str2 = "is the XXXXX"
str3 = "capital"
str4 = "of the"
str5 = "United Kingdom"
#
concat1 = str1.strip()+" ("+str5+")"
print(str1.strip())
print(str1.strip().upper()+str1.strip().upper()+str1.strip().upper()+str3+str3)
print("'"+str1.strip()+(10-len(str1.strip()))*" "+"'")
print(str5.replace("i","a"))
print(str1.strip().lower(),"("+str5.lower()+")")
print(concat1.lower())
print(str1.strip(),str2.replace("X","")+str3,str4,str5)
print(str5[0].upper()+str5[1].lower()+str5[2].upper()+str5[3].lower()+str5[4].upper()+str5[5].lower()+str5[6].upper()+str5[7].lower()+str5[8].upper()+str5[9].lower()+str5[10].upper()+str5[11].lower()+str5[12].upper()+str5[13].lower())
for x in range(0, 13, 2):
    sys.stdout.write(str5[x]) 
print ("\n")
print("\n--------------------------------------------------------------")
print("\n------------------------     E03     -------------------------\n")
nstr = input("\nPlease enter a sensible sentence: ")
print("\nYou entered:-'{}'\n It is {} characters long and it has {} a's in it, {} e's in it, {} i's in it, {} o's in it and {} u's in it!\n".format(nstr,len(nstr),nstr.count("a"),nstr.count("e"),nstr.count("i"),nstr.count("o"),nstr.count("u")))
