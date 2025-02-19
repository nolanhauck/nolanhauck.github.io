import os

def create_exercise(chapnum, exnum, secnum):
    file_name = "Exercise " + str(secnum) + "-" + str(exnum) + ".typ"
    directory_path = 'C:/Users/nhauc/OneDrive/Documents/GitHub/nolanhauck.github.io/files/Solutions/Dummit and Foote/Chapter ' + str(chapnum)
    file_path = os.path.join(directory_path, file_name)
    source = [
        '#import "/files/Solutions/solutionstyle.typ"\n',
        '\n',
        '#show: solutionstyle.template.with(\n',
        '  book: "Abstract Algebra",\n',
        '  author: "Dummit and Foote",\n',
        '  chapter: ' + str(chapnum) + ',\n',
        '  section: ' + str(secnum) + ',\n',
        '  num: ' + str(exnum) + '\n',
        ')'
    ]
    with open(file_path, "w") as f:
        for line in source:
            f.write(line)



def main():
    cont = True
    while cont:
        chapternumber = input("Enter the chapter number of the files you want to create: ")
        sectionnumber = input("Enter the section number of the files you want to create: ")
        for x in range(1,int(input("Enter number of files to create: "))+1):
            create_exercise(chapternumber,x,sectionnumber) 

main()