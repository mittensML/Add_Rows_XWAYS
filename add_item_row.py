#This script takes an export list from XWAYS in HTML and adds row lines
__author__ = 'Matthew Loschmann'
#email: matt.loschmann@gmail.com
#Tested on XWAYS 19.6 Preview 5

import sys
import os
import ntpath

line_num = 1
fileno = ""
filecnt = 1

suffix = '.html'
new_suffix = ''

if len(sys.argv) != 3:
    print "This script takes an export list from XWAYS in HTML and adds row numbers."
    print "Usage: add_item_row.py <infile.html> <outfile.html>"
else:
    in_file = str(sys.argv[1])
    out_file = str(sys.argv[2])

    #print ntpath.basename(out_file)

    while (os.path.isfile(in_file)):

        f = open (in_file, "r")
        f_new = open (out_file, "w")
        print "Writing {}. Please wait.".format (out_file)

        for x in range (0, 7):
            str_line = f.readline()
            f_new.write(str_line)

        f_new.write("<th>#</th>\n")

        while "</tr><tr>" not in str_line:
            str_line = f.readline()
            f_new.write(str_line)

        f_new.write("<td valign=\"top\">" + str(line_num)+"</td>")
        str_line = ""

        while "</html>" not in str_line:
            while "</tr>" not in str_line:
                str_line = f.readline()
                f_new.write(str_line)

            str_line = f.readline()

            if "</html>" not in str_line:
                f_new.write(str_line)
                line_num = line_num + 1
                f_new.write("<td valign=\"top\">" + str(line_num) + "</td>\n")
            else:

                filecnt = filecnt+1
                line_num = line_num + 1

                new_suffix = " " + str(filecnt) + ".html"
                in_file = in_file.replace(suffix, new_suffix)
                out_file = out_file.replace(suffix, new_suffix)
                suffix = new_suffix
                str_line = str_line.replace(ntpath.basename(in_file),ntpath.basename(out_file))
                f_new.write(str_line)

    f.close()
    f_new.close()