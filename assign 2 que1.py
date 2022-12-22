stra= 'Python is a case sensitive language'
length=len(stra)
print("length is=",length)

strb=stra[::-1]
print(strb)

strc=slice(10,35)
print(stra[strc])

strd=stra.replace("a case sensitive language","object oriented")
print(strd)

print(stra.index('a'))

stra=stra.replace(" ","")
print(stra)