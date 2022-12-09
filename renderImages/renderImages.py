def displayPic():
  file = pickAFile()
  pic = makePicture(file)
  show(pic)
  
def printHeightAndWidth():
  file = pickAFile()
  pic = makePicture(file)
  width = getWidth(pic)
  print "Width of the photo: " + str(width)
  height = getHeight(pic)
  print "Height of the photo: " + str(height)
  print "File Location: " + file
  
def duplicateImage():
  file = pickAFile()
  originalPic = makePicture(file)
  pic2 = duplicatePicture(originalPic)
  show(originalPic)
  show(pic2)
  
def exploreImage():
  file = pickAFile()
  pic = makePicture(file)
  explore(pic)
  openPictureTool(pic)

def savePicture():
  file = pickAFile()
  pic = makePicture(file)
  writePictureTo(pic, r"C:\Users\Sharl\Desktop\beach2.jpg")
  
