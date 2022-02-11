from packege import transfer_to_rgb

print("Write here Your CMYK value: ")
c = float(input("Write here Your C value "))
m = float(input("Write here Your M value: "))
y = float(input("Write here Your Y value: "))
k = float(input("Write here Your K value: "))

rgb = transfer_to_rgb(c, m, y, k)
print(rgb)
