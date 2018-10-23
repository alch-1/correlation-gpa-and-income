import csv

FILENAME = r"C:\Users\--\Google Drive\+Programming\[+]Projects\stat101\STAT101 Survey.csv"

def is_gpa_possible(a):
    GPA_IMMUT = None
    try:
        GPA_IMMUT = float(a)
    except ValueError:
        return None
    GPA_LIST = [0, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3]
    MAX_MODS = 45
    gpa_copy = GPA_LIST[:] 
    for mod_count in range(1, MAX_MODS + 1): 
        unique = set() 
        for value in gpa_copy:
            if value == round(GPA_IMMUT * mod_count, 2): 
                return True
            elif value > GPA_IMMUT * mod_count: 
                for gpa in GPA_LIST: 
                    unique.add(round(gpa + value, 2)) 
        gpa_copy = unique
    return False

with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    lst = list(reader)

indices = []

for index, l in enumerate(lst):
    if not is_gpa_possible(l[2]) or float(l[2]) == 0.0:
        if index != 0:
            indices.append(index)

for i in sorted(indices, reverse=True):
    del lst[i]

with open(r"C:\Users\--\Google Drive\+Programming\[+]Projects\stat101\out.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerows(lst)

