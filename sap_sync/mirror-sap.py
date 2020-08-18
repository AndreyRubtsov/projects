import shutil

const_sync_file = '/home/undrey/1/now_sync.txt'
prev_sync_file = '/home/undrey/1/prev_sync.txt'

actual_dict = {}
difs = []
with open(const_sync_file, 'r') as f:
    for line in f:
        size, filename = line.split(' ')
        actual_dict[filename] = size
print(actual_dict)

with open(prev_sync_file, 'r') as f:
    for line in f:
        size, filename = line.split(' ')
        if filename in actual_dict:
            if actual_dict[filename] != size:
                print(actual_dict[filename], size)
print(actual_dict)

shutil.copyfile(const_sync_file, prev_sync_file)
