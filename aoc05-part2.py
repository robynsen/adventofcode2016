import hashlib
my_str = "ugkcyxxp"
password = list("--------")
i = 0
while '-' in password:
    h = hashlib.md5(('%s%s' % (my_str, str(i))).encode('utf-8')).hexdigest()
    if h[:5] == '00000':
        try:
            if int(h[5]) < len(password) and password[int(h[5])] == '-':
                password[int(h[5])] = h[6]
                #print("Updating password with: i ==",i,"h ==",h)
                #print("  > Updated password is:", ''.join(password))
        except:
            #print ('Not a valid password index: h[5] ==', h[5])
            pass
    i += 1
print("Password is:", ''.join(password))
