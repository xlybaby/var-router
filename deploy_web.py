# -*- coding: utf-8 -*-

import os,sys,re,time

def populateWeb(targetDir):
  header = os.path.join(targetDir,  "header.html") 
  footer = os.path.join(targetDir,  "footer.html") 
  for file in os.listdir(targetDir): 
    theFile = os.path.join(targetDir,  file) 
    if os.path.isfile(theFile) and file != "header.html" and file != "footer.html" : 
      content = open(theFile, "rb").read()
      os.remove(theFile)
      open(theFile, "ab+").write(open(header, "rb").read()) 
      open(theFile, "ab+").write(content)
      open(theFile, "ab+").write(open(footer, "rb").read())

def copyFiles(sourceDir,  targetDir): 
      if sourceDir.find(".svn") > 0: 
          return 
      for file in os.listdir(sourceDir): 
          sourceFile = os.path.join(sourceDir,  file) 
          targetFile = os.path.join(targetDir,  file) 
          if os.path.isfile(sourceFile): 
              if not os.path.exists(targetDir):  
                  os.makedirs(targetDir)  
              if os.path.exists(targetFile):
                os.remove(targetFile)
              #if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
              open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
          if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)
   
if __name__ == '__main__':
  srcDir = "D:/developer/var-workspace/var-view"
  targetDir = "D:/developer/var-workspace/var-static/var"
  
  props={}
  if len(sys.argv) > 1:
    for idx in range(1, len(sys.argv)):
      arg = sys.argv[idx]
      if arg.startswith("--") :
        prop = arg[2:]
        pair = prop.split("=")
        props[pair[0]]=pair[1]
    print ("command props", props)
    
  if "srcDir" in props:
    srcDir = props["srcDir"]
    
  if "targetDir" in props:
    targetDir = props["targetDir"]
    
  copyFiles(srcDir+"/images", targetDir+"/images")
  copyFiles(srcDir+"/js", targetDir+"/js")
  copyFiles(srcDir+"/css", targetDir+"/css")
  copyFiles(srcDir+"/fonts", targetDir+"/fonts")
  copyFiles(srcDir+"/web", targetDir+"/web")
  
  populateWeb(targetDir+"/web")