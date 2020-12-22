'''def mD_array(original_entries, array_dim):
	print (array_dim)
	d_array=[]
	counter= [n for n in range(array_dim)]
	print(counter)
	while i<len(original_entries):
		result=
	while array_dim>0:
		d_array.append(original_entries)
		array_dim-=1


	return d_array'''

def part1(entries):
	for i, entry in enumerate(entries):
		for j, ent in enumerate (entries):
			if int(entry)+ int(ent)==2020 and  i!=j:
					print(f"The 1 values {entry} and {ent}")
					answer = int(entry)* int(ent)
					print(f"Part 1 answer = {answer}")
					return

def part2(entries):
	for entry in entries:
		for ent in entries:
			for en in entries:
				if int(entry)+ int(ent)+int(en)==2020:
					print(f"The 3 values {entry} and {ent}, and {en}")
					answer = int(entry)* int(ent)* int(en)
					print(f"Part 1 answer = {answer}")
					return

def main():
	d1_file= open("input_day1.txt", 'r')
	original_entries= [int(i) for i in d1_file.readlines()]
	part1(original_entries)
	part2(original_entries)




if __name__ == "__main__":
	main()
