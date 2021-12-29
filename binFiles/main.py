"""
Работа с бинарными файлами
"""

"""
Форматы
I - инт
s - символ
"""
import struct
from os.path import getsize
format = '15s'  # Формат
size = struct.calcsize(format)  # Сколько занимает
with open("a.bin", 'wb') as f:  # Запись
    f.write(struct.pack(format, 'pricol'.encode('UTF-8')))
with open('a.bin', 'rb') as f:  # чтение
    print(struct.unpack(format, f.read())[0].decode().replace("\x00", ""))
format = 'I'  # Формат
size = struct.calcsize(format)
with open("a.bin", 'wb') as f:  # Запись
    f.write(struct.pack(format, 345))
    f.write(struct.pack(format, 35))
    f.write(struct.pack(format, 345))
    f.write(struct.pack(format, 345))
    f.write(struct.pack(format, 345))
    f.write(struct.pack(format, 345))
with open('a.bin', 'rb') as f:  # чтение
    num_lines = getsize('a.bin') // size
    for i in range(num_lines):
        print(struct.unpack(format, f.read(size))[0])
