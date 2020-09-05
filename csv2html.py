import csv
import sys
import re

if __name__ == "__main__":
    args = sys.argv

    input_path = ""
    output_path = ""

    # Parse command line arguments
    for i, arg in enumerate(args, 0):
        if arg == "-h":
            print("Usage: python ./csv2html.py -i infile.csv [options]...")
            print("")
            print("  -i input-path        input csv path")
            print("  [-o output-path]     output html path")
            print("  [-h]                 show this help")
            exit()
        elif arg == "-i":
            input_path = args[i + 1]
        elif arg == "-o":
            output_path = args[i + 1]
    
    if output_path == "":
        output_path = input_path[:-3] + "html"

    with open(input_path, "r", newline='') as csvFile:
        with open(output_path, "w",newline='') as htmlFile:
            csvName = re.search("[ \w-]+\.csv",input_path)

            htmlFile.write('<!DOCTYPE html>\n')
            htmlFile.write('<html lang="en">\n')

            htmlFile.write('<head>\n')
            htmlFile.write('<meta charset="UTF-8">\n')
            htmlFile.write('<title>')
            htmlFile.write(csvName.group())
            htmlFile.write('</title>\n')
            htmlFile.write('</head>\n\n')

            htmlFile.write('<body>\n')
            htmlFile.write('<h1>')
            htmlFile.write(csvName.group())
            htmlFile.write('</h1>\n')

            # Generate table
            htmlFile.write('<table border="1" rules="all">\n')
            csvInfo = csv.reader(csvFile)
            for csvRow in csvInfo:
                htmlFile.write('<tr>')
                for csvCell in csvRow:
                    htmlFile.write('<td>')
                    htmlFile.write(csvCell)
                    htmlFile.write('</td>')
                htmlFile.write('</tr>\n')
            htmlFile.write('</table>\n')

            htmlFile.write('</body>\n')
            htmlFile.write('</html>\n')