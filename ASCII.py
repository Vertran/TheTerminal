import json
import os

class Console():
    def extend_path(file, type):
        match type:
            case 'style':
                return os.getcwd() + f"\\styles\\{file}.json"
            case 'none':
                return os.getcwd() + f"\\{file}.json"

    def read_json(file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data

    
    def get_style(pref_file):
        with open(pref_file, 'r') as f:
            data = json.load(f)
        return data["CURRENT"]["style"]

    def set_style(pref_file, style):
        try:
            with open(pref_file, 'r') as f:
                prefs = json.load(f)
        except FileNotFoundError:
            prefs = {}

        prefs["CURRENT"]["style"] = style

        with open(pref_file, 'w') as f:
            json.dump(prefs, f, indent=4)

    def generate_ASCII(text, style):
        size = len(style['a'])
        lines = []
        for line_letter in text.split('\n'):
            line = [''] * size
            
            for letter in line_letter:
                if letter == '':
                    line 
                if letter in style:
                    for j in range(size):
                        line[j] += style[letter][j]
                else:
                    for j in range(len(line)):
                        if j < 7:
                            line[j] += '#' * len(style['a'][0])

            lines.append(line)
        return lines
    
    def print_ASCII(conv_text):        
        for line in conv_text:
            for i in line:
                print(i)
            print()