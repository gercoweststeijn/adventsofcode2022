

def snafu2digital(s:str) -> int:
    snafu = s[::-1]
    ret_val= 0
    for i in range(len(snafu)):
        base_number = pow(5,i)
        if snafu[i] == '2':
            ret_val = ret_val+(2*base_number)
        elif snafu[i] == '1':
            ret_val = ret_val+(1*base_number)
        elif snafu[i] == '0':
            ret_val = ret_val+(0*base_number)
        elif snafu[i] == '-':
            ret_val = ret_val+(-1*base_number)
        elif snafu[i] == '=':
            ret_val = ret_val+(-2*base_number)
    return ret_val

def decimal2snafu(decimal: int) -> str:
    result = ""

    #
    # loop door het getal, we tellen, impliciet hoe vaak we door 5 kunnen delen >> dit id de lengte van de snafu (tot de macht 5)
    # 
    #
    while decimal != 0:
        # hoe past ie er in 
        remainder = decimal % 5        
        
        decimal = decimal // 5
        
        if remainder > 2:
            remainder -= 5
            decimal += 1
        match remainder:
            case 2:
                result = "2" + result
            case 1:
                result = "1" + result
            case 0:
                result = "0" + result
            case -1:
                result = "-" + result
            case -2:
                result = "=" + result
    return result


def part_one(filename: str) -> str:
    with open(filename, "r", encoding="utf8") as f:
        snafus = f.read().split("\n")
    
    total_digital = 0
    for snafu in snafus:
        total_digital = total_digital  + snafu2digital(snafu)

    return decimal2snafu(decimal=total_digital)

    



if __name__ == "__main__":
    input_path = "./2022/25/snafu.txt"
    print("---Part One---")
    print(part_one(input_path))

    #print("---Part Two---")
    #print(part_two(input_path))