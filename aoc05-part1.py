import hashlib
my_str = "ugkcyxxp"
password = ""
i = 0
while len(password) < 8:
    h = hashlib.md5(('%s%s' % (my_str, str(i))).encode('utf-8')).hexdigest()
    if h[:5] == '00000':
        password += h[5]
    i += 1
print("Password is:", password)