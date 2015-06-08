# Copy files from one folder to another IFF the files
# have been created or updated within the past 24 hours
import os
import shutil
import time

global output

def main():
    copyUpdatedFiles()

def copyUpdatedFiles(homePath, destPath, lastupdate):
    output = ''
    for filename in os.listdir(homePath):
        modTime = os.path.getmtime(homePath + '\\' + filename)
        #debug print filename
        #debug print 'lastupdate: ', lastupdate
        #debug print 'modTime: ', modTime
        cTime = os.path.getctime(homePath + '\\' + filename)
        #debug print 'cTime: ' , cTime

        if (lastupdate <  modTime) or (lastupdate < cTime):
            shutil.copy(homePath + '\\' + filename, destPath) #actually move file
            #print (filename, ' copied to ', destPath)
            output += str(filename) + ' copied to ' + destPath + '\n' #load up a string for MessageBox summary
    return output # return loaded up string to be inserted in MessageBox



if __name__ == "__main__": main()
