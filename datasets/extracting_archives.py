import zipfile
with zipfile.ZipFile(path, 'r') as archive:
    archive.extractall()
