import numpy as np
import os
import shutil
import numpy as np
import argparse

def get_args_parser():
    parser = argparse.ArgumentParser('Set path', add_help=False)
    parser.add_argument('--thesis_out', type=str)
    parser.add_argument('--out_file', type=str)
    return parser

parser = get_args_parser()
args = parser.parse_args()

bib_list = []
thesis_out = os.listdir(os.getcwd()+'/'+f'{args.thesis_out}') # read dir
f_write = open(os.getcwd()+'/'+f'{args.out_file}', 'w+')
index = 1


for i in range(len(thesis_out)):
    file = f'{i+1}'.zfill(3) + '.txt'
    print(os.getcwd()+'/'+f'{args.thesis_out}/{file}')
    f_read = open(os.getcwd()+'/'+f'{args.thesis_out}/{file}', 'r')

    lines = f_read.readlines()
    data = ''

    for line in lines:
        data += line

    index += 1
    f_read.close()

    bib_list.append([-index, data])

bib_list.sort(key=lambda x: x[0], reverse=True)
for bib_len_i in range(len(bib_list)):
    print(bib_list[bib_len_i][1])
    f_write.write(bib_list[bib_len_i][1])

f_write.close()
