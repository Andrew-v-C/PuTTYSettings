
import sys

def hexToRGB(str):
    r = int(str[1:3], 16)
    g = int(str[3:5], 16)
    b = int(str[5:7], 16)
    return f"{r},{g},{b}"

colour = "#000000"
colours = [colour for i in range(0, 22)]

input_file = open(sys.argv[1], "rt")

colour_type = "none"

for line in input_file:
    line = line.strip()

    if (len(line) > 0):
        if (line[0] == "["):
            if (line == "[colors.primary]"): colour_type = "default"
            elif (line == "[colors.cursor]"): colour_type = "cursor"
            elif (line == "[colors.normal]"): colour_type = "normal"
            elif (line == "[colors.bright]"): colour_type = "bold"
            else: colour_type = "none"
        else:
            temp = line.split("=")
            if (len(temp) >= 2): colour = temp[1].strip(" \"")
            line = line.split()[0]
            if (line == "foreground" and colour_type == "default"):
                colours[0] = colour  # Default Foreground
                colours[1] = colour  # Default Bold Foreground
            elif (line == "background" and colour_type == "default"):
                colours[2] = colour  # Default Background
                colours[3] = colour  # Default Bold Background
            elif (line == "text" and colour_type == "cursor"): colours[4] = colour  # Cursor Text
            elif (line == "cursor" and colour_type == "cursor"): colours[5] = colour  # Cursor Colour 
            elif (line == "black"):
                if (colour_type == "normal"): colours[6] = colour  # ANSI Black
                elif (colour_type == "bold"): colours[7] = colour  # ANSI Black Bold
            elif (line == "red"):
                if (colour_type == "normal"): colours[8] = colour  # ANSI Red
                elif (colour_type == "bold"): colours[9] = colour  # ANSI Red Bold
            elif (line == "green"):
                if (colour_type == "normal"): colours[10] = colour  # ANSI Green
                elif (colour_type == "bold"): colours[11] = colour  # ANSI Green Bold
            elif (line == "yellow"):
                if (colour_type == "normal"): colours[12] = colour  # ANSI Yellow
                elif (colour_type == "bold"): colours[13] = colour  # ANSI Yellow Bold
            elif (line == "blue"):
                if (colour_type == "normal"): colours[14] = colour  # ANSI Blue
                elif (colour_type == "bold"): colours[15] = colour  # ANSI Blue Bold
            elif (line == "magenta"):
                if (colour_type == "normal"): colours[16] = colour  # ANSI Magenta
                elif (colour_type == "bold"): colours[17] = colour  # ANSI Magenta Bold
            elif (line == "cyan"):
                if (colour_type == "normal"): colours[18] = colour  # ANSI Cyan
                elif (colour_type == "bold"): colours[19] = colour  # ANSI Cyan Bold
            elif (line == "white"):
                if (colour_type == "normal"): colours[20] = colour  # ANSI White
                elif (colour_type == "bold"): colours[21] = colour  # ANSI White Bold

input_file.close()

output = "\n"
output += "Windows Registry Editor Version 5.00\n"
output += "\n"
output += "[HKEY_CURRENT_USER\\Software\\SimonTatham\\PuTTY\\Sessions\\Default%20Settings]\n"
output += "\"Colour0\"=\""+hexToRGB(colours[0])+"\"\n"
output += "\"Colour1\"=\""+hexToRGB(colours[1])+"\"\n"
output += "\"Colour2\"=\""+hexToRGB(colours[2])+"\"\n"
output += "\"Colour3\"=\""+hexToRGB(colours[3])+"\"\n"
output += "\"Colour4\"=\""+hexToRGB(colours[4])+"\"\n"
output += "\"Colour5\"=\""+hexToRGB(colours[5])+"\"\n"
output += "\"Colour6\"=\""+hexToRGB(colours[6])+"\"\n"
output += "\"Colour7\"=\""+hexToRGB(colours[7])+"\"\n"
output += "\"Colour8\"=\""+hexToRGB(colours[8])+"\"\n"
output += "\"Colour9\"=\""+hexToRGB(colours[9])+"\"\n"
output += "\"Colour10\"=\""+hexToRGB(colours[10])+"\"\n"
output += "\"Colour11\"=\""+hexToRGB(colours[11])+"\"\n"
output += "\"Colour12\"=\""+hexToRGB(colours[12])+"\"\n"
output += "\"Colour13\"=\""+hexToRGB(colours[13])+"\"\n"
output += "\"Colour14\"=\""+hexToRGB(colours[14])+"\"\n"
output += "\"Colour15\"=\""+hexToRGB(colours[15])+"\"\n"
output += "\"Colour16\"=\""+hexToRGB(colours[16])+"\"\n"
output += "\"Colour17\"=\""+hexToRGB(colours[17])+"\"\n"
output += "\"Colour18\"=\""+hexToRGB(colours[18])+"\"\n"
output += "\"Colour19\"=\""+hexToRGB(colours[19])+"\"\n"
output += "\"Colour20\"=\""+hexToRGB(colours[20])+"\"\n"
output += "\"Colour21\"=\""+hexToRGB(colours[21])+"\"\n"
output += "\n"

output_file = open(sys.argv[1].split(".")[0] + "_PuTTY.reg", "w", encoding="utf-8")
output_file.write(output)
output_file.close()

