def entries_2_int(orig_entries):
	nums_list=[0]
	for line in orig_entries:
		line_int=int(line.strip(".\n"))
		nums_list.append(line_int)
	nums_list.append(sorted(nums_list)[-1]+3)
	#print(nums_list)
	return nums_list

def part1_solution(orig_entries):
	numbers_list=entries_2_int(orig_entries)
	sorted_nums=sorted(numbers_list)

	diff_jolts=[]
	#print(len(sorted_nums))
	for i, num in enumerate (sorted_nums):
		if i!=0:
			diff_jolts.append(num-sorted_nums[i-1])

	#print(diff_jolts)
	diff_jolts3=diff_jolts.count(3)
	diff_jolts1=diff_jolts.count(1)
	#print(diff_jolts3)
	#print(diff_jolts1)
	return(diff_jolts3* diff_jolts1)

def part2_solution(orig_entries):
	numbers_list=entries_2_int(orig_entries)
	sorted_nums=sorted(numbers_list)
	print(sorted_nums)

	comb=[]
	combinations=[]
	ways=[sorted_nums]
	i=1
	baseblocks=[]
	cutoff_index=[]
	#print(sorted_nums)
	new_blocks=[]


	while i<len(sorted_nums)-1:
		#baseblocks=[]
		if sorted_nums[i+1]-sorted_nums[i-1]<=3:



			#print(sorted_nums[i])
			baseblocks.append(sorted_nums[:i])
			#print(baseblocks)
			cutoff_index.append(i)
			#print(cutoff_index)
			new_block=(list(set(sorted_nums)-set([sorted_nums[i]])))
			print(new_block)
			new_blocks.append(new_block)


			#for b in new_block:
			#	j=b[:]
			#	j.extend(new_block[len(j):])
			#	print(j)


			#	b.extend(new_block[cutoff_index[-1]:])
				#print(b)



		i+=1
	print("\n")
	print(new_blocks)
	print(baseblocks)
	#print(cutoff_index)



	''''for i, num  in enumerate(sorted_nums):
		insanity=[]
		print(i)
		if i==0:
			comb.append(num)
			insanity.append(comb)
			ways=insanity[:]
		else:
			for w in ways:
				if (num -w[-1])<=3:
					combinations.append(num)
					break

				else:
					for c in combinations:
						base_comb =w[:]
						base_comb.append(c)
						if (num -c)<=3:
							base_comb.append(num)
						insanity.append(base_comb)
					combinations=[]
					ways=insanity[:]


	print(comb)
	print(combinations)
	print(ways)'''


def main():
	d1_file= open(r"c:\Users\anamanya\Desktop\advent_code\2020\input_day10e.txt", 'r')
	original_entries=  d1_file.readlines()
	result1= part1_solution(original_entries)
	print(f"Answer to part1: {result1}")
	part2_solution(original_entries)
	#result2=part2_solution(original_entries,result1 )
	#print(f"Answer to part2: {result2[0]+result2[-1]}")


if __name__ == "__main__":
	main()
