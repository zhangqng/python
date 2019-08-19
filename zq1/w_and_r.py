def write():
    try:
        filename = "./zq.txt"
    except IOError:
        print("file create error")
    else:
        fp = open(filename,'wb')
        fp.write("bbb".encode('utf-8'))
        fp.close()

def read():
    try:
        filename = "./zq.txt"
        fp = open(filename,'r')
    except IOError:
        print("file open error")
    else:
        for i in fp:
            print("file data is " + i)
        fp.close()

if __name__ == '__main__':
    write()
    read()
    print("OK")