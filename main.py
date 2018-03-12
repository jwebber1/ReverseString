#                                                           ©Jonathan Webber
#This is a simple program that reverses a user-specified string.

#user input for a string
print('Please enter the string you would like to reverse: ')
userStr = input()

#funtion to reverse a string
def revStr(str):
    #temporary string
    tempStr = ''

    #if the user input has nothing in it
    if(len(str)==0):
        return ''

    #loop to put the end of the string into the beginning of tempStr
    for i in range(0, len(str)):
        tempStr += str[-1-i]

    #return the string
    return tempStr

#print out the string
print(revStr(userStr))