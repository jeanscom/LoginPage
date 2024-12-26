# predict output
#a
list1= ["Hello ", "take "] 
list2= ["Dear", "Sir"]
res=[x + y for x in list1 for y in list2]
print(res)

#b
ctr =0
words =['abc','xyz', 'aba', '1221']
for word in words:
	if len(word) > 1 and word [01] == word [2]:
	    ctr += 1
print (ctr)



#The words in the list are checked:

# 'abc': Length is 3, and word[0] is 'a' and word[2] is 'c' (not equal).
# 'xyz': Length is 3, and word[0] is 'x' and word[2] is 'z' (not equal).
# 'aba': Length is 3, and word[0] is 'a' and word[2] is also 'a' (equal).
# '1221': Length is 4, and word[0] is '1' and word[2] is '2' (not equal).
# Only the word 'aba' meets the criteria, so the counter ctr is incremented to 1.

# Thus, the final output is 1, indicating that there is one word in the list that meets the specified conditions.
