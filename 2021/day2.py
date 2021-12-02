def part1_soln(entries):
    h_increase =[]
    v_increase =[]
    v_decrease=[]

    for ind, entry in enumerate(entries):
        value=(int(entry.split(" ")[-1]))
        if "forward" in entry:
            h_increase.append(value)
        if "down" in entry:
            v_increase.append(value)
        if "up" in entry:
            v_decrease.append(value)
        
    return (sum(h_increase)* (sum(v_increase)- sum(v_decrease)))

def part2_soln(entries):
    postion=0
    depth=0
    aim=0
    for ind, entry in enumerate(entries): 
        value=(int(entry.split(" ")[-1]))
        if "forward" in entry:
            postion+=value
            depth+=(aim*value)
        if "down" in entry:
            aim+=value
        if "up" in entry:
            aim-=value
    return postion*depth

def main():
    d1_file= open("./input_day2.txt", 'r')
    original_entries= [i for i in d1_file.readlines()]

    print(part1_soln(original_entries))
    print(part2_soln(original_entries))

if __name__ == "__main__":
	main()