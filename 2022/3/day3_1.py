file1 = open('RS.txt', 'r')
Lines = file1.readlines()

def helft1 (input_str):
    x

def helf2 (input_str):
    helft = (input_str.length() / 2) - 1
    
    input_str[0:]


def get_priority(x: str) -> int:
    return ord(x) - ord("a") + 1 if x.islower() else ord(x) - ord("A") + 27

tot_value = 0

for line in Lines:
    
    #print (line)
    #print (len(line))
    # mysterie waarom dit voor de laatste regel een halve warade haalt - lijkt ergens een verborge character te zitten eof?
    helft = round (((len(line)- 1) / 2) )
    #print (helft)
    helft1 = line[0:int(helft)]
    helft2 = line[int(helft):]
    #print (helft1)
    #print (helft2)


    intersection = set(helft1).intersection(helft2)
    

    inter_str = ''.join(intersection)
    #print (inter_str)

    value = ord(inter_str)
    #print (value)
    # based on unicode set lowercase from 97-122 and upper case from 65 - 90
    if 122 > value > 97:
        value = value - 96
    elif 90 > value > 65:
        value = value - 38
    #print (value)
    

    tot_value = value + tot_value
    #print (tot_value)
    #print ('--')


print (tot_value)