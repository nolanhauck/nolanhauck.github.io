import os
import glob

def count_directories(folder_path):
    """Counts the number of directories in a given folder path.

    Args:
        folder_path: The path to the folder.

    Returns:
        The number of directories in the folder, or None if the path is invalid.
    """
    if not os.path.isdir(folder_path):
        return None
    
    count = 0
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            count += 1
    return count

def count_files(folder_path):
    """
    arg: path to a chapter folder

    returns: number of files in that folder
    """
    if not os.path.isdir(folder_path):
        return None
    
    count = 0
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            count += 1
        
    return count

def create_list_of_file_names(folder_path):
    """
    args: path to a chapter folder

    returns: list of names of files in the folder
    """

    if not os.path.isdir(folder_path):
        return None
    
    list_of_names = []

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            list_of_names.append(item[:-4])
    
    return list_of_names

def create_middle_lines(row_number, sortedlistoflistsofexercises, authors):
    links = []
    for x in (0,1,2):
        chapter_links = []
        for item in sortedlistoflistsofexercises[3*row_number + x]:
            chapter_links.append('                <a href="./files/Solutions/' + authors + '/Chapter ' + str(3*row_number + x + 1) + '/' + item + '">' + item[:-4] + '</a>\n')
        links.append(chapter_links)

    print(links)
    middle_lines = [
        '    <!--Chapter ' + str(3*row_number + 1) + ',' + str(3*row_number + 2) + ',' + str(3*row_number + 3) + '-->\n',
        '    <div class="row">\n',
        '        <!--Chapter ' + str(3*row_number + 1) + ' references-->\n',
        '        <div class="column">\n',
        '            <div id="header 2">\n',
        '                <h2 style="text-align: center;">\n',
        '                    Chapter ' + str(3*row_number + 1) + '\n',
        '                </h2>\n',
        '            </div>\n',
        '            <div id="links">\n'] + links[0] + [
        '            </div>\n',
        '        </div>\n',
        '        <!--Chapter ' + str(3*row_number + 2) + ' references-->\n',
        '        <div class="column">\n',
        '            <div id="header 2">\n',
        '                <h2 style="text-align: center;">\n',
        '                    Chapter ' + str(3*row_number + 2) + '\n',
        '                </h2>\n',
        '            </div>\n',
        '            <div id="links">\n'] + links[1] + [
        '            </div>\n',
        '        </div>\n',
        '        <!--Chapter '+ str(3*row_number + 3) + ' references-->\n',
        '        <div class="column">\n',
        '            <div id="header 2">\n',
        '                <h2 style="text-align: center;">\n',
        '                    Chapter ' + str(3*row_number + 3) + '\n',
        '                </h2>\n',
        '           </div>\n',
        '           <div id="links">\n'] + links[2] + [
        '           </div>\n',
        '        </div>\n',
        '    </div>\n'
    ]
    return middle_lines

def sort_key_exercises(filename):
    """
    Extracts a numerical value from the filename for sorting.
    Assumes filenames are like 'file 1-2.txt', 'file 1-7.txt', 'file 2-14.txt', etc.
    """
    try:
        return (int(filename.split(' ')[1].split('-')[0]),int(filename.split('-')[1].split('.')[0]))
    except (IndexError, ValueError):
        return -1  # Handle cases where the filename doesn't match the expected format

def sort_key_chapters(directoryname):
    """
    Extracts numerical value from the directoryname for sorting naturally.
    Assumes directory names are as 'Chapter 1', 'Chapter 4', etc.
    """
    try:
        return int(directoryname.split(' ')[1])
    except (IndexError, ValueError):
        return -1 # Handle cases where the directoryname doesn't match the expected format


def main():
    authors_of_book = input("authors of book? be very precise lol ")
    title_of_book = input("Title of book ")
    book_path = "C:/Users/nhauc/OneDrive/Documents/GitHub/nolanhauck.github.io/files/Solutions/" + authors_of_book

    chapters_list = glob.glob("Chapter *")
    for item in os.listdir(book_path):
        chapters_list.append(item)
    sorted_chapters_list = sorted(chapters_list, key=sort_key_chapters)
    print(sorted_chapters_list)

    list_of_lists_of_sorted_exercises = []

    for item1 in sorted_chapters_list:
        chapter_path = os.path.join(book_path, item1)
        files_list = glob.glob("Exercise *-*.typ")
        for item2 in os.listdir(chapter_path):
            files_list.append(item2)
        sorted_files_list = sorted(files_list, key=sort_key_exercises)
        list_of_lists_of_sorted_exercises.append(sorted_files_list)


    beginning_lines = [
        '<!DOCTYPE html>\n',
        '<link rel="stylesheet" href="styles.css">\n',
        '<html lang="en-US">\n',
        '<style>\n',
        '    h1 {\n',
        '        text-align: center;\n',
        '        font-size: 32px; \n',
        '        background-color: chocolate;\n',
        '    }\n',
        '    body {\n',
        '        background-color: #D9925F;\n',
        '    }\n',
        '    li a {\n',
        '        display: block;\n',
        '        text-align: center;\n',
        '    }\n',
        '</style>\n',
        '<body>\n',
        '    <div id="header 1">\n',
        '        <h1>\n',
        '            ' + title_of_book + ' by ' + authors_of_book + '\n',
        '        </h1>\n',
        '    </div>\n'
    ]
    ending_lines = [
        '    <div class="wrapper" id="navbar">\n',
        '        <ul class="nav-bar-ul">\n',
        '            <li><a href="./index.html">Home</a></li>\n',
        '        </ul>\n',
        '    </div>\n',
        '</body>\n',
        '<!--Footer-->\n',
        '<div>\n',
        '    <footer>\n',
        '        Views and opinion expressed here are entirely my own and are not intended to reflect on the University of Missouri.\n',
        '    </footer>\n',
        '</div>\n',
        '</html>'
    ]

    full_row_count, columns_in_last_row = divmod(count_directories(book_path),3)

    

    with open("test.html","w") as f:
        for line in beginning_lines:
            f.write(line)
        for x in range(full_row_count):
            for line in create_middle_lines(x, list_of_lists_of_sorted_exercises, authors_of_book):
                f.write(line)
        for line in ending_lines:
            f.write(line)
                
        # for line in ending_lines:
        #     f.write(line)



    

        


        
        
        
    
    
       
    
    
        
        
    

# 
#     
#     <!--Chapter 4,5,6-->
#     <div class="row">
#         <!--Chapter 4 references-->
#         <div class="column">
#             <div>
#                 <h2 style="text-align: center;">
#                     Chapter 4
#                 </h2>
#             </div>
#             <div>
#                nix
#             </div>
#         </div>
#         <!--Chapter 5 references-->
#         <div class="column">
#             <div>
#                 <h2 style="text-align: center;">
#                     Chapter 5
#                 </h2>
#             </div>
#             <div>
#                 nix
#             </div>
#         </div>
#         <!--Chapter 6 references-->
#         <div class="column">
#             <div>
#                 <h2 style="text-align: center;">
#                     Chapter 6
#                 </h2>
#             </div>
#             <div>
#                 nix
#             </div>
#         </div>
#     </div>

    












main()