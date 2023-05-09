import TextCompress as TextC
import sys

InputFile = sys.argv[2]
OutputFile = ""

if len(sys.argv) > 3 and sys.argv[3] == "-o":
    OutputFile = sys.argv[4]

if sys.argv[1] == "-c":
    if OutputFile == "":
        OutputFile = "out.z78"

    TextC.CompressFile(InputFile, OutputFile)

elif sys.argv[1] == "-x":
    if OutputFile == "":
        OutputFile = "out.txt"
 
    TextC.DecompressFile(InputFile, OutputFile)

else:
    print("Comando inexistente!")