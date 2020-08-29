import os
outher_path=r'xxxx\pilixiuga'
folderlist=os.listdir(outher_path)
num=input()
for folder in folderlist:
    inner_path=os.path.join(outher_path,folder)
    filelist=os.listdir(inner_path)
    for item in filelist:
        itemp=item[15:]
        itemps=num+itemp
        if item.endswith(itemp):
            scr=os.path.join(os.path.abspath(inner_path),item)
            dst=os.path.join(os.path.abspath(inner_path),itemps)
            try:
                os.rename(scr,dst)
            except:
                continue