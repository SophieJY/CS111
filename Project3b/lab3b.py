#!usr/local/cs/bin
import sys

def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        

if __name__ == '__main__':
    main()