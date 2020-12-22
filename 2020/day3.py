
import math
import time

def part1(orig_entries,  right_inc ,down_inc):

	square="."
	tree ="#"
	entry_dict={".":"O", "#":"X"}
	r_mov=0
	d_mov=0
	findings=[]

	while d_mov<(len(orig_entries)-1):
		d_mov+=down_inc
		pos_list=list(orig_entries[d_mov].strip())
		r_mov+=right_inc
		if r_mov>=len(pos_list):
			r_mov-=len(pos_list)

		findings.append(entry_dict[pos_list[r_mov]])

	#print(findings)
	#print(findings.count(entry_dict[tree]))
	return findings.count(entry_dict[tree])

def part2(orig_entries,array):
	outputs=[]
	for i in array:
		right_inc ,down_inc=i[0],i[1]
		outputs.append(part1(orig_entries,  right_inc ,down_inc))

	print(outputs)
	return math.prod(outputs)


def main():
	start_time = time.perf_counter()
	d1_file= open("input_day3.txt", 'r')
	original_entries=  d1_file.readlines()
	result= part1(original_entries,3, 1)
	print(f"Answer to part1: {result}")

	part2_array=[[1,1], [3,1],[5,1],[7,1],[1,2]]
	result2= part2(original_entries, part2_array)
	print(f"Answer to part2: {result2}")
	end_time = time.perf_counter()
	print(f"time spent: {end_time-start_time}")

if __name__ == "__main__":
	main()
