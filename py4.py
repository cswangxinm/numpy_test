fr = open('readfile.txt')

for i in range(4):
    z = fr.readline()
    for j in range(5):
        print int(z[j])
