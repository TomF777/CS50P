# Uses command-line argument with argument parsing

import argparse

parser = argparse.ArgumentParser(description="Sending Hello Message")
parser.add_argument("-n", default=1, help="number of messages to send", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("hello")
