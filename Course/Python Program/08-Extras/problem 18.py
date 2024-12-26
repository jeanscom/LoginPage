
# Utkarsh, an inventive boy from Telangana, has created an unusual copying machine.
# Here's how it works:
# • If he feeds the machine an original document, he gets back one more original
# document and one copy.
# • If he uses the machine on a copied document, he receives two additional copies.
# Initially, Utkarsh has only one original document. 
# He wants to determine if it's possible to use the machine to obtain exactly 'x' copied documents and 'y' original documents. Importantly, he cannot discard any documents, and he can only apply the machine to a copied document if he currently has at least one copy. Your task is to write a program that takes 'x' and 'y' as inputs and prints "YES" if it's possible to achieve these quantities using the machine, or "NO" if it's not possible.


x = int(input("Enter number of copied documents: "))
y = int(input("Enter number of original documents: "))

while x > 0 or y > 1:
    if y > x:
        # More copied documents than original ones, can't go further.
        print("NO")
        break
    
    if y == 0:
        # If no copies, but still originals, we can't proceed
        print("NO")
        break
    
    if y == 1:
        print("YES")
        break
    
    if x == y and x != 0:
        print("YES")
        break

# If the loop completes without a break, it's not possible
else:
    print("NO")
