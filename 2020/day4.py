from pprint import pprint
import re
import math

def part1_get_passport_blocks(orig_entries):
	blocks=[]
	passports={}
	start_block=0
	for i in range(len(orig_entries)):
		line=list(orig_entries[i].strip())
		#print(line)
		if not line:
			blocks.append(i)
	for i, block in enumerate(blocks):
		key=f"passport_{i}"
		passports.update({key:f"{orig_entries[start_block:blocks[i]]}"})
		start_block=blocks[i]+1

	#pprint(passports)
	return passports


def part1_solution(dict_passports, array_passport_fields):
	#passport dont have to contain a cid field
	#comp_fields=[ele for ele in array_passport_fields if ele != "cid"]
	comp_fields=list(set(array_passport_fields)-set(["cid"]))


	#Check for the other existance of other passport fields
	valid_passports_dict ={k:val for k, val in dict_passports.items()if all(f"{fld}:" in val for fld in comp_fields)}

	#pprint(valid_passports_dict)

	return valid_passports_dict


def proper_passport_dict(orig_entries):# because improper dicts bit me where it hurts.
	blocks=[]
	passports=[]
	start_block=0
	entries=[]
	for i in range(len(orig_entries)):
		line=list(orig_entries[i].strip())
		entries.append(orig_entries[i].strip().split(" "))
		if not line:
			blocks.append(i)
	for i, block in enumerate(blocks):
		init={}
		for ele in entries[start_block:blocks[i]]:
			for el in ele:
				k, value = el.split(":")
				init.update({k: value})

		passports.append(init)
		start_block=blocks[i]+1

	#pprint(passports)
	return passports

def part2_1_valid_passport(list_passports, array_passport_fields):
	#passport dont have to contain a cid field
	#comp_fields=[ele for ele in array_passport_fields if ele != "cid"]
	comp_fields=list(set(array_passport_fields)-set(["cid"]))
	#Check for the other existance of other passport fields
	valid_passports_list =[val for val in list_passports if all(fld in val.keys() for fld in comp_fields)]

	#pprint(valid_passports_list)

	return valid_passports_list


def part2_solution(list_passport, passport_fields, vald_t):
	valid_pp=[]
	for pass_dets in list_passport:
		status={}
		#print(f"\n entry for {pass_dets}")

		if pass_dets["ecl"] in vald_t["ecl"]:
			status.update({"ecl":1})
		else:status.update({"ecl":0})

		for i in vald_t["hgt"]["options"]:
			if i["unit"] in pass_dets["hgt"] and i["atleast"]<= int(pass_dets["hgt"].replace(i["unit"], "")) <= i["atmost"]:
				status.update({"hgt":1})
				break
			else:status.update({"hgt":0})

		hcl_pattern= re.compile(vald_t["hcl"]["reg_str"])
		match_hcl =re.search(hcl_pattern, pass_dets["hcl"])
		if match_hcl:
			status.update({"hcl":1})
		else:status.update({"hcl":0})

		pid_pattern = re.compile(vald_t["pid"]["reg_str"])
		match_pid = re.search(pid_pattern, pass_dets["pid"])
		if match_pid:
			status.update({"pid":1})
		else:status.update({"pid":0})

		for k in passport_fields[:3]:
			if len(pass_dets[k])==vald_t[k]["length"] and vald_t[k]["atleast"]<= int(pass_dets[k])<= vald_t[k]["atmost"]:
				status.update({k:1})

			else:
				status.update({k:0})

		#print(status)
		if math.prod(status.values())==1:
			valid_pp.append(pass_dets)

	return(valid_pp)


def main():
	d1_file= open("input_day4.txt", 'r')
	original_entries=  d1_file.readlines()
	passport_fields=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
	valid_passports=part1_solution(part1_get_passport_blocks(original_entries), passport_fields)
	result=len(valid_passports)
	print(f"Answer to part1: {result}")

	valid_passports= part2_1_valid_passport(proper_passport_dict(original_entries),passport_fields)
	result=len(valid_passports)
	print(f"Answer to part1: {result}")

	validity_dict = {
					"byr":{"length":4, "atleast":1920,"atmost":2002},
					"iyr":{"length":4, "atleast":2010,"atmost":2020},
					"eyr":{"length":4, "atleast":2020,"atmost":2030},
					"hgt":{"options":[{"unit":"cm","atleast":150,"atmost":193},{"unit":"in","atleast":59,"atmost":76}]},
					"hcl":{"reg_str":r'#([0-9a-fA-F]+)'},
					"ecl":["amb","blu","brn","gry","grn","hzl","oth"],
					"pid":{"reg_str":r'^([0-9]{9})$'},
					}

	result2 = part2_solution(valid_passports, passport_fields, validity_dict)
	print(f"Answer to part2: {len(result2)}")


if __name__ == "__main__":
	main()
