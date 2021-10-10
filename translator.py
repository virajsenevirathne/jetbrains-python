import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source')
parser.add_argument('target')
parser.add_argument('word')

args = parser.parse_args()

LANGUAGES = ['All', 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
             'Portuguese',
             'Romanian', 'Russian', 'Turkish']


def display_menu():
    print("Hello, you're welcome to the translator. Translator supports: ")
    for i, l in enumerate(LANGUAGES):
        print(f"{i + 1}. {l}")
    source = LANGUAGES[int(input('Type the number of your language:\n'))]
    target = LANGUAGES[
        int(input("Type the number of a language you want to translate to or '0' to translate to all \n"))]
    word = input('Type the word you want to translate:\n')
    return source, target, word


def get_input():
    source = args.source.capitalize()
    target = args.target.capitalize()
    word = args.word
    return source, target, word


def get_data(source, target, word):
    url = f"https://context.reverso.net/translation/{source}-{target}/{word}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')


def get_translated_words(html_page):
    words = html_page.find(id={'translations-content'}).findAll('a', class_={'translation'})
    translations = [i.text.strip() for i in words]
    return translations[0]


def extract_examples(html_page):
    examples = html_page.find(id={'examples-content'}).findAll('div', class_={'example'})
    examples_list = []
    for div in examples:
        examples_list.append((div.find(class_={'src'}).text.strip(), div.find(class_={'trg'}).text.strip()))
    return examples_list[0]


def get_translations(source, target, word, file):
    try:
        html_page = get_data(source.lower(), target.lower(), word)
        translated_word = get_translated_words(html_page)
        print(f'\n{target} Translations:')
        file.write(f'{target} Translations:\n')
        print(translated_word)
        file.write(translated_word + '\n')
        print(f'\n{target} Example:')
        file.write(f'\n{target} Example:\n')
        examples = extract_examples(html_page)
        print(examples[0] + ':')
        file.write(examples[0] + ':\n')
        print(examples[1])
        file.write(examples[1] + '\n')
        print()
        file.write("\n\n")
        return True
    except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
        return False
    except AttributeError:
        print(f"Sorry, unable to find {word}")
        return False


def main():
    source, target, word = get_input()
    if source not in LANGUAGES or target not in LANGUAGES:
        print(f"Sorry, the program doesn't support {source.lower() if source not in LANGUAGES else target.lower()}")
        return
    f = open(f"{word}.txt", "w", encoding="utf-8")
    if target == "All":
        for i in LANGUAGES[1:]:
            target = i
            if target == source:
                continue
            else:
                if not get_translations(source, target, word, f):
                    break

    else:
        get_translations(source, target, word, f)
    f.close()


if __name__ == "__main__":
    main()
