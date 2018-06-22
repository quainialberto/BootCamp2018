class ContentFilter:
    """A ContentFilter object class.
    Attributes:
    name (str): name of the file.
    content (str): content of the file
    numlines (int): number of lines
    """
    def __init__(self, filename):             # This function is the constructor.
        """Set the file name and its content.  It will continue to run
        and ask for a valid name until you give a valid file name.
        Parameters:
        filename (str): the file name of a file to be read.
        """
        exists = False
        while not exists:
            try:
                with open(filename, 'r') as readfile:
                    exists = True
                    self.filename = filename
                    self.content = readfile.read()
                    self.numlines = len(readfile.readlines())
            except:
                filename = input("Please enter a valid file name: ")
        self.numchars = len(self.content)
        self.numalphas = sum(c.isalpha() for c in self.content)
        self.numdigits = sum(c.isdigit() for c in self.content)
        self.numspaces = sum(c.isspace() for c in self.content)

    def uniform(self, writefile, mode='w', case='upper'):
        """Method to save text in uppercase or lowercase to file.
        """
        valid = ['w', 'x', 'a']
        if mode not in valid:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        if case == 'upper':
            writethis = self.content.upper()
        elif case == 'lower':
            writethis = self.content.lower()
        else:
            raise ValueError("This is not a valid case.  Use upper or lower")
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def reverse(self, writefile, mode='w', unit='line'):
        """Method to reverse words or lines in text and save to file.
        """
        valid = {'w', 'x', 'a'}
        valid.add(mode)
        if len(valid) != 3:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        if unit == 'line':
            wordlist = self.content.split('\n')
            newwordlist = wordlist[::-1]
            writethis = "\n".join(newwordlist)
        elif unit == 'word':
            wordlist = self.content.split('\n')
            newwordlist = wordlist
            for i in range(len(wordlist)):
                newwordlist[i] = wordlist[i][::-1]
            writethis = "\n".join(newwordlist)
        else:
            raise ValueError("This is not a valid unit.  Use line or word")
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def transpose(self, writefile, mode='w'):
        """Method to transpose text and save it to a file.
        """
        valid = {'w', 'x', 'a'}
        valid.add(mode)
        if len(valid) != 3:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        lines = self.content.split('\n')
        matrix = []
        for i in range(len(lines)):
            matrix.append(lines[i].split(' '))
        matrix = [*zip(*matrix)]
        for j in range(len(matrix)):
            matrix[j] = " ".join(matrix[j])
        writethis = "\n".join(matrix)
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def __str__(self):
        """Magic method of printing the class object.  It prints a
        summary of the text.
        """

        string = str("Source File:\t\t\t" + str(self.filename) +
        "\nTotal characters:\t\t" + str(self.numchars) + "\nAlphabetic characters:\t\t" +
        str(self.numalphas) + "\nNumerical characters:\t\t" + str(self.numdigits) +
        "\nWhitespace characters:\t\t" + str(self.numspaces) +
        "\nNumber of lines:\t\t" + str(self.numlines))
        return string
