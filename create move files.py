import os

def createifnotexists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
print(files)
createifnotexists('Images')
createifnotexists('Docs')
createifnotexists('Media')
createifnotexists('others')
 # os.makedirs('Media') # creates folders
imgext=[".png",'.jpeg','.jpg']
images = [file for file in files if os.path.splittext(file)[1].lower() in imgext]

docext=['.txt','.docx','.doc','.pdf']
docs = [file for file in files if os.path.splittext(file)[1].lower() in docext]
print(docs)

medext=['.mp3','.mp4']
media = [file for file in files if os.path.splittext(file)[1].lower() in medext]
print(media)

others = []
for file in files:
    ext = os.path.splittext(file)[1].lower()
    if (ext not in medext) and (ext not in docext) and (ext not in imgext):
        others.append(file)

    