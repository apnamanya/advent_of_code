
from pprint import pprint
def main():
    d_file= open("input_daytest.txt", 'r')
    #d_file= open("input_day4.txt", 'r')
    original_entries= [i.strip("\n") for i in d_file.readlines()]
    draw_numbers =  [int (i) for i in original_entries[0].split(",")]
    original_entries.remove('')
    #print(original_entries)
    #print(draw_numbers)
    boards={}
    i=1
    num=0
    board_len = 6
    while i in range (len(original_entries)):
        boards.update({num:original_entries[i:i+board_len]})
        num+=1
        i=i+board_len

    
    fmt_boards={}
    for kb,vb in boards.items():
        vb_arrays=[]
        for vals in vb:
            vb_arrays.append([int(i)for i in vals.split(" ")if i!=""])

        fmt_boards.update({kb:vb_arrays.remove([])})

    pprint(fmt_boards)
    draft=len(fmt_boards[0][0])
    print(draft)
    while draft in range(len(draw_numbers)):
        print(draw_numbers[0:draft])
        for kfb, vfb in boards.items():
            for vf in vfb:
                if (all(v in draw_numbers[0:draft] for v in vf)):
                    print(vf)
                    print(kfb)
                    return kfb
        draft+=1
        




        


    #print(part1_soln(original_entries))
    #print(part2_soln(original_entries))

if __name__ == "__main__":
	main()