def readfile(day):
    d1_file= open(f"./input_day{day}.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    return original_entries

def readfile_unstrip(day):
    d1_file= open(f"./input_day{day}.txt", 'r')
    original_entries= [i.strip("\n") for i in d1_file.readlines()]
    return original_entries
    
def read_testfile():
    d1_file= open(f"./test_input_day.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    return original_entries

def read_testfile_unstrip(day):
    d1_file= open(f"./test_input_day.txt", 'r')
    original_entries= [i.strip("\n") for i in d1_file.readlines()]
    return original_entries