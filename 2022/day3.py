import string
def soln2(entries):
    startcounter=0
    endcounter=2
    window=3
    total_score=0
    while endcounter<len(entries):
        common_letter=list(set(entries[startcounter]).intersection(entries[startcounter+1]).intersection(entries[endcounter]))
        #print(common_letter)
        startcounter=startcounter+window
        endcounter=endcounter+window
        for cl in common_letter:
            score=(string.ascii_letters.index(cl)+1)
            total_score=total_score+score
    return total_score
    



def soln1(entries):
    total_score=0
    for ent in entries:
        midpoint=int(len(ent)/2)
        #print(ent[:midpoint]+" : "+ent[-midpoint:])
        common_letter=list(set(ent[:midpoint]).intersection(ent[-midpoint:]))
        for cl in common_letter:
            score=(string.ascii_letters.index(cl)+1)
            total_score=total_score+score
    return total_score

def main():
    d1_file= open("./input_day3.txt", 'r')
    original_entries= [i.strip() for i in d1_file.readlines()]
    #print(original_entries)
    print(soln1(original_entries))
    print(soln2(original_entries))


if __name__ == "__main__":
	main()