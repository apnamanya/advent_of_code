import sys, prep

def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])
def argmax(a):
    return max(range(len(a)), key=lambda x : a[x])

str_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0
day=1
original_entries= prep.readfile_unstrip(day)
calibv=[]

for line in original_entries:
    print("------------------")
    print(line)
    first_num_idxs = [line.find(x) for x in nums]
    last_num_idxs = [line.rfind(x) for x in nums]
    first_str_idxs = [line.find(x) for x in str_nums]
    last_str_idxs = [line.rfind(x) for x in str_nums]
    print(first_num_idxs)
    print(last_num_idxs)
    print(first_str_idxs)
    print(last_str_idxs)


    first_num_idxs[:] = [x if x != -1 else len(line) for x in first_num_idxs]
    first_str_idxs[:] = [x if x != -1 else len(line) for x in first_str_idxs]
    print(first_num_idxs)
    print(first_str_idxs)

    if min(first_num_idxs) < min(first_str_idxs):
        tens = argmin(first_num_idxs)
    else:
        tens = argmin(first_str_idxs)
        
    print(tens)

    if max(last_num_idxs) > max(last_str_idxs):
        ones = argmax(last_num_idxs)
    else:
        ones = argmax(last_str_idxs)
    print(ones)
    t = tens*10 + ones
    # print(tens, ones, t)
    calib_value =int(f"{tens}{ones}")
    calibv.append(calib_value)
    total += t
    
#print(total)
print(calibv)