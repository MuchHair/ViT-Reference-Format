import numpy as np
import os
import shutil
import numpy as np
import argparse
# input .bib file

#split_dir = 'ijcv'


def get_args_parser():
    parser = argparse.ArgumentParser('Set path', add_help=False)
    parser.add_argument('--input_bib',  type=str)
    parser.add_argument('--split_dir', type=str)

    return parser


parser = get_args_parser()
args = parser.parse_args()
split_dir = args.split_dir
input_bib = args.input_bib

f_read = open(f'{input_bib}', 'r')
line = f_read.readline()

if not os.path.exists(split_dir):
    os.mkdir(f'{split_dir}')


def write_bib(file_name, content):
    f_write = open(f"{split_dir}/{file_name}.txt", 'w+')
    f_write.write(content)
    f_write.close()

content = ''
begin = True
index = 1

while line:
    if '@' in line:
        if not begin:
            file_name = str(index).zfill(3)
            write_bib(file_name, content)
            content = ''
            index += 1
        else:
            begin = False
        content += line
    else:
        content += line

    line = f_read.readline()

file_name = str(index).zfill(3)
write_bib(file_name, content)