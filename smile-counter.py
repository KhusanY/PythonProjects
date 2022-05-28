import re
from argparse import ArgumentParser


def smile_counter(s: str) -> int:
    n = len(s)
    # k = 0
    # for i in range(0, n - 2):
    #     if s[i] == ";" and s[i + 1] == "<" and s[i + 2] == "P":
    #         k += 1
    # return k return s.count(";<P")
print(re.search(r'\w+', ';<P'))


def test(num: str, s: str):
    return "test " + num + ": \"" + s + "\"\n" + str(smile_counter(s))


if __name__ == "__main__":
    tests = {
        '1': ";<P;<P;<P;<P;<P;<P;<Pdighshlwdlszhsu lojtslgl",
        '2': "mz;<Pnvz,v,didj  kd;<P;<P;<Phmv  lk,x ",
        '3': "Тут нет нужных смайлов",
        '4': ";<P                  п",
        '5': "'4': \";<P                  п\",    ",
    }
    argument_parser = ArgumentParser(prog="smile-counter")
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
        print(smile_counter(input()))
