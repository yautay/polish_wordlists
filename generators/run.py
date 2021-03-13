from generators.dates_generator import DatesGenerator
from generators.hash_splitter import HashSplitter
from generators.length_cutter import LengthCutter
from generators.file_splitter import FileSplitter
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--file_in", required=False,
                        help="Specify a file containing words")
    parser.add_argument("-o", "--file_out", required=True,
                        help="Specify a output file")
    parser.add_argument("-g", "--generator", required=True,
                        help="Specify generator type")
    parser.add_argument("-s", "--date_start", required=False,
                        help="Specify start date in ddmmyyyy format")
    parser.add_argument("-e", "--date_end", required=False,
                        help="Specify end date in ddmmyyyy format")
    parser.add_argument("-f", "--format", required=False,
                        help="Specify format options")
    parser.add_argument("-d", "--delimiter", required=False,
                        help="Specify delimiter options")
    parser.add_argument("-min", "--minimum_length", required=False,
                        help="Specify minimum length of word")
    parser.add_argument("-max", "--maximum_length", required=False,
                        help="Specify maximum length or number of words")

    args = parser.parse_args()

    if args.generator == "date_generator":
        generator = DatesGenerator(start_date_ddmmyyyy=args.date_start,
                                   end_date_ddmmyyyy=args.date_end,
                                   _format=args.format,
                                   delimiter=args.delimiter,
                                   file_out=args.file_out
                                   )
    elif args.generator == "hash_splitter":
        generator = HashSplitter(file_in=args.file_in,
                                 file_out=args.file_out,
                                 separator=args.delimiter)
    elif args.generator == "word_cutter":
        generator = LengthCutter(file_in=args.file_in,
                                 file_out=args.file_out,
                                 minimum=args.minimum_length,
                                 maximum=args.maximum_length)
    elif args.generator == "file_splitter":
        generator = FileSplitter(file_in=args.file_in,
                                 file_out=args.file_out,
                                 maximum=args.maximum_length)
