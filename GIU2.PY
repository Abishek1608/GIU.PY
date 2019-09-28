import os
import time
print(os.getcwd())

try:
    os.rmdir("audio")
    os.rmdir("video")
    os.rmdir("image")
    #time.sleep(2)
    os.makedirs("audio")
    os.makedirs("video")
    os.makedirs("image")
except:
    os.makedirs("audio")
    os.makedirs("video")
    os.makedirs("image")
path=os.getcwd()
for r,d,f in os.walk(os.getcwd()):
    for file in f:
        if '.mp3' in file:
            cmd="move \""+file+"\" \""+path+"\\audio\""
            os.system(cmd)
        elif '.mp4' in file:
            cmd="move \""+file+"\" \""+path+"\\video\""
            os.system(cmd)
        elif '.png' in file or '.jpeg' in file:
            cmd="move \""+file+"\" \""+path+"\\image\""
            os.system(cmd)
            
        #print(file)
    break
