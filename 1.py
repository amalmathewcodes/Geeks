'''To reverse a string seperated by dots'''

a = str(input('Enter the string with dots:'))
b = list(a)
c = ''
for i in b:
    if i != "." :
        c+=i
    else:
        c+=" "
len = len(c)
result = ''
temp = ''
for i in range(-1,(-len-1),-1):
    if c[i].isalpha():
        temp+=c[i]
        if i==-len:
            temp = temp[::-1]
            result += temp
    elif c[i].isspace():
        temp = temp[::-1]
        result+=temp+'.'
        temp = ''
    else:
        break
print(result)
