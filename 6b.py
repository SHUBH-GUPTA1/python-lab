# import os
# import sys
# import pathlib
# import zipfile

# dirname=input("enter the directory name you want to archieve")

# if not os.path.isdir(dirname):
#     print("directory doesn't exist")
#     sys.exit(0)
    
# curdirectory=pathlib.Path(dirname)    

# num=1
# while True:
#     zipfilename=os.path.basename(curdirectory)+'_'+str(num)+'.zip'
#     if not os.path.exists(zipfilename):
#         break
#     num+=1
# print(f'creating{zipfilename}...')
# with zipfile.ZipFile(zipfilename,'w') as archieve:
#     for filepath in curdirectory.rglob('*'):
#         archieve.write(filepath,arcname=filepath.relative_to(curdirectory))
# if os.path.isfile(zipfilename):
#     print("archive",zipfilename,"created successfully")    
# else:
#     print("error in creating zip file")    
    
    
import os
import sys
import pathlib
import zipfile

dirname=input("enter the directory you want to archieve")    
if not os.path.isdir(dirname):
    print("directory doesn't exist")
    sys.exit(0)
curdirectory=pathlib.Path(dirname)
num=1
while True:
    zipfilename=os.path.basename(curdirectory)+'_'+str(num)+'.zip'
    if not os.path.exists(zipfilename):
        break
    num+=1
print(f'creating{zipfilename}')
with zipfile.ZipFile(zipfilename,'w')as archieve:
    for filepath in curdirectory.rglob("*"):
        archieve.write(filepath,arcname=filepath.relative_to(curdirectory))
    if os.path.isfile(zipfilename):
        print("archieve",zipfilename,"created successfully")
    else:
        print("error in creating zipfile")    
            
            