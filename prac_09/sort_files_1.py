import os
import shutil


def main():
    os.chdir('')
    os.mkdir('Module')
    # for filenames in os.walk('.'):
    #     print("(Current working directory is: {})".format(os.getcwd()))
    #     print("\tand files:", filenames)
    for filename in os.listdir("."):
        if filename.endswith('.pptx'):
            shutil.move(filename, 'Lecture')


main()
