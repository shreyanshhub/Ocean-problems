def write_file(n):

    file = open('sol48.txt','a')
    for i in range(1,n+1):
        file.write('{0}\n'.format(i))

    file.close()

