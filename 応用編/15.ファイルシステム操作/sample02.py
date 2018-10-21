import os
import shutil

def show_dir(path):
    print('====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))


tmpdir = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tmp'

os.mkdir(tmpdir)
os.makedirs('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)

os.rmdir('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)

# os.removedir(tmpdir)
shutil.rmtree(tmpdir)
