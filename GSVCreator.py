import zipfile
import os
import errno

def createDirectory(path):
    try:
        os.makedirs(path)
        return True
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
    return False


if __name__ == '__main__':
    path_of_zipFile = raw_input("Enter hosttrace zip file path:")
    target_path = raw_input("Enter target path:")
    target_path += "/processed_files/"
    try:
        print 'Attempting to unzip files for processing ...'
        unzipper(path_of_zipFile, target_path)
    except:
        print 'Failed.'
        
def unzipper(source, target):
    if (createDirectory(target)):
        zip_ref = zipfile.ZipFile(source, "r")
        zip_ref.extractall(target)
        zip_ref.close()

