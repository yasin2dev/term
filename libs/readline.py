import readline

def arrowKeys():
    print('\n'.join([str(readline.get_history_item(i + 1))
    for i in range(readline.get_current_history_length())]))
