import copy
from collections import defaultdict

def isUnique(s: str)-> bool:
    if len(s) ==1 :
        print ('ja gevonden')
        return True
    elif s[0] in s[1::]:
        return False
    else:
        return isUnique (s[1::])

def part_one(filename: str) -> str:
    with open(filename, "r", encoding="utf8") as f:
        signal = f.read()
    
    for i in range(0,len(signal)-4):
        start = i
        end = i+4
        tst_str = signal[start:end]
        if isUnique(tst_str):
            
            return end

def part_two(filename: str) -> str:
    with open(filename, "r", encoding="utf8") as f:
        signal = f.read()
    
    for i in range(0,len(signal)-4):
        start = i
        end = i+14
        tst_str = signal[start:end]
        if isUnique(tst_str):            
            return end


if __name__ == "__main__":
    input_path = "./2022/6/signal.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))