import os

check_for = '#include <sciplot'
rootdir = 'sciplot/sciplot'
def correct_file(subdir, filepath):
    og_file = open(filepath, 'r')
    new_file_name = f'{filepath[:-4]}_r.hpp'
    new_file = open(new_file_name, 'a')
    for line in og_file:
        if line[:len(check_for)] == check_for:
            if subdir == rootdir:
                new_line = line.replace('<sciplot/', '"')
                new_line = new_line.replace('>', '"')
                new_file.write(new_line)
            else:
                new_line = line.replace('<sciplot/', '"../')
                new_line = new_line.replace('<sciplot/specs/', '"')
                new_line = new_line.replace('>', '"')
                new_file.write(new_line)
        else:
            new_file.write(line)

    og_file.close()
    new_file.close()
    os.system(f'rm {filepath}')
    os.system(f'mv {new_file_name} {filepath}')


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith('.hpp'):
            correct_file(subdir, filepath)