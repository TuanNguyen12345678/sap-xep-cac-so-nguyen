# Sắp xếp các số nguyên
def sosanh(so1,so2,so3):
    tam=0
    if so2<so1 and so2<so3:
        tam=so1
        so1=so2
        so2=tam
    elif so3<so1 and so3<so2:
        tam=so1
        so1=so3
        so3=tam
    if so3<so2:
        tam=so2
        so2=so3
        so3=tam
    return (so1,so2,so3)
x=int(input("nhập số 1: "))
y=int(input("Nhập số 2: "))
z=int(input("Nhập số 3: "))
a,b,c=sosanh(x,y,z)
print("Chuỗi số ban đầu nhập vào: ", x, y, z)
print("Sau khi sắp xếp tăng dần: ", a, b, c)