def readfile(day):
    d1_file= open(f"./input_day{day}.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    return original_entries

def readfile_unstrip(day):
    d1_file= open(f"./input_day{day}.txt", 'r')
    original_entries= [i.strip("\n") for i in d1_file.readlines()]
    return original_entries
    