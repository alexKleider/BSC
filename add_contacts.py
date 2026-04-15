#!/usr/bin/env python3

# File: add_contacts.py

"""
Insert new values into a gmail compliant contacts.csv vile.

Relevant field names which are used:
First Name, Last Name, E-mail 1 - Value, 
"""

import csv

csvf = "bsc.csv"

g_field_names = (   # keys used by google's csv contacts listing
"First Name","Middle Name","Last Name","Phonetic First Name",
"Phonetic Middle Name","Phonetic Last Name","Name Prefix",
"Name Suffix","Nickname","File As","Organization Name",
"Organization Title","Organization Department","Birthday",
"Notes","Photo","Labels","E-mail 1 - Label","E-mail 1 - Value",
"E-mail 2 - Label","E-mail 2 - Value","Phone 1 - Label",
"Phone 1 - Value","Phone 2 - Label","Phone 2 - Value",
"Address 1 - Label","Address 1 - Formatted","Address 1 - Street",
"Address 1 - City","Address 1 - PO Box","Address 1 - Region",
"Address 1 - Postal Code","Address 1 - Country",
"Address 1 - Extended Address", )

def manual_insert(csvf):
    """
    Provides ability to mannually add entries [*]
    to a gmail compliant contacts csv file <csvf>.
    Still ToDo:
    If the file doesn't exist, create one.
    [*] only first and last names and emails
    are included.
    """
    with open(csvf, 'r') as getter:
        keys = getter.readline().split(',')
        fieldnames = [f"{key}" for key in keys]
    with open(csvf, "a", newline='') as outf:
        writer = csv.DictWriter(outf,
                        fieldnames=fieldnames,
                        lineterminator='\n')
        while True:
            first = input("First name: ")
            last = input("Last name: ")
            email = input("email: ")
            if not first:
                break
            else:
                writer.writerow({'First Name':first,
                                 'Last Name':last,
                             'E-mail 1 - Value':email,
                                 })


if __name__ == "__main__":
    insert(csvf)
