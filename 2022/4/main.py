

def part_one(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        pairs = f.read().strip().split("\n")


    count = 0
    for pair in pairs:
        #print (pair)
        list_pair = pair.split(',')
        left_low = int(list_pair[0].split('-')[0])
        left_high = int(list_pair[0].split('-')[1])
        right_low = int(list_pair[1].split('-')[0])
        right_high = int(list_pair[1].split('-')[1])
        
        #print(left_low)
        #print(left_high)
        #print(right_low)
        #print(right_high)
        
        if ((left_low >= right_low) and (left_high <= right_high)):
            count = count + 1
            #print ('dze1')
            #print (pair)
        elif ((right_low >= left_low) and (right_high <= left_high)):
            
            count = count + 1
            #print ('dze2')
            #print (pair)

    return count
            
def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        pairs = f.read().strip().split("\n")


    count = 0
    for pair in pairs:
        #print (pair)
        list_pair = pair.split(',')
        left_low = int(list_pair[0].split('-')[0])
        left_high = int(list_pair[0].split('-')[1])
        right_low = int(list_pair[1].split('-')[0])
        right_high = int(list_pair[1].split('-')[1])
        
        #print(left_low)
        #print(left_high)
        #print(right_low)
        #print(right_high)
        
        # if left_low <= right_low and 

        if ((left_low >= right_low) and (left_high <= right_high)):
            count = count + 1
            #rint ('dze1')
            #print (pair)
        elif ((right_low >= left_low) and (right_high <= left_high)):
            
            count = count + 1
            #print ('dze2')
            #print (pair)

        elif left_high >= right_low and left_high <=right_high:

            count = count + 1
            #print ('dze3')
            #print (pair)

        elif right_high >= left_low and right_high <=left_high:

            count = count + 1
            #print (pair)


       
        #print ('------------')
    return count


if __name__ == "__main__":
    input_path = "./2022/4/assignments.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
    