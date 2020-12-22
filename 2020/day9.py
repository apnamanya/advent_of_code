
def rolling_window(seq, window_size): #Stackoverflow to the rescue.
    it = iter(seq)
    win = [next(it) for cnt in range(window_size)] # First window
    yield win
    for e in it: # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        yield win


def entries_2_int(orig_entries):
	nums_list=[]
	for line in orig_entries:
		line_int=int(line.strip(".\n"))
		nums_list.append(line_int)
	return nums_list

def find_2nums(entries, sum_qn):
	status=False
	for i, entry in enumerate(entries):
		for j, ent in enumerate (entries):
			if entry+ ent== sum_qn and  i!=j:
				status=True
				return status
	return status

def part1_solution(orig_entries):
	numbers_list=entries_2_int(orig_entries)
	wrong_numbers =[]

	for line in orig_entries:
		line_int=int(line.strip(".\n"))
		numbers_list.append(line_int)

	preample_list=numbers_list[:25]

	for num in numbers_list[25:]:
		if not find_2nums(preample_list, num):
			wrong_numbers.append(num)

		preample_list=preample_list[1:25]
		preample_list.append(num)
	return wrong_numbers[0]


def part2_solution(orig_entries, pt1_soln):
	numbers_list=entries_2_int(orig_entries)
	wrg_num_i=numbers_list.index(pt1_soln)
	list_sum =0
	n=5

	while list_sum != pt1_soln:
		for w in rolling_window(numbers_list[:wrg_num_i], n):
			list_sum = sum(w)
			if list_sum==pt1_soln:
				return sorted(w)
		n+=1

def main():
	d1_file= open("input_day9.txt", 'r')
	original_entries=  d1_file.readlines()

	result1= part1_solution(original_entries)
	print(f"Answer to part1: {result1}")
	result2=part2_solution(original_entries,result1 )
	print(f"Answer to part2: {result2[0]+result2[-1]}")


if __name__ == "__main__":
	main()
