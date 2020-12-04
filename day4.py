from enum import Enum
import re


class PassportField(Enum):
    BYR = 'byr'  # Birth Year
    IYR = 'iyr'  # Issue Year
    EYR = 'eyr'  # Expiration Year
    HGT = 'hgt'  # Height
    HCL = 'hcl'  # Hair Color
    ECL = 'ecl'  # Eye Color
    PID = 'pid'  # Passport ID
    CID = 'cid'  # Country ID


all_available_passport_fields: set = {field.value for field in PassportField}
optional_passport_fields: set = {PassportField.CID.value}
required_passport_fields: set = all_available_passport_fields - optional_passport_fields


class HeightUnit(Enum):
    CM = 'cm'
    IN = 'in'


class EyeColor(Enum):
    AMB = 'amb'
    BLU = 'blu'
    BRN = 'brn'
    GRY = 'gry'
    GRN = 'grn'
    HZL = 'hzl'
    OTH = 'oth'


def validate_number_range(value: str, max_num: int, min_num: int,) -> bool:
    if value.isdigit():
        num = int(value)
        return max_num >= num >= min_num
    else:
        return False


def validate_byr(value: str) -> bool:
    return validate_number_range(value, 2002, 1920)


def validate_iyr(value: str) -> bool:
    return validate_number_range(value, 2020, 2010)


def validate_eyr(value: str) -> bool:
    return validate_number_range(value, 2030, 2020)


def validate_hgt(value: str) -> bool:
    unit = value[-2:]
    if unit == HeightUnit.CM.value:
        return validate_number_range(value[:-2], 193, 150)
    elif unit == HeightUnit.IN.value:
        return validate_number_range(value[:-2], 76, 59)
    else:
        return False


def validate_hcl(value: str) -> bool:
    return bool(re.search("^#[a-f0-9]{6}$", value))


def validate_ecl(value: str) -> bool:
    return value in [color.value for color in EyeColor]


def validate_pid(value: str) -> bool:
    return len(value) == 9 and value.isdigit()


def validate_cid(value: str) -> bool:
    return True


field_validators = {
    PassportField.BYR.value: validate_byr,
    PassportField.IYR.value: validate_iyr,
    PassportField.EYR.value: validate_eyr,
    PassportField.HGT.value: validate_hgt,
    PassportField.HCL.value: validate_hcl,
    PassportField.ECL.value: validate_ecl,
    PassportField.PID.value: validate_pid,
    PassportField.CID.value: validate_cid,
}


def have_required_fields(passport: dict) -> bool:
    passport_fields = set(passport.keys())
    return passport_fields - optional_passport_fields == required_passport_fields


def validate_passport(passport: dict) -> bool:
    if not have_required_fields(passport):
        return False

    field_validation_results = [
        field_validators[key](value)
        for key, value in passport.items()
    ]

    return all(field_validation_results)


def extract_passports(lines: list[str]) -> list[dict]:
    passport = {}
    passports = []
    for line in lines:
        if passport and not line:
            passports.append(passport)
            passport = {}
        else:
            fields = line.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport.update({key: value})
    if passport:
        passports.append(passport)

    return passports


def part1(passports):
    count = 0
    for passport in passports:
        if have_required_fields(passport):
            count += 1
    return count


def part2(passports):
    count = 0
    for passport in passports:
        if validate_passport(passport):
            count += 1
    return count


with open('day4-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part1(extract_passports(inputs)))
    print(part2(extract_passports(inputs)))
