import prep
import re

def d1part1(o_entries):
    calib_values= []
    for entries in o_entries:
        res=[]
        res = re.findall(r'\d', entries)
        calib_value =int(f"{res[0]}{res[-1]}")
        calib_values.append(calib_value)
    result=sum(calib_values)
    return result

def d1part2(o_entries):
    help_dict = {'1':'one','2': 'two','3':'three','4':'four','5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'zero'}
    n_entries=[]
    l_entries=[]
    calib_values= []
    for s in o_entries:
        l=s
        c = list(help_dict.values())
        res2=[s.find(n) for n in c ]
        r_res2=[s.rfind(n) for n in c ]
        ipa=[i for i in res2 if int(i)>=0]
        r_ipa=[i for i in r_res2 if int(i)>=0]
        if len(ipa)>0 or len(r_ipa)>0:
            min_index = res2.index(min(ipa))+1
            max_index = r_res2.index(max(r_ipa))+1
            if help_dict[str(min_index)] in s: s=s.replace(help_dict[str(min_index)],str(min_index))
            if help_dict[str(max_index)] in l: l=l.replace(help_dict[str(max_index)],str(max_index))
        n_entries.append(s)
        l_entries.append(l) 
        first_num=re.findall(r'\d', s)[0]
        last_num=re.findall(r'\d', l)[-1]
        calib_value =int(f"{first_num}{last_num}")
        calib_values.append(calib_value)    
    result=sum(calib_values)
    return result
        


def main():
    day=1
    original_entries= prep.readfile_unstrip(day)
    print(f"Day {day} Part 1: {d1part1(original_entries)}")
    print(f"Day {day} Part 2: {d1part2(original_entries)}")
    
    

if __name__ == "__main__":
	main()
 
 
 