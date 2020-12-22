import time
import re
from pprint import pprint


def parse_input(orig_entries):
	bags_list= []

	for line in orig_entries:
		line_str=line.strip("\n")
		b1, b2 = line_str.split("bags contain")
		b2_sections = b2.split(",")
		bags_dict={"b1_colour":b1.strip(), "contain":[]}
		for b2_sec in b2_sections:
			b2_sec_list= b2_sec.split(" ")
			number = b2_sec_list[1]
			b2_colour = f"{b2_sec_list[2]} {b2_sec_list[3]}"
			bags_dict["contain"].append({"b2_number":number,"b2_colour":b2_colour})
		bags_list.append(bags_dict)

	return bags_list

def p1_iteration_search(bags_list, colour):
	count=0
	lvl2_bags =[]
	for bags in bags_list:
		if colour in bags['b1_colour']:
			count+=1

		else:
			for bgs in bags["contain"]:
				if colour in bgs['b2_colour']:
					lvl2_bags.append(bags['b1_colour'])
					count+=1

	return count, lvl2_bags

def p1_initial_clr_search(bags_def, colour):
	count=0
	lvl2_bags =[]
	for bags in bags_def:
		for bgs in bags["contain"]:
			if colour in bgs['b2_colour']:
				lvl2_bags.append(bags['b1_colour'])
				count+=1

	return count, lvl2_bags

def part1_solution(orig_entries):
	bags = parse_input(orig_entries)
	n , new_clrs = p1_initial_clr_search(bags, "shiny gold")
	clrs_found=[]

	while len(new_clrs)>0:
		bs2=[]
		for b in new_clrs:
			c, bgs= p1_iteration_search(bags, b)
			bs2.extend(bgs)

		clrs_found.extend(new_clrs)
		new_clrs=list(set(bs2)-set(clrs_found))

	return list(set(clrs_found))


def create_math_str(bags_list, clr):
	math_str="1 "
	clr2 = []
	for bg in bags_list:
		if bg["b1_colour"]==clr:
			for bc in bg['contain']:
				if bc['b2_number']=='no':
					value = (f"(0*0) ")
				else:
					clr2.append(bc['b2_colour'])
					value = (f"({bc['b2_number']}*({bc['b2_colour']})) ")
				math_str =f"{math_str}+ {value}"
	return math_str,clr2

def part2_solution(orig_entries):
	bags = parse_input(orig_entries)
	clr1= "shiny gold"
	math_st, cl2 = create_math_str(bags, clr1)
	new_math_st = math_st

	new_clrs= cl2[:]

	i=1

	while len(new_clrs)>0:

		inner_clrs=[]
		for cl in new_clrs:
			math_st2, cl3 = create_math_str(bags, cl)
			new_math_st = new_math_st.replace(cl, math_st2)
			inner_clrs.extend(cl3)


		new_clrs=list(set(inner_clrs))
		i+=1

	return (eval (new_math_st)-1)


def main():
	d1_file= open("input_day7.txt", 'r')
	original_entries=  d1_file.readlines()
	result1= part1_solution(original_entries)
	print(f"Answer to part1: {len(result1)}")
	result2= part2_solution(original_entries)
	print(f"Answer to part1: {result2}")


if __name__ == "__main__":
	main()
