
def get_instruct_ops(orig_entries):
	instruction_op_tuple_list= []
	for line in orig_entries:
		line_str=line.strip(".\n")
		instr, operand = line_str.split(" ")
		instruction_op_tuple_list.append((instr, operand))

	return instruction_op_tuple_list

def run_program(inst_op_tuple_list):
	n=0
	acc_value=0
	acc_values_list=[]
	n_seq =[]

	while all(n_seq.count(i)<2 for i in n_seq) and n< len(inst_op_tuple_list):
		n_seq.append(n+1)

		if inst_op_tuple_list[n][0]=='acc':
			acc_value+= int(inst_op_tuple_list[n][1])

			n+=1
		elif inst_op_tuple_list[n][0]=='nop':
			n+=1
		elif inst_op_tuple_list[n][0]=='jmp':
			n+=int(inst_op_tuple_list[n][1])

		acc_values_list.append(acc_value)
	return n_seq, acc_values_list

def part1_solution(orig_entries):
	inst_op_tuples=get_instruct_ops(orig_entries)
	program_seq, acc_sums = run_program(inst_op_tuples)
	acc_value = acc_sums[len(list(set(program_seq)))-1]
	return acc_value


def part2_solution(orig_entries):
	inst_op_tuples=get_instruct_ops(orig_entries)
	output_seq =run_program(inst_op_tuples)[0]
	jmp_nop_indices=[]
	for j, io in  enumerate (inst_op_tuples):
		if io[0]=='jmp' or io[0]=='nop':
			jmp_nop_indices.append(j)

	orig_inst_op_tuple=inst_op_tuples[:]
	i=0
	while any(output_seq.count(i)>1 for i in output_seq):
		inst_op_tuples=orig_inst_op_tuple[:]
		if inst_op_tuples[jmp_nop_indices[i]][0]=='jmp':
			inst_op_tuples[jmp_nop_indices[i]]=("nop", inst_op_tuples[jmp_nop_indices[i]][1])
		elif inst_op_tuples[jmp_nop_indices[i]][0]=='nop':
			inst_op_tuples[jmp_nop_indices[i]]=("jmp", inst_op_tuples[jmp_nop_indices[i]][1])
		output_seq, acc_sums = run_program(inst_op_tuples)
		i+=1

	return acc_sums[-1]


def main():
	d1_file= open("input_day8.txt", 'r')
	original_entries=  d1_file.readlines()
	result1= part1_solution(original_entries)
	print(f"Answer to part1: {result1}")
	result2=part2_solution(original_entries)
	print(f"Answer to part2: {result2}")


if __name__ == "__main__":
	main()
