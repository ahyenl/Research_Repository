#ex.1-6 Time converter

 #This line prompts the user to enter a number of seconds.
sec = input("Enter the number of seconds: ")

 #input converted into integer
sec = int(sec)

 #It calculates the number of days (dd) by performing integer division (//) on the input value (sec) divided by the total number of seconds in a day, which is (24 * 60 * 60)
dd = sec // (24 * 60 * 60)

 #It calculates the number of seconds left after calculating the days. It uses the modulo operator (%) to find the remainder when the input value (sec) is divided by the total number of seconds in a day.
sec_left = sec % (24 * 60*60)

 #It calculates the number of hours (hh) by performing integer division on the remaining seconds (sec_left) divided by the total number of seconds in an hour, which is (60 * 60).
hh = sec_left // (60 * 60)

 #it calculates the number of seconds left after calculating the hours, using the modulo operator to find the remainder when the remaining seconds (sec_left) are divided by the total number of seconds in an hour.
sec_left = sec_left % (60*60) 

 #It calculates the number of minutes (mm) by performing integer division on the remaining seconds (sec_left) divided by the total number of seconds in a minute, which is 60.
mm = sec_left // 60

 #It calculates the number of seconds left after calculating the minutes, using the modulo operator to find the remainder when the remaining seconds (sec_left) are divided by 60.
sec_left = sec_left % 60

 #this line prints the converted time in the format "days : hours : minutes : seconds". It uses f-strings to format the output with the values of dd, hh, mm, and sec_left.
print(f"{dd} : {hh} : {mm} : {sec_left}")

# print(dd)
# print(hh)
# print(mm)
# print(sec_left)
