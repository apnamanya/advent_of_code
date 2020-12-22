# The code works... It is horrible but it works.


from functools import reduce

def get_grouped_lines(orig_entries):
	group_entries=[]
	answers_list=[]
	for i in range(len(orig_entries)):
		line=orig_entries[i].strip()
		group_entries.extend(line)

		if not line or i== len(orig_entries)-1:
			answers_list.append(sorted(set(list(group_entries))))

			group_entries=[]

	return answers_list

def part1_solution(orig_entries):
	answer_list = get_grouped_lines(orig_entries)
	no_of_answers= []
	for ans in answer_list:
		no_of_answers.append(len(ans))

	return sum(no_of_answers)

def get_group_lineAndPeople_number(orig_entries):
	group_entries=[]
	people_number=[]
	answers_list=[]
	for i in range(len(orig_entries)):
		line=orig_entries[i].strip()
		if line:
			group_entries.append(list(line))

		if not line or i== len(orig_entries)-1:

			people_number.append(len(group_entries))
			answers_list.append(sorted(list(group_entries)))
			group_entries=[]


	return answers_list, people_number

def part2_solution(orig_entries):
	answer_list, group_nos = get_group_lineAndPeople_number(orig_entries)
	ans_list=[]
	intersect_no =[]

	for ans in answer_list:
		ans_list= list(reduce(set.intersection, [set(item) for item in ans ]))
		intersect_no.append(len(ans_list))
	return sum(intersect_no)


def main():
	#start_time = time.perf_counter()
	d1_file= open("input_day6.txt", 'r')
	original_entries=  d1_file.readlines()
	result1= part1_solution(original_entries)

	print(f"Answer to part1: {result1}")

	result2 = part2_solution(original_entries)
	print(f"Answer to part2: {result2}")



if __name__ == "__main__":
	main()
