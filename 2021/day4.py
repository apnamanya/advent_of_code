
from pprint import pprint
def get_board_draft(entries):
    draw_numbers =  [int (i) for i in entries[0].split(",")]
    entries.remove('')
    print("this crazy...")
    #print(original_entries)
    #print(draw_numbers)
    boards={}
    i=1
    num=0
    board_len = 6
    while i in range (len(entries)):
        boards.update({num:entries[i:i+board_len]})
        num+=1
        i=i+board_len

    fmt_boards={}
    for kb,vb in boards.items():
        vb_arrays=[]
        for vals in vb:
            vb_arrays.append([int(i)for i in vals.split(" ")if i!=""])

        fmt_boards.update({kb:vb_arrays})

    #pprint(fmt_boards)
    draft=len(fmt_boards[0][0])
    
    while draft in range(len(draw_numbers)):
        #print(draft)
        #print(draw_numbers[0:draft])
        for kfb, vfb in fmt_boards.items():
            for vf in vfb:
                if (all(v in draw_numbers[0:draft] for v in vf)) and vf !=[]:
                    print(kfb)
                    return kfb, vfb, draw_numbers[0:draft]
        draft+=1
def part1_soln(entries):
    board_num, board, drafted_nums=get_board_draft(entries)
    all_board_nums=[]
    for b_line in board:
       all_board_nums.extend(b_line) 
    print(all_board_nums)
    not_called = list(set(all_board_nums)- set(drafted_nums))
    print(not_called)
    result=sum(not_called)*drafted_nums[-1]
    return result



def main():
    #d_file= open("input_daytest.txt", 'r')
    d_file= open("input_day4.txt", 'r')
    original_entries= [i.strip("\n") for i in d_file.readlines()]
  
    print(part1_soln(original_entries))
    #print(part2_soln(original_entries))

if __name__ == "__main__":
	main()