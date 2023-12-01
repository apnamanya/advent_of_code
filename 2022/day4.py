import prep
import numpy as np

def get_elv_ranges(ent):
    # print(ent)
    sec_ranges= ent.split(",")
    elv1_ranges=sec_ranges[0].split('-')
    elv2_ranges=sec_ranges[1].split('-')
    elv1=np.arange(int(elv1_ranges[0]),int(elv1_ranges[1])+1,1)
    elv2=np.arange(int(elv2_ranges[0]),int(elv2_ranges[1])+1,1)
    # print(elv1)
    # print(elv2)
    return elv1, elv2 

def soln2(entries):
    double_coverage_pairs=0
    for ent in entries:
        elv1, elv2=get_elv_ranges(ent)
        if list(set(elv1).intersection(elv2)):
           double_coverage_pairs=double_coverage_pairs+1

    return double_coverage_pairs 



def soln1(entries):
    full_coverage_pairs=0
    for ent in entries:
        elv1, elv2=get_elv_ranges(ent)
        if set(elv1)<= set(elv2) or set(elv2)<= set(elv1):
            full_coverage_pairs=full_coverage_pairs+1

    return full_coverage_pairs


def main():
    day=4
    original_entries= prep.readfile(day)
    #print(original_entries)
    print(soln1(original_entries))
    print(soln2(original_entries))


if __name__ == "__main__":
	main()