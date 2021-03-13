#!/usr/bin/env python3

__author__ = 'Jake Miller (@LaconicWolf)'
__modified__ = "Michal Pielaszkiewicz (@yautay)"
__date__ = '20201206'
__version__ = '0.1'
__description__ = """Removes case, digits, and special characters for a wordlist
and uniques it for polish wordlists."""

import argparse
import os
from lib.parsers import WordParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="Specify a file containing words.")
    parser.add_argument("-o", '--outfile',
                        help="Writes the words to a specified outfile name")
    args = parser.parse_args()

    if not args.file and not args.outfile:
        parser.print_help()
        print(
            "\n[-] Please specify an input file containing words (-f) and the name of an output file to write to (-o out.txt).\n")
        exit()
    else:
        file = args.file
        outfile = args.outfile
        if not os.path.exists(file):
            print(
                "\n[-] The file cannot be found or you do not have permission to open the file. Please check the path and try again\n")
            exit()
        print('[*] Reading file: {}'.format(file))
        counter = 0
        out_file = open(outfile, 'w')
        with open(file, encoding='utf8', errors='ignore') as in_file:
            for line in in_file:
                if line.find(",") > 0:
                    words_in_line = line.split(",")
                    for word in words_in_line:
                        word = parsing_word(word)
                        counter += 1
                        out_file.write(word)

                else:
                    word = parsing_word(line)
                    counter += 1
                    out_file.write(word)
            print("[*] Collected {} words.".format(counter))


def parsing_word(word):
    parser = WordParser(word)
    parser.lowercase()
    parser.remove_signs(order="front")
    parser.substitute_spec_signs_with_()
    parser.unidecode_polish_ltrs()
    parser.rip_numbers()
    parser.remove_signs(order="reversed")
    return parser.word


if __name__ == '__main__':
    main()



