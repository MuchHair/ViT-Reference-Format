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

        flag_f = 0
        flag_t = 0
        flag_a = 0
        flag_b = 0
        flag_y = 0
        flag_p = 0
        while line:


            if '@' in line:
                flag_f += 1
                infor_num += 1
                data = line.split('{')[1][:-2]
                label = data
            elif ' title' in line:
                flag_t = 1
                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                '''if data not in ['No-Frills Human-Object Interaction Detection: Factorization, Layout Encodings, and Training Techniques']:
                    continue'''
                title = data + '. '

            elif 'author' in line:
                # print(line)
                flag_a = 1
                infor_num += 1
                data = line.split('{')[1][:-2]
                data = data.split('and')
                for i in range(len(data)):
                    data_i = data[i].split(',')
                    if i == (len(data) - 1):
                        try:
                            author = author + ' and ' +  data_i[1][1] + '. ' + data_i[0].replace(' ', '')

                            author = author + '. '
                        except IndexError:
                            print(data_i)

                    else:
                        try:
                            author = author +  data_i[1][1] + '. ' + data_i[0].replace(' ', '')
                            author = author + ', '
                        except IndexError:
                            print(data_i)

            elif ('booktitle' in line) or ('journal' in line) or ('publisher' in line and 'IEEE' not in line):
                flag_b =1
                infor_num += 1
                if 'Computer Vision and Pattern Recognition' in line or 'computer vision and pattern recognition' in line:
                    bo_jo = 'Proc. IEEE Conf. Comput. Vis. Pattern Recog. (CVPR)'
                elif 'European Conference on Computer Vision' in line or 'European conference on computer vision' in line or 'Eeuropean conference on computer vision' in line or 'Proc. Eur. Conf. Comput. Vis' in line or 'ECCV' in line :
                    bo_jo = 'Proc. Eur. Conf. Comput. Vis. (ECCV)'
                elif 'International Conference on Computer Vision' in line or 'international conference on computer vision' in line:
                    bo_jo = 'Proc. IEEE Int. Conf. Comput. Vis. (ICCV)'
                elif 'International Conference on Learning Representations' in line or 'international conference on learning representations' in line or 'International conference on machine learning' in line:
                    bo_jo = 'Proc. Int. Conf. Learn. Represent. (ICLR)'
                elif 'International Journal of Computer Vision' in line:
                    bo_jo = 'Int. J. Comput. Vis. (IJCV)'
                elif 'AAAI' in line:
                    bo_jo = 'AAAI'
                elif 'Winter Conference on Applications of Computer Vision' in line or 'winter conference on applications of computer vision' in line:
                    bo_jo = 'WACV'
                elif 'Transactions on Image Processing' in line or 'transactions on image processing' in line:
                    bo_jo = 'TIP'
                elif 'Neural Information Processing Systems' in line or 'neural information processing systems' in line:
                    bo_jo = 'Proc. Adv. Neural Inf. Process. Syst. (NeurIPS)'
                elif 'Transactions on Circuits and Systems for Video Technology' in line:
                    bo_jo = 'TCSVT'
                elif 'ACM international conference on Multimedia' in line or "ACM International Conference on Multimedia" in line:
                    bo_jo = 'Proc. ACM Int. Conf. Multimedia'
                else:
                    data = line.split('{')[1].split('}')[0]
                    bo_jo = data
            elif 'year' in line:
                flag_y =1
                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                year = data + '.'

            elif 'page' in line:
                flag_p = 1
                infor_num += 1
                data = line.split('{')[1].split('}')[0]
                page = data + '. '

            line = f_read.readline()
            if infor_num >=4 and (flag_f ==1 and flag_a ==1 and flag_b ==1) and ('@' in line or line ==''):

                # if label in order:
                if label not in label_list:
                    label_list.append(label)
                    #index = order.index(label) + 1
                    if flag_p ==1 and flag_y ==1:
                        data = '\\bibitem{' + label + '}\label{' + str(
                        index) + '}\n' + author + title + 'In  ' + bo_jo + ', ' + 'pp. ' + page + year
                    elif flag_p ==1 :
                        data = '\\bibitem{' + label + '}\label{' + str(
                        index) + '}\n' + author + title + 'In  ' + bo_jo + ', ' + 'pp. ' + page
                    elif  flag_y ==1:
                        data = '\\bibitem{' + label + '}\label{' + str(
                        index) + '}\n' + author + title + 'In  ' + bo_jo + ', ' + year
                    else:
                        data = '\\bibitem{' + label + '}\label{' + str(
                        index) + '}\n' + author + title + 'In  ' + bo_jo
                    bib_list.append([-index, data])
                index += 1
                infor_num = 0
                label = ''
                author = ''
                title = ''
                bo_jo = ''
                year = ''
                flag_f = 0
                flag_t = 0
                flag_a = 0
                flag_b = 0
                flag_y = 0
                flag_p = 0
            elif flag_f >1:
                print(flag_f ,flag_a , flag_b ,"error")
                assert 0


        bib_list.sort(key=lambda x: x[0], reverse=True)
        for bib_len_i in range(len(bib_list)):
            f_write.write('\n')
            f_write.write(bib_list[bib_len_i][1])
            f_write.write('\n')
        f_read.close()
        f_write.close()
