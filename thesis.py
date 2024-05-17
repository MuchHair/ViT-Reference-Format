# -*- coding: utf-8 -*-
"""
Created on Tue., Sep. 22(nd), 2020 at 20:45
@author: Zefeng Ding， Xubin Zhong
"""

import numpy as np
import os
import shutil
import numpy as np
import argparse

def get_args_parser():
    parser = argparse.ArgumentParser('Set path', add_help=False)
    parser.add_argument('--split_dir', type=str)

    return parser


def transform_format(thesis_out, split_dir, thesis_in):

    for file in thesis_in:
        f_read = open(f'{split_dir}/{file}', 'r')
        f_write = open(f'{thesis_out}/{file}', 'w+')

        infor_num = 0
        label = ''
        author = ''
        title = ''
        bo_jo = ''
        year = ''
        page = ''
        index = 1
        bib_list = []
        label_list = []
        line = f_read.readline()
        flag_A = False
        begin = True

        flag_article = 0
        flag_t = 0
        flag_author = 0
        flag_b = 0
        flag_y = 0
        flag_p = 0

        while line:
            if '@inproceedings' in line or '@InProceedings' in line:
                flag_article = 1

                infor_num += 1
                data_all = line.split('{')
                flag_A = True
                label = '@A' + '{' + data_all[-1]

            if '@article' in line or '@A' in line:
                flag_article = 1
                label = line

            if 'title' in line and 'book' not in line:

                if '[A]' not in line and flag_A:
                    data = line.split('}')
                    title = data[0] + '[A]' + '},'

                else:
                    title = line
                flag_t = 1

            if 'author' in line:

                flag_a = 1
                infor_num += 1
                authors = line
                flag_author = 1

            if 'booktitle' in line :
                bo_jo = line
                flag_b = 1

            if 'journal' in line:
                bo_jo = line
                flag_b = 1

            if 'year' in line:
                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                year = data + ':'
                flag_y = 1

            if 'page' in line:

                data = line.split('{')[1].split('}')[0]
                data0 = data.split('--')
                if len(data0)<2:
                    #print(data)
                    page = data0[0] + '-' + data0[0]

                else:
                    page = data0[0] + '-' + data0[1]
                flag_p = 1
            line = f_read.readline()

        if flag_t + flag_y + flag_author + flag_article + flag_b == 5:
            if '@article' in label or 'arXiv' in bo_jo:
                years = 'year = {'
                years += year.split(':')[0] + '},'
                pages = 'page ={' + page + '}'
                data = label + title + '\n' + authors + bo_jo + years + '\n' + pages + '\n' + '}'
            else:
                d = bo_jo.split('{')[-1]
                d = d.split('}')[0]
                years = 'year = {'
                years += d + '[C]. ' + year + page + '}'
                data = label + title + '\n' + authors + bo_jo + years + '\n' + '}'
            bib_list.append([-index, data])

        bib_list.sort(key=lambda x: x[0], reverse=True)
        for bib_len_i in range(len(bib_list)):
            f_write.write('\n')
            f_write.write(bib_list[bib_len_i][1])
            f_write.write('\n')
        f_read.close()
        f_write.close()


