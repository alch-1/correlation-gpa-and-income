# Data cleaning: remove all impossible and 0 GPAs

# A brief explanation on why this is needed:
# In SMU (the university in which data was gathered), there are only
# these possible GPA scores for each module: 0, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4 and 4.3.
# Given this, and given that a student generally does not take more than 45 modules, there is a fixed set of possible GPAs;
# If the GPA in our dataset is not in this set, then we know it is false data as the GPA would be mathematically impossible to attain.
# This code aims to eliminate such GPAs.
# This also removes the "trolls" that input their GPA as > 4.3. (One person declared their GPA to be 300...)

import csv

FILENAME = r"STAT101 Survey.csv"

def is_gpa_possible(a):
    GPA_IMMUT = None
    # Q: Why the try/except?
    # A: The first list would be the header. This would be a string.
    #    All other entries would be floats or integers, as required by the Google Form that was used.
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
                return True # The GPA is attainable, ie, it exists within the set of all possible permutations of combined GPAs given 45 modules are taken.
            elif value > GPA_IMMUT * mod_count: 
                for gpa in GPA_LIST: 
                    unique.add(round(gpa + value, 2)) 
        gpa_copy = unique 
    return False # The GPA is not attainable.

# Read csv to list of lists
with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    lst = list(reader)

indices = []

# Get list of indices that point to data which we wish to delete (unclean data)
for index, l in enumerate(lst):
    if not is_gpa_possible(l[2]) or float(l[2]) == 0.0:
        if index != 0:
            indices.append(index)

# Reverse before deleting to avoid indexing issues
for i in sorted(indices, reverse=True):
    del lst[i]

# Write the cleaned csv
with open("out.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerows(lst)

