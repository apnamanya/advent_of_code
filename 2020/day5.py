import time

def letter_def(l, array):
	if l == "F" or l=="L":
		return array[0:int(len(array)/2)]
	if l =="B" or l=="R":
		return array[int(len(array)/2):len(array)]


def part1(orig_entries):
	seat_IDs =[]
	for line in orig_entries:
		line_list= list(line.strip())

		col_list = line_list[:-3]
		row_list = line_list[-3:]


		col_array = [x for x in range(128)]
		row_array = [x for x in range(8)]
		i=0
		while i<len(col_list):
			col_array = letter_def(col_list[i],col_array)
			i+=1

		j=0
		while j<len(row_list):
			row_array = letter_def(row_list[j],row_array)
			j+=1

		seat_ID = col_array[0]*8+row_array[0]
		seat_IDs.append(seat_ID)

		#print(f"[{col_array[0]},{row_array[0]},{seat_ID}]")
	return seat_IDs

def get_seatID(passID): # Justin's code that copied to test out the binary trees.
    rows = int(passID[:7].replace("B","1").replace("F","0"),base=2)
    cols = int(passID[7:].replace("R","1").replace("L","0"),base=2)
    seatID = rows * 8 + cols
    return seatID

def part2(seat_id_list):
	sorted_list = sorted(seat_id_list)
	start, end = sorted_list [0], sorted_list [-1]

	return sorted(set(range(start, end + 1)).difference(sorted_list))

def part1_binary(orig_entries):
	seat_IDs =[]
	for line in orig_entries:
		line_l= line.strip()
		seat_IDs.append(get_seatID(line_l))

	return seat_IDs

def main():
	start_time = time.perf_counter()
	d1_file= open("input_day5.txt", 'r')
	original_entries=  d1_file.readlines()
	#result = part1(original_entries) # This makes it a whole micro second slower
	result = part1_binary(original_entries)
	print(f"Answer to part1: {max(result)}")
	result2= part2(result)
	print(f"Answer to part2: {result2}")
	end_time = time.perf_counter()
	print(f"time spent: {end_time-start_time}")


if __name__ == "__main__":
	main()
