import numpy as np
import re

with open("input4.txt") as file:
    lines = file.readlines()
    matrix = [""]
    i = 0
    for line in lines:
        if line == "\n":
            i += 1
            matrix.append("")
        else:
            line = str.strip(line)
            matrix[i] += line + " "

print(len(matrix))
corr = 0
for pw in matrix:
    pwd = str.split(pw, " ")
    print(pwd)
    amcorr = 0
    for part in pwd:
        if "byr" in part:
            reg = re.search(r"byr:(\d\d\d\d)", pw)
            year = reg.group(1)
            if 1920 <= int(year) <= 2002:
                amcorr += 1
                print("byr")
        if "iyr" in part:
            reg = re.search(r"iyr:(\d\d\d\d)", pw)
            year = reg.group(1)
            if 2010 <= int(year) <= 2020:
                amcorr += 1
                print("iyr")
        if "eyr" in part:
            reg = re.search(r"eyr:(\d\d\d\d)", pw)
            year = reg.group(1)
            if 2020 <= int(year) <= 2030:
                amcorr += 1
                print("eyr")
        if "hgt" in part:
            reg = re.search(r"hgt:(\d*)([a-z]*)", pw)
            if reg is None:
                break
            num = reg.group(1)
            un = reg.group(2)
            if un == "cm":
                if 150 <= int(num) <= 193:
                    amcorr += 1
                    print("hgt1")
            if un == "in":
                if 59 <= int(num) <= 76:
                    amcorr += 1
                    print("hgt2")
        if "hcl" in part:
            reg = re.findall(r"hcl:#([0-9a-f]{6})", pw)
            if len(reg) == 1:
                amcorr += 1
                print("hcl")
        if "ecl" in part:
            reg = re.findall(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", pw)
            if len(reg) == 1:
                amcorr += 1
                print("ecl")
        if "pid" in part:
            reg = re.findall(r"pid:(\d{9})", pw)
            if len(reg) == 1:
                amcorr += 1
                print("pid")
    print(amcorr)
    if amcorr >= 7:
        corr += 1

print(corr)