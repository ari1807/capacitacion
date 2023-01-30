
def convert_number(num = None):
    """ Esta función convierte el número pasado por parámetro en un string de números mostrados por display"""
    
    if num == None:
        return ""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    for x in str(num):
        if (x == "0"):
            line_1 += " _ "
            line_2 += "| |"
            line_3 += "|_|"
        elif (x == "1"):
            line_1 += "   "
            line_2 += "  |"
            line_3 += "  |"
        elif (x == "2"):
            line_1 += " _ "
            line_2 += " _|"
            line_3 += "|_ "
        elif (x == "3"):
            line_1 += " _ "
            line_2 += " _|"
            line_3 += " _|"
        elif (x == "4"):
            line_1 += "   "
            line_2 += "|_|"
            line_3 += "  |"
        elif (x == "5"):
            line_1 += " _ "
            line_2 += "|_ "
            line_3 += " _|"
        elif (x == "6"):
            line_1 += " _ "
            line_2 += "|_ "
            line_3 += "|_|"
        elif (x == "7"):
            line_1 += " _ "
            line_2 += "  |"
            line_3 += "  |"
        elif (x == "8"):
            line_1 += " _ "
            line_2 += "|_|"
            line_3 += "|_|"
        else:
            line_1 += " _ "
            line_2 += "|_|"
            line_3 += " _|"
    return line_1 + "\n" + line_2 + "\n" + line_3

    