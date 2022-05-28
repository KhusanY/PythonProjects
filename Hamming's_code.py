print()
data = list(input())
if len(data) != 7 or any(True if int(bit) != 0 and int(bit) != 1 else False for bit in data):
    print()
    exit()

dictionary =  {"001": 3, "010": 2, "011": 5, "100": 0, "101": 4, "110": 2, "111": 6}

s1 = str(int(data[0]) ^ int(data[2]) ^ int(data[4]) ^ int(data[6]))
s2 = str(int(data[1]) ^ int(data[2]) ^ int(data[5]) ^ int(data[6]))
s3 = str(int(data[3]) ^ int(data[4]) ^ int(data[5]) ^ int(data[6]))

s = s1 + s2 + s3

if s in dictionary.keys():
    print(f"Ошибка в бите под нормером {dictionary[s]+1}")
    data[dictionary[s]] = "1" if data[dictionary[s]] == "0" else "0"
else:
    print("Ошибка не обнаружено")
print(f"Правильное сообщение: {data[2] + data[4] + data[5] + data[6]}")



