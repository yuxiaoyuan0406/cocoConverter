import os
import cv2
import time
import argparse
import numpy as np

def path_check(path, name):
    assert os.path.exists(path), 'invalid {} path: {}'.format(name, path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt', type=str, default='',
                        help='Path to txt')
    parser.add_argument('--ratio', type=float, default=0.5,
                        help='split ratio')
    parser.add_argument('--out', type=str, default='out.txt',
                        help='Path to output file')
    opt = parser.parse_args()
    
    path_check(opt.txt, 'txt')
    
    try:
        os.makedirs(os.path.split(opt.out))
    except:
        pass
    
    assert not os.path.exists(opt.out), 'already exists: {}'.format(opt.out)
    
    f = open(opt.txt, 'rt')
    out = open(opt.out, 'wt')
    for line in f:
        if np.random.rand(1) < opt.ratio:
            out.write(line)
            
    f.close()
    out.close()
    
    
    
    
    
    
