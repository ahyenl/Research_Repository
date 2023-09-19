#ex.3-2 Star pyramid
#double FOR loop

#The goal is to create an increasing triangle pattern with asterisks.
#The outer for loop (for i in range(10)) iterates from 0 to 9. It determines the number of rows in the pattern.
#Inside the outer loop, there's an inner for loop (for j in range(i+1)) that iterates from 0 to i. It determines the number of asterisks to be printed in each row.
#res_string is initialized as an empty string for each row.
#Inside the inner loop, an asterisk is added to the res_string for each iteration.
#After the inner loop completes for each row, res_string contains the appropriate number of asterisks for that row.
#The print(res_string) statement prints the res_string, which represents a row of asterisks. As i increases, more asterisks are added to each row, creating an increasing triangle pattern.


for i in range(10):
    res_string = ""
    for j in range(i+1):
        res_string += "* "
    print(res_string);

# (2)
for i in range(10, 0, -1):
    res_string = ""
    for j in range(i):
        res_string += "* "
    print(res_string);

