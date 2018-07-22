file='alice.txt'
try:
    with open(file) as f_obj:
        contents=f_obj.read()
    print(contents)
except:
    msg ="Sorry, the file"+file+"don't exit"
    print(msg)