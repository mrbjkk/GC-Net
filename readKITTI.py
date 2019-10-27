import os
import pickle
dir_scene = './KITTI2015_SceneFlow/training/image_2'
paths=[]

for root, dirs, files in os.walk(dir_scene):
    for file in files:
        paths.append(os.path.join(root, file))

# print(len(paths))
# print(paths)

def sortindex(elem):
#     index = list(elem)
    return list(map(int, [list(elem)[-8], list(elem)[-9], list(elem)[-10]]))

paths_left = []
paths_right = []
for i in range(len(paths)):
    if list(paths[i])[-5] == '0':
        paths_left.append(paths[i])
    elif list(paths[i])[-5] == '1':
        paths_right.append(paths[i])

print(list(paths_left[0]))
# print(paths_left)
# print("==================================================================")
# print(paths_right)
