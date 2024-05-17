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

'''parser = get_args_parser()
args = parser.parse_args()

split_dir = args.split_dir
thesis_in = os.listdir(f'{split_dir}') # read dir
thesis_out = split_dir+'_out'

if not os.path.exists(thesis_out):
    os.mkdir(f'{thesis_out}')'''

def transform_format(thesis_out, split_dir, thesis_in):
    for file in thesis_in:
        f_read = open(f'{split_dir}/{file}', 'r')
        f_write = open(f'{thesis_out}/{file}', 'w+')
        index = 1
        infor_num = 0
        label = ''
        author = ''
        bib_list = []
        label_list = []
        title = ''
        bo_jo = ''
        year = ''
        line = f_read.readline()
        while line:
            if '@' in line:
                infor_num += 1
                data = line.split('{')[1][:-2]
                label = data
            elif ' title' in line:

                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                '''if data not in ['No-Frills Human-Object Interaction Detection: Factorization, Layout Encodings, and Training Techniques']:
                    continue'''
                title = data + '. '

            elif 'author' in line:
                # print(line)

                infor_num += 1
                data = line.split('{')[1][:-2]
                data = data.split('and')
                for i in range(len(data)):
                    data_i = data[i].split(',')
                    if i == (len(data) - 1):
                        try:
                            author = author + ' and ' + data_i[1][1] + '. ' + data_i[0].replace(' ', '')

                            author = author + '. '
                        except IndexError:
                            print(data_i)

                    else:
                        try:
                            author = author + data_i[1][1] + '. ' + data_i[0].replace(' ', '')
                            author = author + ', '
                        except IndexError:
                            print(data_i)

            elif ('booktitle' in line) or ('journal' in line) or ('publisher' in line and 'IEEE' not in line):
                infor_num += 1
                if 'Computer Vision and Pattern Recognition' in line or 'computer vision and pattern recognition' in line:
                    bo_jo = 'CVPR'
                elif 'European Conference on Computer Vision' in line or 'European conference on computer vision' in line or 'european conference on computer vision' in line or 'Proc. Eur. Conf. Comput. Vis' in line:
                    bo_jo = 'ECCV'
                elif 'International Conference on Computer Vision' in line or 'international conference on computer vision' in line:
                    bo_jo = 'ICCV'
                elif 'AAAI' in line:
                    bo_jo = 'AAAI'
                elif 'Winter Conference on Applications of Computer Vision' in line or 'winter conference on applications of computer vision' in line:
                    bo_jo = 'WACV'
                elif 'Transactions on Image Processing' in line or 'transactions on image processing' in line:
                    bo_jo = 'TIP'
                elif 'Neural Information Processing Systems' in line or 'neural information processing systems' in line:
                    bo_jo = 'NeurIPS'
                elif 'Transactions on Circuits and Systems for Video Technology' in line:
                    bo_jo = 'TCSVT'
                elif 'ACM international conference on Multimedia' in line or "ACM International Conference on Multimedia" in line:
                    bo_jo = 'ACM MM'
                else:
                    data = line.split('{')[1].split('}')[0]
                    bo_jo = data
            elif 'year' in line:
                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                year = data
            line = f_read.readline()
            if infor_num == 5:

                # if label in order:
                if label not in label_list:
                    label_list.append(label)
                    # index = order.index(label) + 1
                    if 'arXiv' in bo_jo:
                        data = '\\bibitem{' + label + '}\label{' + str(
                            index) + '}\n' + author + title + bo_jo + f' ({year})'
                    else:
                        data = '\\bibitem{' + label + '}\label{' + str(
                            index) + '}\n' + author + title + 'In: ' + bo_jo + f' ({year})'
                    bib_list.append([-index, data])
                index += 1
                infor_num = 0
                label = ''
                author = ''
                title = ''
                bo_jo = ''
                year = ''

        bib_list.sort(key=lambda x: x[0], reverse=True)
        for bib_len_i in range(len(bib_list)):
            f_write.write('\n')
            f_write.write(bib_list[bib_len_i][1])
            f_write.write('\n')
        f_read.close()
        f_write.close()
