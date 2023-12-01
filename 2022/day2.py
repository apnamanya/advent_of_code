
elf_draw_order=['A','B','C']
self_draw_order=['X','Y','Z']
loss_comb=['C Y','B X','A Z']
win_comb=['A Y','B Z','C X']
draw_comb=['A X','B Y','C Z']

def soln1(comb_list):
    total_score=0
    for comb in comb_list:
        if comb in win_comb:
            score_add=6
        elif comb in loss_comb:
            score_add=0
        else: 
            score_add=3
        score=(self_draw_order.index(comb.split(' ')[1])+1)+ score_add
        total_score=total_score+score

    return total_score

def soln2(comb_list):
    total_score=0
    for comb in comb_list:
        draw=comb.split(' ')
        if draw[1]=='X': #loss
            score_add=0
            new_comb=loss_comb[:]
        elif draw[1]=='Y': #draw
            score_add=3
            new_comb=draw_comb[:]
        elif draw[1]=='Z': #win
            score_add=6
            new_comb=win_comb[:]
        
        new_comb_choice=[lc for lc in new_comb if lc.startswith(draw[0])]
        #print(new_comb_choice)
        for ncc in new_comb_choice: 
            total_score=total_score+((self_draw_order.index(ncc.split(' ')[1])+1)+ score_add)

    return total_score
    

def main():
    d1_file= open("./input_day2.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    #print(original_entries)
    print(soln1(original_entries))
    print(soln2(original_entries))


if __name__ == "__main__":
	main()