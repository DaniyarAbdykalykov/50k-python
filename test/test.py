lst = []
string = input()
while string != '777':
    lst.append(string)
    string = input()
print(*lst, sep='***')