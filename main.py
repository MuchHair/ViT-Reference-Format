import numpy as np
import os
import shutil
import numpy as np
import argparse

def get_args_parser():

    parser = argparse.ArgumentParser('Set path', add_help=False)
    parser.add_argument('--split_dir', type=str)
    parser.add_argument('--format', type=str, required=True)
    return parser

if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args()

    split_dir = args.split_dir
    thesis_in = os.listdir(f'{split_dir}') # read dir
    thesis_out = split_dir+'_out'

    if not os.path.exists(thesis_out):
        os.mkdir(f'{thesis_out}')

    if args.format=='eccv':
        from ECCV import transform_format
    elif args.format =='cvpr':
        from CVPR import transform_format
    elif args.format == 'nips':
        from CVPR import transform_format
    elif args.format=='ijcv':
        from IJCV import transform_format
    else:
        assert False
    transform_format(thesis_out, split_dir, thesis_in)
