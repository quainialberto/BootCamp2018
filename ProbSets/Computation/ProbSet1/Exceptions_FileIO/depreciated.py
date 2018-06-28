class ContentFilter:
    """A ContentFilter object class. Opens a file and records it's name and content.
    Attributes:
        name (str): name of the file.
        content (str): content of the file
    """
    def __init__(self, file_in):
        """Open and read a file.
         Parameters:
             name (str): name of the file.
             content (str): content of the file.
         """
        file_exists = False
        while not file_exists:
            try:
                with open(file_in, 'r') as file_chosen:
                    file_exists = True
                    self.name = file_in
                    self.content = file_chosen.read()
            except:
                file_in = input("Please enter a valid file name (hint: use 'text.txt'): ")
    def uniform(self, file_out, mode = 'w', case = 'upper'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("'mode' must be either 'w', 'x' or 'a'.")
        if case == "upper":
            text = self.content.upper()
        elif case == "lower":
            text = self.content.lower()
        else:
            raise ValueError("'case' must be either 'upper' or 'lower'.")
        with open(file_out, mode) as outfile:
            outfile.write(text)
    def reverse(self, file_out, mode = 'w', unit = 'line'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("'mode' must be either 'w', 'x' or 'a'.")
        if unit == 'line':
            wordlist = self.content.split('\n')
            wordlist = wordlist[::-1]
            text = '\n'.join(wordlist)
        elif unit == 'word':
            wordlist = self.content.split('\n')
            wordlist2 = wordlist
            for i in range(len(wordlist)):
                wordlist2[i] = wordlist[i][::-1]
            text = '\n'.join(wordlist2)
        else:
             raise ValueError("'mode' must be either 'w', 'x' or 'a'.")
        with open(file_out, mode) as outfile:
            outfile.write(text)
    def transpose(self, file_out, mode = 'w'):
        if mode not in ['w', 'x', 'a']:
             raise ValueError("'mode' must be either 'w', 'x' or 'a'.")
        wordlist = self.content.split('\n')
        matrix = []
        for i in range(len(wordlist)):
            matrix.append(wordlist[i].split(' '))
        matrix = [*zip(*matrix)]
        for i in range(len(matrix)):
            matrix[i] = ' '.join(list(matrix[i]))
        text = '\n'.join(matrix)
        with open(file_out, mode) as outfile:
            outfile.write(text)
    def __str__(self):


        print(matrix)




ContentFilter("test.txt")
print(ContentFilter("text.txt").name)
print(ContentFilter("text.txt").content)
ContentFilter("text.txt").uniform("uniform_text.txt")
ContentFilter("text.txt").reverse("reverse_text.txt")
ContentFilter("text.txt").transpose("transposed_text.txt")
