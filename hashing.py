import hashlib
hash=str(input("enter string"))
md5hash=hashlib.md5(hash.encode())
print(md5hash.hexdigest()) 