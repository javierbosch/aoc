import sys
data_file = open(sys.argv[1], "r")
data = data_file.read()
lines = data.split("\n")

class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []
        self.size = 0
        self.parent = None

    def addFile(self, file_):
        self.files.append(file_)
    
    def addFolder(self,folder):
        folder.parent = self
        self.folders.append(folder)

    def findFolder(self,name):
        for f in self.folders:
            if f.name == name:
                return f
    
    def calculate_sizes(self):
        size = sum([f.size for f in self.files])
        size += sum([f.calculate_sizes() for f in self.folders])
        self.size = size
        return size

counter_part1 = 0

def part1(root_):
    global counter_part1
    size = sum([f.size for f in root_.files])
    size += sum([part1(f) for f in root_.folders])
    if size<100000:
        counter_part1 += size
    return size

root = folder("/")
current = root
i = 1

while i < len(lines):
    if not lines[i].startswith("$"):
        fst, snd = lines[i].split()
        if fst == "dir":
            folder_ = folder(snd)
            current.addFolder(folder_)
        else:
            file_ = file(snd, int(fst))
            current.addFile(file_)
    elif lines[i] == "$ ls":
        pass
    elif lines[i] == "$ cd ..":
        current = current.parent
    else:
        _, _ , folder_name = lines[i].split()
        current = current.findFolder(folder_name)
    i += 1



part1(root)
    
root.calculate_sizes()

smallest_size = 70000000

must_free = 30000000 - (70000000 - root.size)

def part2(root_):
    global smallest_size
    if root_.size > must_free:
        if root_.size < smallest_size:
            smallest_size = root_.size
        for f in root_.folders:
            part2(f)

part2(root)

print("Part 1:", counter_part1)
print("Part 2:", smallest_size)


data_file.close()
