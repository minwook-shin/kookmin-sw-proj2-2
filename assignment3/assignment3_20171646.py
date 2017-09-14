import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    print(scdb)
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    try:
        while (True):
            inputstr = (input("Score DB > "))
            if inputstr == "": continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'quit':
                break
            elif parse[0] == 'find':
                find_thing_list = []
                count = 0
                for p in scdb:
                    if p['Name'] == parse[1]:
                        find_thing_list += (
                         {'Age': scdb[count]['Age'], 'Name': scdb[count]['Name'], 'Score': scdb[count]['Score']})
                    count += 1
                showScoreDB(find_thing_list, 'Name')
            elif parse[0] == 'inc':
                for i in range(len(scdb)):
                    if scdb[i]['Name'] == parse[1]:
                        scdb[i]['Score'] = str(int(scdb[i]['Score']) + int(parse[2]))
            else:
                print("Invalid command: " + parse[0])
    except:
        print ("error")
        doScoreDB(scdb)





def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
