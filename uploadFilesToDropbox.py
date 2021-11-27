import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def uploadFile(self, localPath, dropboxPath):
        dropboxAccess = dropbox.Dropbox(self.accessToken)
        f = open(localPath, "rb")
        try:
            dropboxAccess.files_upload(f.read(), dropboxPath, mode=WriteMode("overwrite"))
        except:
            print(dropboxPath + " failed to upload.")
    
    def uploadFolder(self, localPath, dropboxPath):
        dropboxAccess = dropbox.Dropbox(self.accessToken)
        if (os.path.isdir(localPath)):
            fileList = os.listdir(localPath)
            for fileName in fileList:
                currentPath = localPath + "/" + fileName
                if (os.path.isdir(currentPath)):
                    self.uploadFolder(currentPath, dropboxPath + "/" + fileName)
                else:
                    self.uploadFile(currentPath, dropboxPath + "/" + fileName)
        else:
            print(localPath + " is not a directory.")


def main():
    token = "[your token here]"
    td = TransferData(token)
    td.uploadFolder("[path on computer]", "[path in dropbox]")


main()