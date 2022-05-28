from argparse import ArgumentParser

WORDS_PUNCTUATION = {"-", "'"}
SENTENCE_PUNCTUATION = {',', '.', ':', ';', '!', '?'}


def text_corrector(s: str) -> str:
    s = ' '.join(s.split())
    prev = ""
    j = 0
    while j < len(s):
        begin = j
        removed = 0
        if j > 0 and s[j - 1] in SENTENCE_PUNCTUATION:
            prev = ""
        while j < len(s) and (s[j].isalpha() or s[j] in WORDS_PUNCTUATION):
            j += 1
        if begin != j:
            this = s[begin:j].lower()
            if set(this).issubset(WORDS_PUNCTUATION):
                prev = ""
                continue
            if prev == this:
                s = s[:begin-1] + s[j:]
                removed = len(this) + 1
            prev = this
        j += -removed + 1
    return s


def test(num: str, s: str):
    return "test " + num + ": \"" + s + "\"\n" + text_corrector(s)


if __name__ == "__main__":
    tests = {
        '1': "qwerty qwerty qwerty   qwerty u u u u u u kgksgdlh",
        '2': "С этой строкой что-то что-то не так так.",
        '3': "Вот тут! Тут! Нет нужных повторов",
        '4': "С этой строкой все не не очень очень нормально",
        '5': "Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."
    }
    argument_parser = ArgumentParser(prog="text_corrector")
    argument_parser.add_argument(
        "--test",
        choices=(list(tests.keys()) + ['all']),
        help=""
    )
    args = argument_parser.parse_args()
    if args.test:
        if args.test != 'all':
            print(test(args.test, tests[args.test]))
        else:
            for i in tests.keys():
                print(test(i, tests[i]))
    else:
        print(text_corrector(input()))
