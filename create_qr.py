import pyqrcode
import sys
import random

database_directory = "database.csv"

if len(sys.argv) == 1:

    with open(database_directory, 'r') as file:
        r = random.randint(100000000000, 999999999999)
        run = True
        while run:
            run = False
            for line in file:
                if int(line.split(',')[0]) == r:
                    r = random.randint(100000000000, 999999999999)
                    run = True
                    break

    with open(database_directory, 'a') as file:
        line = "%s,,,,,,\n" % (r)
        file.write(line)
        print str(r) + " successfully created"

    qr = pyqrcode.create(str(r))
    qr.png("qrcodes/" + str(r) + ".png", scale=6)

    print str(r) + ".png successfully created"

else:
    qr = pyqrcode.create(sys.argv[1])
    qr.png("qrcodes/" + sys.argv[1] + ".png", scale=6)

    print sys.argv[1] + ".png successfully created"
