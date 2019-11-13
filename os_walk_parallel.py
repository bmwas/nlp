import itertools
import multiprocessing
import os

def worker(j):
    return(j)   

def main():
    with multiprocessing.Pool(24) as pool: # pool with 24 processes.
        p="/home/xxxxxxxx/"
        walk = os.walk(p)
        fn_gen = itertools.chain.from_iterable((os.path.join(root, file)
                                                for file in files)
                                               for root, dirs, files in walk)
        results= pool.map(worker,[j for j in fn_gen])
        return results
        
output=main() # Output contains all files under the p directory. 
