def part1_soln(entries):
    increase_count =0
    for ind, entry in enumerate(entries):
        if entries[ind]> entries[ind-1] and ind>0:
            increase_count+=1
    return increase_count

def part2_soln(entries, window_size):
    window_sums=[]
    for ind, entry in enumerate(entries[:-2]): # Top before the last 2
        window_sums.append(sum(entries[window_size-3:window_size]))
        window_size+=1
    return part1_soln(window_sums)

def main():
    d1_file= open("./input_day1.txt", 'r')
    original_entries= [int(i) for i in d1_file.readlines()]
    print(part1_soln(original_entries))

    window_size = 3 #Windowsize
    print(part2_soln(original_entries,window_size ))

if __name__ == "__main__":
	main()