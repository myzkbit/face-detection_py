import math
import sys
import os

def main():
  # val = float(sys.argv[1])
  # print(math.radians(val))
  current_directory = os.getcwd()
  print("カレントディレクトリのパス:", current_directory)

if __name__ == "__main__":
  main()