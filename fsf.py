import os
directory_list = '.'
ext = ('.svg')
for files in os.listdir(directory_list):
    if files.endswith(ext):
        one_line = '<?xml version="1.0" encoding="utf-8"?>\n'
        with open(files, 'r+') as fp:
            # f_line = fp.readline().rstrip()
            # lines = fp.readlines()
            content = fp.read()
            # if( f_line != one_line.rstrip()):
                # lines.insert(0, one_line)
            fp.seek(0)              
            fp.write(one_line + content)
            # else:
            #     continue
    else:
        continue
