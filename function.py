def openFile(filename):
    with open(filename, "r") as file:
        file_contents = file.read()
    return file_contents

