
from tabulate import tabulate

def part1(orig_entries):
	tb_rows=[]
	valid=0
	for entries in orig_entries:
		policy, password = entries.split(":")
		pol_control, pol_char = policy.split(" ")
		low_bd, up_bd =pol_control.split("-")
		occurances = password.count(pol_char)
		tb_row = [low_bd,up_bd,pol_char,password,occurances, "no"]

		if occurances <=int(up_bd) and occurances >=int(low_bd):
			valid+=1
			tb_row = [low_bd,up_bd,pol_char,password,occurances, "yes"]

		tb_rows.append(tb_row )

	table=tabulate(tb_rows, headers=["low_bd","up_bd","pol_char","password","occurances","policy_met"],tablefmt='orgtbl')
	print(table)
	print(f"Answer to the question = {valid}\n\n")

def part2(orig_entries):
	tb_rows=[]
	valid=0
	for entries in orig_entries:

		policy, password = entries.split(":")
		pol_control, pol_char = policy.split(" ")
		low_bd, up_bd =[int(i)for i in pol_control.split("-")]
		pswd_list=list(password.strip())

		#Exactly one of these positions (low_bd or up_bd) must contain the given letter else it is invalid

		if pswd_list[low_bd-1]==pol_char and pswd_list[up_bd-1]!=pol_char : # 1 is 0 -array index
			valid+=1
			tb_row = [low_bd,up_bd,pol_char,password, "yes"]

		elif pswd_list[up_bd-1]==pol_char and pswd_list[low_bd-1]!=pol_char:
			valid+=1
			tb_row = [low_bd,up_bd,pol_char,password, "yes"]

		else:
			tb_row = [low_bd,up_bd,pol_char,password, "No"]

		tb_rows.append(tb_row )

	table=tabulate(tb_rows, headers=["low_bd","up_bd","pol_char","password","policy_met"],tablefmt='orgtbl')
	#print(table)
	print(f"Answer to the part2 = {valid}")


def part2_2(orig_entries):
	tb_rows=[]
	valid=0
	for entries in orig_entries:

		policy, password = entries.split(":")
		pol_control, pol_char = policy.split(" ")
		low_bd, up_bd =[int(i)for i in pol_control.split("-")]
		pswd_list=list(password.strip())

		#Exactly one of these positions (low_bd or up_bd) must contain the given letter else it is invalid
		#Creating a string of the important character positions in the password.
		pol_pswd_chars=f"{pswd_list[low_bd-1]}{pswd_list[up_bd-1]}"

		if pol_pswd_chars.count(pol_char)==1: #The count of the pol_char should be 1 for the password to be valid.
			valid+=1
			tb_row = [low_bd,up_bd,pol_char,password, "yes"]
		else:
			tb_row = [low_bd,up_bd,pol_char,password, "No"]

		tb_rows.append(tb_row )

	table=tabulate(tb_rows, headers=["low_bd","up_bd","pol_char","password","policy_met"],tablefmt='orgtbl')
	#print(table)
	print(f"Answer to the part2 = {valid}")

def main():
	d1_file= open("input_day2.txt", 'r')
	original_entries=  d1_file.readlines()
	part1(original_entries)
	part2(original_entries)
	part2_2(original_entries)


if __name__ == "__main__":
	main()
