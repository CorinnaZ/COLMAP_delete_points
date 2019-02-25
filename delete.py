import re
imagelist = 'imglist.txt'
pointfile = 'points3D.txt'
resultfile = 'text.txt'
delete = []
numbers = []
ids = []
indices = []
# open files
result = open(resultfile, 'a')
with open(imagelist) as f:
    imglist = f.readlines()
with open(pointfile) as g:
    ptfile = g.readlines()
# extract image ids that should be deleted
for line in imglist:
    numbers.extend(re.findall(r'\d+', line))
numbers = [float(x) for x in numbers]
# extract lines in points3D.txt
for line in ptfile:
    ids.append([s for s in line.split()])
# collect in list: only image ids and point2D id of each line
for line in ids:
    indices.append(line[8:])
# delete all entries in indices that belong to deleted images
for delete in numbers:
    for k, line in enumerate(indices):
        line = indices[k]
        line = [float(x) for x in line]
        for j, item in enumerate(line):
            if j%2 == 0 and  delete == item:
                index = line.index(delete)
                mydel = line[index+1]
                indices[k].remove(str(int(delete)))
                indices[k].remove(str(int(mydel)))
# if no image ids remain: do not write the line
# if any image ids remain: write the line (without ids for deleted images)
for k, line in enumerate(indices):
    if not line:
        print("Empty! Index: "+str(k))
    else:
        for item in ids[k][:8]:
            result.write(str(item)+" ")
        for item in indices[k]:
            result.write(str(item)+" ")
        result.write("\n")
