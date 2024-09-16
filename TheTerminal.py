from pathlib import Path
import json

class Terminal():

    def set_def_value(parameter, subparameter):
        current_directory = Path(__file__).parent
        file_path = current_directory / 'data.json'
        with file_path.open("r") as file:
            data = json.load(file)
        
        user_var = []
        run = True
        i = 0
        while run:
            user_var.append(input("VALUE: "))
            if user_var[i].isdigit():
                user_var[i] = int(user_var[i])
            else:
                if user_var[i].rfind('/end') != -1:
                    user_var[(len(user_var)-1):] = ''
                    break
            i+=1

        data[parameter][subparameter] = user_var
        #match parameter:
        #    case 'font':
        #        data['specs']['font'] = [input('inp1: '), int(input('inp2: '))]
        #    case 'window_def':
        #        data['specs']['window_def'] = [int(input('inp1: ')), input('inp2: ')]
        #    case 'accent':
        #        data['colors']['accent'] = input('inp1: ')
        #    case 'bg':
        #        data['colors']['bg'] = input('inp1: ')
        #    case 'text':
        #        data['colors']['text'] = input('inp1: ')
        #    case _:
        #        user_var = ''
        #        run = True
        #        chamber = input('inp1: ')
        #        while run:
        #            user_var += input("VALUE: ") + '|'
        #            if user_var.rfind('/end') != -1:
        #                user_var = user_var.split('|')
        #                user_var[(len(user_var)-2):] = ''
        #                break
        
        #        data['user_presets'][chamber] = user_var

        with file_path.open("w") as file:
            json.dump(data, file, indent=4)


Terminal.set_def_value(input('parameter: '), input('subparameter: '))
