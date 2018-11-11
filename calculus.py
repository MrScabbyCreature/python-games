#program doing various functions of calculus(only differentiation for now)

def variables():
    global numbers, numbers_string
    numbers = range(10)
    numbers_string = []
    for ch in numbers:
        numbers_string.append(str(ch))
variables()

class calculus:
    def __init__(self, function):
        self.function = function
        self.list_convert()

    def list_convert(self):
        self.listy = []
        for ch in self.function:
            if ch in numbers_string:
                self.listy.append(int(ch))
            else:
                self.listy.append(ch)
        return self.listy	

    def string_convert(self, list_input):
        self.stringy = ''
        for ch in list_input:
            self.stringy += str(ch)
        return self.stringy 
    
    def differentiate(self):
        self.listy.append(" ")
        for i in range(len(self.listy)):
            if self.listy[i] in numbers:
                if (self.listy[i+1] == '+' or self.listy[i+1] == '-' or self.listy[i+1] == " ") and (self.listy[i-1] == '+' or self.listy[i-1] == '-'):
                    self.listy.pop(i)
                    self.listy.pop(i-1)
                    self.listy.append(" ")
                    self.listy.append(" ")
                    
        for i in range(len(self.listy)):
            if self.listy[i] == 'x':
                if self.listy[i+1] in numbers:
                    if self.listy[i-1] in numbers:
                        self.listy[i-1] *= self.listy[i+1]
                        if self.listy[i+1] == 2:
                            self.listy.pop(i+1)
                            self.listy.append(" ")
                        else:
                            self.listy[i+1] -= 1
                    else:
                        self.listy.insert(i-1, self.listy[i+1])
                        if self.listy[i+1] == 2:
                            self.listy.pop(i+1)
                            self.listy.append(" ")
                        else:
                            self.listy[i+1] -= 1
                else:
                    self.listy.pop(i)
                    self.listy.append(" ")
        
        while self.listy[-1] == ' ':
            self.listy.pop(-1)
        return self.listy
    
    def computer_script(self):
        self.comp_listy = self.listy
        self.comp_listy.append(" ")
        for i in range(len(self.comp_listy)):
            if self.comp_listy[i] == 'x':
                if self.comp_listy[i-1] in numbers:
                    self.comp_listy.insert(i, '*')
                if self.comp_listy[i+1] in numbers:
                    self.comp_listy.insert(i+1, '^')
        self.comp_listy.pop(-1)
        return self.comp_listy
                   

function1 = "-5x+1"
function2 = "x2-4x-5"

func1 = calculus(function1)
func2 = calculus(function2)

ori1 = func1.string_convert(func1.computer_script())
func1.list_convert()
func1.differentiate()
dif1 = func1.string_convert(func1.computer_script())

ori2 = func2.string_convert(func2.computer_script())
func2.list_convert()
func2.differentiate()
dif2 = func2.string_convert(func2.computer_script())

result = "(" + "(" + "(" + dif1 + ")" + "*" + "(" + ori2 + ")" + ")" + "-" + "(" + "(" + dif2 + ")" + "*" + "(" + ori1 + ")" + ")" + ")" + "/" + "(" + ori2 + ")" + "^" + "2"
print 'd', " ", function1
print "--", "", "---------", "=", result
print "dx", "", function2
print