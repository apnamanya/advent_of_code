from tabulate import tabulate

def fuel_cal(mass):
    return int((int(mass)/3))-2
def main():
    d1_file= open("day1_input.txt", 'r')
    masses = d1_file.readlines()
    
    tb_rows=[]
    part1_fuel=0
    part2_fuel=0
    for mass in masses:
        fuel=fuel_cal(mass)
        mass_fuel=[]
        while fuel>0:
            mass_fuel.append(fuel)
            fuel=fuel_cal(fuel)
        table_row=[int(mass),mass_fuel,sum(mass_fuel)]
        tb_rows.append(table_row)
        part1_fuel += mass_fuel[0]
        part2_fuel += sum(mass_fuel)
    table=tabulate(tb_rows, headers=["Mass","Fuel_array","Module_Fuel_Total"],tablefmt='orgtbl')
    print(table)
    print("********************************************************************************************")
    print (f"Part1 fuel = {part1_fuel}")
    print (f"Part2 fuel = {part2_fuel}")
 
if __name__ == "__main__":
    main()



