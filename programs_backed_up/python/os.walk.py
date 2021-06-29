import os
current_path = os.getcwd()
print(os.getcwd())
new_path = '/home/normal/Documents'
'''for root, dirs, files in os.walk('.'): #'.' represents current directory 
    print(root)
    print(dirs)
    print(files)
    print('-------')'''

'''for root, dirs, files in os.walk('.'):
    for dirname in dirs:
        for file in files:
            print(os.path.join(dirname, file))'''

'''for root, dirs, files in os.walk('.'):
    for dirname in dirs:
        for file in files:
            print(os.path.join(root, dirname, file))'''

'''#gives us the full os path and hence full tree structure, best solution so far
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    for dirname in dirs:
       for file in files:
          print(os.path.join(root, dirname, file))'''

'''name = 'mldid.tex'
for root, dirs, files in os.walk('.'):
    if name in files:
        print(os.path.join(root,dir,name))
    else:
        print('404') #outputs 404 many times'''


'''name = '1406.db'
for root, dirs, files in os.walk('.'):
    for dirname in dirs:
        if name in files:
            print(os.path.join(root, dirname, name))            
        else:
            print('404')'''

#alternative to os.walk 
DATADIR = '/home/normal'
CATEGORIES = ['Documents', 'Dropbox', 'Pictures']
for category in CATEGORIES:
	path = os.path.join(DATADIR,category)
	print(path)
	print(os.listdir(path))

for category in CATEGORIES:
	path = os.path.join(DATADIR,category)
	print(path)
	print(os.listdir(path))
	for file in os.listdir(path):
		print(os.path.join(path, file))



	


#separating files according to their types
paths = []
def different_files(filename, filetype):
    status = filename.lower().endswith(filetype)
    return status

print(different_files('1406.db', '.db'))

for root, dirs, files in os.walk(current_path):
    for dirname in dirs:
        for filename in files:
            if different_files(filename, '.py'):
                print(os.path.join(root,dirname, filename))
            else:
                print('no file of this type')

for root, dirs, files in os.walk(current_path):
    for dirname in dirs:
        for filename in files:
            if different_files(filename, '.pdf'):
                paths.append(os.path.join(root,dirname,filename))

print(paths)


    