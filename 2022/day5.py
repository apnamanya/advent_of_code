
import prep
import string
import re
def soln1(entries):
    instruct_break =entries.index("")
    #print (instruct_break)
    cubes=entries[:instruct_break]
    cube_pos=[]
    for cubes_list in cubes[:-1]:
        cube_pos.append((cubes_list.replace("    ",":").replace("] ","]:")).split(":"))
    print(cube_pos)
    #print(cubes)
    instruct_numbers=[]
    instruct_list=entries[instruct_break+1:]
    for ent in instruct_list:
        #print(ent)
        instruct_numbers.append(re.findall(r'\d+',ent))
        #instructions={"block_no":instruct_numbers[0], "from":instruct_numbers[1] ,"to":instruct_numbers[2]}
    print(instruct_numbers)
    pos=[[],[],[],[]]
    message=""
    for cp in cube_pos:
        if cp[0]:pos[1].append(cp[0])
        if cp[1]:pos[2].append(cp[1])
        if cp[2]:pos[3].append(cp[2])
    print(pos[1])
    print(pos[2])
    print(pos[3])
    
    # print("----- first interation----")
    # pos1.insert(0,pos2[0])
    # pos2[0]="" 
    # print(pos1)
    # print(pos2)
    # print(pos3)

    # print("----- 2nd interation----")
    # pos3.insert(0,pos1[0])
    # pos3.insert(0,pos1[1])
    # pos3.insert(0,pos1[2])
    # pos1[0]=pos1[1]=pos1[2]=""
    # print(pos1)
    # print(pos2)
    # print(pos3)

    # print("----- 3rd interation----")
    # pos1.insert(0,pos2[1])
    # pos1.insert(0,pos2[2])
    # pos2[1]=pos2[2]=""
    # print(pos1)
    # print(pos2)
    # print(pos3)
    # print("----- 4th interation----")
    # pos2.insert(0,pos1[0])
    # pos1[0]=""
    # while("" in pos1):pos1.remove("") 
    # while("" in pos2):pos2.remove("") 
    # while("" in pos3):pos3.remove("") 
    # print(pos1)
    # print(pos2)
    # print(pos3)
    # message=(pos1[0]+pos2[0]+pos3[0]).replace("[", "").replace("]",'')
    

    return message

    
def main():
    day=5
    original_entries= prep.readfile_unstrip(day)
    print(original_entries)
    print(soln1(original_entries))
    #print(soln2(original_entries))


if __name__ == "__main__":
	main()