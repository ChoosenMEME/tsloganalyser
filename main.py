import os
from datetime import datetime


def readFiles(folder):
    result = []
    files = os.listdir(folder)
    i = 0
    for file in files:
        i= i + 1
        with open(folder + "\\" + file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                result.append(line)
            result.sort()
    return result


def formatData(lines):
    result = []
    for line in lines:
        splitLine = line.split('|')
        for item in splitLine:
            # remove spaces
            item.strip()
        # check if line is a log line
        if splitLine[2] == 'VirtualServerBase':
            # convert date to datetime
            dateValue = str(splitLine[0])
            splitLine[0] = (datetime.strptime(dateValue, '%Y-%m-%d %H:%M:%S.%f'))
            result.append(splitLine)
    return result

def getUsernames(lines):
    result = []
    username = []
    for line in lines:
        message = line[4]
        if message[0:18] == 'client connected \'':
            endpos = message.find('\'', 20)
            idpos = message.find('(id:', endpos)
            idend = message.find(')', idpos)
            username = message[idpos+4:idend], message[18:endpos]
        elif message[0:21] == 'client disconnected \'':
            endpos = message.find('\'', 23)
            idpos = message.find('(id:', endpos)
            idend = message.find(')', idpos)
            username = message[idpos + 4:idend], message[21:endpos]
        if username not in result:
            result.append(username)
    return result

if __name__ == '__main__':
    lines = readFiles('C:\\Users\\Tim\\Desktop\\logs')
    formatLines = formatData(lines)
    usernames = getUsernames(formatLines)
    #print(len(formatLines))
