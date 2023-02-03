# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

with open(r'encoded.txt', 'r') as data:
    text = data.read().split()
print(text)
def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: 
        return '' 
    for char in data:
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else:
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return(encoding)

encoded_val = rle_encode('aaaaabbbcccc') 
print(encoded_val)
with open("decoded.txt", "w") as o:
    o.write(encoded_val)

with open(r'decoded.txt', 'r') as data:
    text = data.read().split()
print(text)
def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count) 
            count = '' 
        return decode
decoded_val = rle_decode('5a3b4c') 
print(decoded_val)
# with open("encoded.txt", "a") as o:
#     o.write(decoded_val)
