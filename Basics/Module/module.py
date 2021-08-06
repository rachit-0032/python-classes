# Understanding __name__

## When a Python file is run, __name__ contains __main__ in case it is being run directly.
## However, if the file is run from another file by importing it, then __name__ contains the name of this file that is being run.
## Thus, sometimes, it is preferred to write the piece of code in line 13-14, to ensure that something is run only if file is run directly.

print("This is the first line of the Module file being called from", __name__)

def main():
    print("This is the main funciton being called directly!")

# Ensures that this part of the code is run only when the file is being run directly and not from any other file using the import functionality.
if __name__ == '__main__':
    main()