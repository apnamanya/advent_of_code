def position_arry(entries):
    entry_positions=[[]]
    arr_len=len(entries[0])
    for i in range(arr_len):
        entry_positions.append([])

    for entry in entries:
        for i in range(arr_len):
            entry_positions[i].append(int(entry[i]))

    return entry_positions[:-1]

def part1_soln(entries):
    entry_positions=position_arry(entries)

    epi_val=''
    g_val=''
    for v in entry_positions:
        epi_val=f'{epi_val}{1 if v.count(1)<len(v)/2 else 0}'
        g_val=f'{g_val}{1 if v.count(1)>len(v)/2 else 0}'

    gam=int(g_val, 2)
    epi= int(epi_val, 2)

    return  g_val,epi_val, gam*epi

def get_max_bit(entries, type, position):
    n=position
    count1=[int(item[n]) for item in entries].count(1)
    count0=[int(item[n]) for item in entries].count(0)
    if type=="O2":
        max_bit =1 if count1>=count0 else 0
    elif type=="CO2":
        max_bit=0 if count0<=count1 else 1
    else:
        print(f"Enter the type to consider: O2 or CO2 and not {type}")
        
    return count1, count0, max_bit, type

def get_rating(entries, type):
    i=0
    parsed_entries=entries[:]
    while len(parsed_entries)>1:
        sorted_ent=[]
        maxbit=get_max_bit(parsed_entries, type, i)[2]
        for pe in parsed_entries:
            if maxbit==int(pe[i]):
                sorted_ent.append(pe)
        i+=1
        parsed_entries=sorted_ent[:] 
    return parsed_entries[0]

def part2_soln(entries):
    i=0
    co_rating_binary=get_rating(entries, "CO2")
    o_rating_binary=get_rating(entries, "O2")
    o2=int(o_rating_binary, 2)
    co2= int(co_rating_binary, 2)

    return co_rating_binary,o_rating_binary, o2*co2

def main():
    #d1_file= open("input_daytest.txt", 'r')
    d1_file= open("input_day3.txt", 'r')
    original_entries= [i.strip()for i in d1_file.readlines()]

    print(part1_soln(original_entries))
    print(part2_soln(original_entries))

if __name__ == "__main__":
	main()