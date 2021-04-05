import argparse

def my_decorator(func):
    def change_data():
        print("============Training Model==========")
        args  = func().parse_args()
        print(f"           model:{args.model}" )
        print(f"           batch_size: {args.batch_size}")
        print(f"           epoch: {args.epoch}")
        print(f"           input_nc: {args.input_nc}")
        print(f"           lr_decay: {args.lr_decay}")
        print(f"           gpu_is: {args.gpu_is}")
        print("------------------------------------")
    return change_data

@my_decorator
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr_decay", default = None, help = "learning rate decay", 
                        type = int)
    parser.add_argument("--batch_size", default = 1, help ="Input Batch size", 
                        type = int)
    parser.add_argument("--epoch", default = 100, type = int, help = "which epoch to load?")
    parser.add_argument("--gpu_is", default = '0', type = str, help = "gpu:0, cpu: -1")
    parser.add_argument("--input_nc", default = 3, type=int, help = "channel of color")
    parser.add_argument("--model", default ="my_model", type = str, help = "Change the model")
    
    return parser

if __name__=="__main__":
    parser()