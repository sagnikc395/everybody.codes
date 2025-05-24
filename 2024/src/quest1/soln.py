POINT_MAPPINGS = {
    'A':0,
    'B':1,
    'C':3,
    'D':5,
}



def diabolical_round2(data: str) -> int:
    n = len(data)
    print(f"The length of the string is : {n}")
    points = 0 

    pair_counter = 0 
    for i in range(0,n,2):
        curr_item = data[i]
        next_item = data[i+1]

        if curr_item == 'x':
            points += POINT_MAPPINGS.get(next_item,0)+1
            pair_counter += 1
        elif next_item == 'x':
            points += POINT_MAPPINGS.get(curr_item,0)+1
            pair_counter += 1
        else:
            points += POINT_MAPPINGS.get(curr_item,0)+1
            points += POINT_MAPPINGS.get(next_item,0)+1
            pair_counter += 1 
            

    assert pair_counter == int(n/2),f"Expected {n//2} pairs, got {pair_counter}"
    
    return points
 

def total_potions_needed(data: str) -> int:
    count = 0
    for i in data:
        if i == 'A':
            count += 0
        elif i == 'B':
            count += 1
        elif i == 'C':
            count += 3
    return count 

def main():
    print("----part1 solution------")
    with open('./notes.txt','r') as f:
        raw_data = f.read()

    data = raw_data.strip()

    print(total_potions_needed(data))
    print("\n-----part2 solution------")
    
    with open('./notes2.txt','r') as f:
        raw_data = f.read()
    data2 = raw_data.strip()
    print(diabolical_round2(data2))

if __name__ == '__main__':
    main() 
