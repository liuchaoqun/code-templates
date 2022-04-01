import argparse

parser = argparse.ArgumentParser(description='PyTorch Wikitext-2 RNN/LSTM/GRU/Transformer/FNN Language Model')
parser.add_argument('--data', type=str, default='./data/wikitext-2',
                    help='location of the data corpus')
parser.add_argument('--emsize', type=int, default=200,
                    help='size of word embeddings')
parser.add_argument('--sample', action='store_true',
                    help='try a small number of samples')

args = parser.parse_args()

print(args.data)
print(args.emsize)
print(args.sample)