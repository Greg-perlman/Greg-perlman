from urllib.request import urlopen

def fetch():
    story = urlopen('http://sixty-north.com/c/t.txt')
    words = []
    for line in story:
        lines = line.decode('utf-8').split()
        for word in lines:
            words.append(lines)
    story.close()
    return words


def print_words(words):
    for w in words:
        print(w)


def main():

    words = fetch()
    print_words(words)

if __name__ == '__main__':
    main()

def add_spam(menu= None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


num_to_Let = {'1':'A',
              '2':'B',
              '3':'C',
              '4':'D'}
let_to_num = {let : num for num, let in num_to_let.items() }
