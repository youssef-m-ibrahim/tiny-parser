import math
import sys


def isLetter(c):
    return c.isalpha()


def isDigit(c):
    try:
        int(c)
        return True
    except ValueError:
        return False


class Scanner():

    buffer = ''
    state = 0
    tokens = []

    def read(self, c):
        if (c == ' ' or c == '\n') and (self.state != 1):
            if (
                self.state == 6.1 or self.state == 7.3 or self.state == 8.4 or
                self.state == 9.4 or self.state == 10.3 or self.state == 11.2 or
                self.state == 12.5 or self.state == 13.3
            ):
                self.tokens.append((self.buffer, 'reserved'))
                self.buffer = ''
                self.state = 0
            elif self.state == 3:
                self.tokens.append((self.buffer, 'identifier'))
                self.buffer = ''
                self.state = 0
            elif self.state == 4:
                self.tokens.append((self.buffer, 'number'))
                self.buffer = ''
                self.state = 0
            return
        #symbol
        if self.state == 0:
            if (
                c == '+' or c == '-' or c == '*' or c == '/' or c == '=' or
                c == '<' or c == '(' or c == ')' or c == ';'
            ):
                self.tokens.append((c, 'sybmol'))
            elif c == ':':
                self.state = 1
                self.buffer += c
            elif isDigit(c):
                self.state = 4
                self.buffer += c
            elif c == '{':
                self.state = 5
            elif c == 'i':
                self.state = 6.0
                self.buffer += c
            elif c == 't':
                self.state = 7.0
                self.buffer += c
            elif c == 'w':
                self.state = 8.0
                self.buffer += c
            elif c == 'u':
                self.state = 9.0
                self.buffer += c
            elif c == 'e':
                self.state = 10.0
                self.buffer += c
            elif c == 'r':
                self.state = 12.0
                self.buffer += c
            elif isLetter(c):
                self.state = 3
                self.buffer += c
            else:
                raise Exception('no match')
        #:=
        elif self.state == 1:
            if c == '=':
                self.tokens.append((self.buffer+c, 'sybmol'))
                self.buffer = ''
                self.state = 0
            else:
                raise Exception('no match')
        #Identifire
        elif self.state == 3:
            if isLetter(c):
                self.buffer += c
            else:
                self.tokens.append((self.buffer, 'identifier'))
                self.buffer = ''
                self.state = 0
                self.read(c)
        #Number
        elif self.state == 4:
            if isDigit(c):
                self.buffer += c
            else:
                self.tokens.append((self.buffer, 'number'))
                self.buffer = ''
                self.state = 0
                self.read(c)
        #Comment
        elif self.state == 5:
            if c == '}':
                self.state = 0
        #If
        elif math.floor(self.state) == 6:
            if c == 'f' and self.state == 6.0:
                self.state = 6.1
                self.buffer += c
            elif self.state == 6.1:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Then
        elif math.floor(self.state) == 7:
            if c == 'h' and self.state == 7.0:
                self.state = 7.1
                self.buffer += c
            elif c == 'e' and self.state == 7.1:
                self.state = 7.2
                self.buffer += c
            elif c == 'n' and self.state == 7.2:
                self.state = 7.3
                self.buffer += c
            elif self.state == 7.3:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Write
        elif math.floor(self.state) == 8:
            if c == 'r' and self.state == 8.0:
                self.state = 8.1
                self.buffer += c
            elif c == 'i' and self.state == 8.1:
                self.state = 8.2
                self.buffer += c
            elif c == 't' and self.state == 8.2:
                self.state = 8.3
                self.buffer += c
            elif c == 'e' and self.state == 8.3:
                self.state = 8.4
                self.buffer += c
            elif self.state == 8.4:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Until
        elif math.floor(self.state) == 9:
            if c == 'n' and self.state == 9.0:
                self.state = 9.1
                self.buffer += c
            elif c == 't' and self.state == 9.1:
                self.state = 9.2
                self.buffer += c
            elif c == 'i' and self.state == 9.2:
                self.state = 9.3
                self.buffer += c
            elif c == 'l' and self.state == 9.3:
                self.state = 9.4
                self.buffer += c
            elif self.state == 9.4:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Else
        elif math.floor(self.state) == 10:
            if c == 'l' and self.state == 10.0:
                self.state = 10.1
                self.buffer += c
            elif c == 'n' and self.state == 10.0:
                self.state = 11.1
                self.buffer += c
            elif c == 's' and self.state == 10.1:
                self.state = 10.2
                self.buffer += c
            elif c == 'e' and self.state == 10.2:
                self.state = 10.3
                self.buffer += c
            elif self.state == 10.3:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #End
        elif math.floor(self.state) == 11:
            if c == 'd' and self.state == 11.1:
                self.state = 11.2
                self.buffer += c
            elif self.state == 11.2:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Repeat
        elif math.floor(self.state) == 12:
            if c == 'e' and self.state == 12.0:
                self.state = 12.1
                self.buffer += c
            elif c == 'p' and self.state == 12.1:
                self.state = 12.2
                self.buffer += c
            elif c == 'a' and self.state == 12.1:
                self.state = 13.2
                self.buffer += c
            elif c == 'e' and self.state == 12.2:
                self.state = 12.3
                self.buffer += c
            elif c == 'a' and self.state == 12.3:
                self.state = 12.4
                self.buffer += c
            elif c == 't' and self.state == 12.4:
                self.state = 12.5
                self.buffer += c
            elif self.state == 12.5:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
        #Read
        elif math.floor(self.state) == 13:
            if c == 'd' and self.state == 13.2:
                self.state = 13.3
                self.buffer += c
            elif self.state == 13.3:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'reserved'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)
            else:
                if isLetter(c):
                    self.state = 3
                    self.buffer += c
                else:
                    self.tokens.append((self.buffer, 'identifier'))
                    self.buffer = ''
                    self.state = 0
                    self.read(c)

    def eval(self):
        if self.state == 3:
            self.tokens.append((self.buffer, 'identifier'))
            self.buffer = ''
            self.state = 0
        elif self.state == 4:
            self.tokens.append((self.buffer, 'number'))
            self.buffer = ''
            self.state = 0
        elif (
            self.state == 6.1 or self.state == 7.3 or self.state == 8.4 or
            self.state == 9.4 or self.state == 10.3 or self.state == 11.2 or
            self.state == 12.5 or self.state == 13.3
        ):
            self.tokens.append((self.buffer, 'reserved'))
            self.buffer = ''
            self.state = 0
        return self.tokens

    def read_lines(self, path):
        with open(path, "r") as f:
            for c in f.read():
                self.read(c)

    def out_lines(self, path):
        with open(path, "w") as f:
            f.write(
                listToTxt(
                    self.eval()
                )
            )

def listToTxt(list):
    output = ''
    for token, type in list:
        output += token + ' : ' + type + '\n'
    return output

