#!/usr/bin/env python3

# File: v3.py

"""
Primary purpose is to take a google formated contacts.csv file and
output a "better4june.txt" file implemented as contacts2txt.py.

Also provides json_dump.py and to_csv.py
"""
import csv
import json

f_name = "forJune.data"
f_json = "junes.json"
contacts_file = "contacts.csv"  # must be imported or decrypted!!
better4june = "better4june.txt"


def google_keys():
    g1stline ="""
    First Name,Middle Name,Last Name,Phonetic First Name,Phonetic Middle Name,Phonetic Last Name,Name Prefix,Name Suffix,Nickname,File As,Organization Name,Organization Title,Organization Department,Birthday,Notes,Photo,Labels,E-mail 1 - Label,E-mail 1 - Value,E-mail 2 - Label,E-mail 2 - Value,Phone 1 - Label,Phone 1 - Value,Phone 2 - Label,Phone 2 - Value,Address 1 - Label,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address
    """
    return g1stline.strip().split(',')
    
field_names = ("First Name",      # keys June wants
               "Last Name",
               "E-mail 1 - Value" )


def json_dump(j_data, f_json):
    """
    Moves <j_data> (asumed to be a json
    compliant text file) to a json file.
    """
    with open(f_json, 'w') as jf:
        json.dump(j_data, jf, indent="  ")
    print(f"json data sent to {f_json}")


def to_csv(mappings, csv_file):
    """
    Appends data (a list of dicts)
    to an existing csv file.
    - json.load(s) string into json.
    - json.dump(s) json into string.
    """
    with open(csv_file, 'a', newline='') as outf:
        writer = csv.DictWriter(outf,
                        fieldnames=google_keys(),
                        lineterminator='\n')
        writer.writerows(mappings)
    print(f"Data appended to {csv_file}")


def contacts2text(gcsvf, output_file):
    """
    Input is a exported gmail contacts.csv file.
    <output_file> is a text file listing last, first
    and email fields, with an optional header.
    """
    ret = []
    with open(gcsvf, 'r') as inf:
        reader = csv.DictReader(inf, fieldnames=google_keys())
        for mapping in reader:
            new_dict = {}
            new_dict['first'] = mapping["First Name"]
            new_dict['last']= mapping["Last Name"]
            new_dict['email'] = mapping["E-mail 1 - Value"]
            ret.append(new_dict)
    print(f"Data collected from {gcsvf}")
    ret = ret[1:]
    ret.sort(key=lambda x: x['last'])
    with open(output_file, 'w') as outf:
        yn = input("Include a header? (y/n): ")
        if yn and yn[0] in "yY":
            print("""


    June's listing of Summer Camp Tea party invitees
    ================================================""",
                  file=outf)
        for item in ret:
             first = item['first']
             last = item['last']  + ","
             email = item['email']
             print(f"          {last:<15} {first:<10} {email:>29}",
                   file=outf)
    print(f"Data sent to {output_file}.")


if __name__ == "__main__":
    contacts2text("contacts.csv", better4june)
#   json_dump(j_data, f_json)
#   to_csv(j_data, contacts_file)

