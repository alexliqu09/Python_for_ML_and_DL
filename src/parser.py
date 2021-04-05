import numpy as np

import argparse

def tanh(x):
    return (np.exp(x) + np.exp(-x)) / (np.exp(x) - np.exp(-x))

def parser(funct):
    parser = argparse.ArgumentParser()
    parser.add_argument("argument", help = "If you wanr to compute the tanh we need you give a x parammeters", 
                        type = int)
    args = parser.parse_args()
    print(f"Your argument is: {args.argument} and the result is: {funct(args.argument)}")


if __name__=="__main__":
    parser(tanh)