import os

def createifnotexists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
print(files)
createifnotexists('Images')
createifnotexists('Docs')
createifnotexists('Media')
 # os.makedirs('Media') # creates folders
imgext=[".png",'.jpeg','.jpg']
images = [file for file in files if os.path.splittext(file)[1].lower() in imgext]

docext=['.txt','.docx','.doc','.pdf']
docs = [file for file in files if os.path.splittext(file)[1].lower() in docext]
print(docs)
