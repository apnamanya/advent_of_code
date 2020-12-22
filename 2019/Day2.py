def computer_instructions(opcode_list, new1, new2):
    n=4
    start_position=0
    
    opcode_list[1]=new1
    opcode_list[2]=new2
    
    while len(opcode_list)>start_position:
        last_position=start_position+n
        if last_position<len(opcode_list):
            current_ops =opcode_list[start_position:last_position]
        else:
            current_ops =opcode_list[start_position:len(opcode_list)]
        start_position=last_position
        if current_ops[0]==1:
            opcode_list[current_ops[3]]=opcode_list[current_ops[1]]+opcode_list[current_ops[2]]
        elif current_ops[0]==2:
            opcode_list[current_ops[3]]=opcode_list[current_ops[1]]*opcode_list[current_ops[2]]
        elif current_ops[0]==99:
            break
        else: return("Something went very wrong!")
       
            
    return opcode_list

def main():
    d2_file= open("day2_input.txt", 'r')
    opcodes= d2_file.readline()
    original_opcode_list = [int(i) for i in list(opcodes.split(","))]
    
    part1= computer_instructions(original_opcode_list, original_opcode_list[1], original_opcode_list[1])[0]
    print (f"The answer for part 1 = {part1}")
    A=0
    while A<=99:
        B=0
        while B<=99:
            original_opcode_list = [int(i) for i in list(opcodes.split(","))]
            result = computer_instructions(original_opcode_list, A, B)
            if isinstance(result, list):
                if result[0]== 19690720:
                    #print(result)
                    answer = 100*A+B
                    print(f"The noun and verb are ({A}, {B}) respectively.")
                    print(f"The answer for part 2 is {answer}.")
                    return
            B+=1
        A+=1
    
    
if __name__ == "__main__":
    main()