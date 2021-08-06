# Importing another file and running its function indirectly.

## Importing the module makes the imported file run entirely, using __name__ as the name of that file being imported.

print(__name__)                                             # currently it is __main__ for this file
import module                                               # __name__ becomes 'module' as soon as the file is imported

print("This is the first line of import file.")

# module.main()                                               # to run that main function in the other file explicitly