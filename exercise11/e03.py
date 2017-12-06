"""Download the file “NumberSum.txt” from the Google Classroom. Write a code that opens
the file “NumberSum.txt”. It contains all numbers from 0 to 999 (one number per line). Read
in each line and add them all up. Display your result. Remember to add an error exception."""



def file_to_list(filename):
    "Receives a filename and returns a list of the lines in that file"
    my_list = []
    try:
        my_file = open(filename, 'r')
    except IOError:
        print('Error, cannot open file')
    else:
        for line in my_file:
            my_list.append(int(line))
        my_file.close()
    return my_list

def addup_list(inputlist):
    "Receives a list of numbers and totals up all the lines"
    total = 0
    for i in inputlist:
        total += inputlist[i]
    return total

def main():
    "Execute the program"
    main_list = file_to_list("NumberSum.txt")
    main_total = addup_list(main_list)
    print("Sum of all numbers is {0}".format(main_total))
    return

main()
