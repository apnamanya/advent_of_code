def prep(entries):
    grouped_list = []
    one_elf=[]
    for ent in entries:
        if len(ent)>0:
            one_elf.append(int(ent))
        else:
            one_elf=[]
            grouped_list.append(one_elf)
    cal_list=[sum(group)for group in grouped_list]
    return  cal_list, grouped_list

def soln1(grouped_list):
    cal_max=max(grouped_list)
    return cal_max

def soln2(groupedl):
    groupedl.sort()
    return sum(groupedl[-3:])


def advent_of_code_2022_day_1(arr):
    total = 0
    for num in arr:
        if type(num) == list:
            total += advent_of_code_2022_day_1(num)
        else:
            total += num
    return total

# example usage
#arr = [1, [2,3], 4, [5,6]]
#print(advent_of_code_2022_day_1(arr)) # prints 21



def main():
    d1_file= open("./input_day1.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    glist, arr=prep(original_entries)
    print(soln1(glist))
    print(soln2(glist))
    arr = [[1000,2000,3000],4000,[5000,6000],[7000,8000,9000],10000]#[1, [2,3], 4, [5,6]]
    print(advent_of_code_2022_day_1(arr))


if __name__ == "__main__":
	main()