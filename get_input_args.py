import argparse

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--throw', type = str, default='dice_throw.py',
                        help = 'path to the dice throw function')
    parser.add_argument('--prison', type = str, default = 'out_of_prison.py',
                        help = 'path to the out of prison function')
    parser.add_argument('--question', type = str, default = 'free_or_prison.py',
                        help = 'path to the free or prison question function')
    return parser.parse_args()
