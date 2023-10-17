import os

file_name = "ghu"

objz = os.listdir(file_name)

for obj in objz:
    p = os.path.join(file_name, obj)
    if os.path.isfile(p):
        print(f"{obj} - file - {os.path.getsize(p) // 1024} bytes")
    elif os.path.isdir(p):
        print(f"{obj} - dir")

# directory = r'D:\pyth\ghu\DAISAVEAUTOEC774D55.txt'
# directory1 = r'D:\pyth\ghu\DAISAVECHAP3D8795BD.txt'
# directory2 = r'D:\pyth\ghu'
# for root, dirs, filez in os.walk("ghu", False):
#     print("Papka", root)
#     print("Dirs", dirs)
#     print("files", filez[0], os.path.getsize(directory) // 1024, "Байтов")
#     print("files", filez[1], os.path.getsize(directory1) // 1024, "Байтов")
