from polyglot.detect import Detector


def lang_detect(txt):
    languages = Detector(txt).languages
    for lang in languages:
        print(lang)


text = 'Game theory is a set of tools used to help analyze situations where an individual’s best course of action depends on what others do or are expected to do. Game theory allows us to understand how people act in situations where they are interconnected.'

lang_detect(text)
