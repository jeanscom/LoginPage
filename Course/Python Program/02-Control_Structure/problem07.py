#Write python program to print the below patterns. Take as input no: of rows     		
"""
a

        		* 
              * * 
            * * * 
          * * * * 
        * * * * * 
      * * * * * * 
    * * * * * * * 
  * * * * * * * * 
* * * * * * * * * 
"""

# number of rows
rows = 9
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")

"""
b
* * * * * * * * * 
  * * * * * * * * 
    * * * * * * * 
      * * * * * * 
        * * * * * 
          * * * * 
            * * * 
              * * 
                * 
"""
rows = 9
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
"""
c

                * * * * * * * * * * 
                 * * * * * * * * * 
                  * * * * * * * * 
                   * * * * * * * 
                    * * * * * * 
                     * * * * * 
                      * * * * 
                       * * * 
                        * * 
                         * 
"""
rows = 9
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
"""
d
*               * 
* *           * * 
* * *       * * * 
* * * *   * * * * 
* * * * * * * * *
"""
rows = 5  # Number of rows for the pyramids

for i in range(1, rows + 1):
    # Print left pyramid
    print("* " * i, end="")  # Print stars for the left pyramid
    
    # Print spaces in the middle
    print(" " * (2 * (rows - i) - 1), end="")  # Print spaces for separation
    
    # Print right pyramid
    if i != rows:  # Avoid printing stars for the last row
        print("* " * i)  # Print stars for the right pyramid
    else:
        print("* " * i)  # Print stars for the last row

"""
e

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
