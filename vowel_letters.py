from argparse import ArgumentParser
import re

WORDS_PUNCTUATION = {"-", "'"}
VOWEL_LETTERS = set("аоуыиэеёюя")


def count_vowels(word: str) -> int:
    return len(set(word).intersection(VOWEL_LETTERS))


def vowel_letters(s: str) -> list:
    # ans = set()
    # j = 0
    # while j < len(s):
    #     begin = j
    #     while j < len(s) and (s[j].isalpha() or s[j] in WORDS_PUNCTUATION):
    #         j += 1
    #     if begin != j:
    #         this = s[begin:j]
    #         if not set(this).issubset(WORDS_PUNCTUATION) and count_vowels(this) == 1:
    #             ans.add(this)
    #     j += 1
    ans = list(filter(lambda word: count_vowels(word) == 1, set(re.split(r'\W+', s.lower()))))
    return sorted(ans, key=len)


def test(num: str, s: str):
    return "test " + num + ": \"" + s + "\"\n" + '\n'.join(vowel_letters(s))


if __name__ == "__main__":
    tests = {
        '1': "еее еее йщш ыолфт фдддфф ссв оо",
        '2': "С этой стро-кой нормально нормально.",
        '3': "Вот тут! Тут! Нет нужных повторов",
        '4': "С этой строкой все не не очень очень нормально",
        '5': "Довольно распространённая оши-бка ошибка – это лишний повтор повтор слова слова. "
             "Смешно, не не правда ли? Не нужно портить хор хоровод."
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
        print('\n'.join(vowel_letters(input())))
