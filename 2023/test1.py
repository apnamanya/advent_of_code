
help_dict = {
        '1':'one',
        '2': 'two',
        '3':'three',
        '4':'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }
# s = 'eightwothree'
c = list(help_dict.values())
res=[s.find(n) for n in c ]
ipa=[i for i in res if int(i)>=0]
while len(ipa)>0:
    m = min(ipa)
    index_m = res.index(m)+1
    ipa.remove(m)
    if help_dict[str(index_m)] in s: s=s.replace(help_dict[str(index_m)],str(index_m))
    
print (s)        
