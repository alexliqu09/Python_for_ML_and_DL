import numpy as np

import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", default = "sigmoid", help = "activation fuction", 
                        type = str)
    parser.add_argument("value", default = 1, help ="value to function", 
                        type = int)
    return parser

if __name__ == "__main__":
    pars = parser()

    args = pars.parse_args()

    if args.function == "tanh":
        list_ = np.array(args.value)

        tanh = lambda x: (np.e**(x)-np.e**(-x))/(np.e**(-x)+np.e**(x))
        print(tanh(list_))

    
    elif args.function == "sigmoid":
        args.value = np.array(args.value)
        sigmoide  =  (lambda x: 1/(1+np.e**(-x)),
              lambda x: x*(1-x))

        print(sigmoide[0](args.value))

    elif args.function == "relu":
        args.value = np.array(args.value)
        relu = lambda x: np.maximum(0, x)
        print(relu(args.value))