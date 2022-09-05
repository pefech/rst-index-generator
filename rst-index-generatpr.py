import sys

def main():
    print("starting..")

    if(len(sys.argv) != 2):
        print("ERROR: No file given.")
        sys.exit(1)

    input_file = sys.argv[1]
    input_file = open(input_file, "r")

    output_file = open("output.rst", "w")

    lines = input_file.readlines()
    lines_count = len(lines)
    print("input file lines: " + str(lines_count))
    
    h1_count = 0
    h2_count = 0
    h3_count = 0
    h4_count = 0

    last_heading = 1

    try:
        for n in range(1, lines_count):
            thisLine = lines[n - 1].replace("\n", "")  # loading next and current Line
            nextLine = lines[n].replace("\n", "")      # to have heading type and name

            if nextLine == "": continue  # when line is empty, it would be recorgnised as heading
            
            if "*" in thisLine: thisLine = thisLine.replace("*", "")

            # check if the characters are all the same, if so there is likely a heading
            if(nextLine == len(nextLine) * nextLine[0]):
                
                if nextLine[0] == "=":
                    # h1
                    print("h1")
                    h1_count = h1_count + 1
                    output_file.write("-  " + str(h1_count) + " `" + thisLine + "`_\n")  # writing heading link

                    h2_count = 0  # resetting heading counts 
                    h3_count = 0
                    h4_count = 0

                    last_heading = 1

                elif nextLine[0] == "-":
                    # h2
                    print("h2")
                    h2_count = h2_count + 1

                    firstchar = ""
                    if(last_heading < 2): firstchar = "\n"

                    output_file.write(firstchar + "   -  " + str(h1_count) + "." + str(h2_count) + " `" + thisLine + "`_\n")  # writing heading link

                    h3_count = 0  # resetting heading counts
                    h4_count = 0
                    last_heading = 2

                elif nextLine[0] == "~":
                    # h3
                    print("h3")
                    h3_count = h3_count + 1

                    firstchar = ""
                    if(last_heading < 3): firstchar = "\n"

                    output_file.write(firstchar + "      -  " + str(h1_count) + "." + str(h2_count) + "." + str(h3_count) + " `" + thisLine + "`_\n")  # writing heading link
                    
                    h4_count = 0  # resetting heading count
                    last_heading = 3

                elif nextLine[0] == "^":
                    # h4
                    print("h4")
                    h4_count = h4_count + 1

                    firstchar = ""
                    if(last_heading < 4): firstchar = "\n"

                    output_file.write(firstchar + "         -  "  + str(h1_count) + "." + str(h2_count) + "." + str(h3_count) + "." + str(h4_count) + " `" + thisLine + "`_\n")  # writing heading link
                    
                    last_heading = 4
                # when the detected heading isn't a real heading, skip it
                else:
                    continue

    except IndexError:
        print("end of file.. finishing..")

    except:
        print("unexpected error occured. Stopping..")
        sys.exit(1)

    finally:
        input_file.close()
        output_file.close()

        print("finished! Output is in output.rst")


if __name__ == "__main__":
        main()