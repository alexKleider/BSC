#!/usr/bin/env python3

# File: get_fields.py

"""
Reads the BR&BC contacts list and sends the list of 
keys to keys.csv

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                    restval='', extrasaction='ignore')
fieldnames:
First Name,Middle Name,Last Name,Phonetic First Name,Phonetic Middle Name,Phonetic Last Name,Name Prefix,Name Suffix,Nickname,File As,Organization Name,Organization Title,Organization Department,Birthday,Notes,Photo,Labels,E-mail 1 - Label,E-mail 1 - Value,E-mail 2 - Label,E-mail 2 - Value,Phone 1 - Label,Phone 1 - Value,Phone 2 - Label,Phone 2 - Value,Address 1 - Label,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address

The four that we use:
First Name,Last Name,E-mail 1 - Label,E-mail 1 - Value, 


"""

with open("/home/alex/Git/Sql/Secret/contacts.csv", 'r') as inf:
    keys = inf.readline()
with open("keys.csv", "w") as csvf:
    print(keys, file=csvf)


if __name__ == "__main__":
    print("Running contacts.py")
