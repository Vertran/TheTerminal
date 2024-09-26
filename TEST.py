from ASCII import Console as sl

file = 'roman'
text = """Hello World!
How are you?"""
action = input('Enter: ')

if action.split(' ')[0] == 'style':
    sl.set_style(sl.extend_path('prefs', 'none'))
elif action.split(' ')[0] == 'text':
    text = action[1:]
elif action.split(' ')[0]

sl.print_ASCII(sl.generate_ASCII(text, sl.read_json(sl.extend_path(sl.get_style(sl.extend_path('prefs', 'none')), 'style'))))