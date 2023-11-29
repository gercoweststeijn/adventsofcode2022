def decimal_to_snafu(decimal: int) -> str:
    result = ""
    while decimal != 0:
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


print (decimal_to_snafu(12))