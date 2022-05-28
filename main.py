import time

NUMBER_CHARS = [str(i) for i in range(0, 10)]


def match_lesson(s):
    word = ''
    for j in range(len(s)):
        word = word + s[j]
        if word == 'lesson' and s[j + 1] in NUMBER_CHARS:
            return True
    return False


class Timetable:
    def __init__(self):
        self.lessons = []
        self.day = ""


def parse_line(line):
    line = line.replace("  ", "").replace('\n', '')
    key, word = line.split(":", 1)
    return key, word


def parse_file(file):
    lines = file.readlines()
    schedule = Timetable()
    lesson = dict()
    timetable_start = False
    for line in lines:
        if timetable_start:
            if line.count("  ", 0, 2) == 0:  # проверяем не закончилась ли таблица
                break
            else:
                line = line.replace("\n", "").replace("  ", "").replace(": ", ":")
                if match_lesson(line) and len(lesson) != 0:
                    schedule.lessons.append(lesson)
                    lesson = dict()
                else:
                    key, word = parse_line(line)
                    lesson[key] = word
        if "timetable" in line:
            timetable_start = True

    schedule.lessons.append(lesson)
    return schedule


def file_to_xml(file):
    schedule = parse_file(file)
    xml = "<timetable>\n"
    for i in range(0,len(schedule.lessons)):
        lesson = schedule.lessons[i]
        if i==0:
            for p in lesson:
                xml += f"\t<{p}>{lesson[p]}</{p}>\n"
    for i in range(1, len(schedule.lessons)):
        lesson = schedule.lessons[i]
        xml += f"\t<lesson{i}>\n"
        for p in lesson:
            xml += f"\t\t<{p}>{lesson[p]}</{p}>\n"
        xml += f"\t</lesson{i}>\n"
    xml += "</timetable>"
    return xml


def convert_file(input_file_name, output_file_name, show=False):
    input_file = open(input_file_name + ".yml", 'r', encoding='utf-8')
    output_file = open(output_file_name + ".xml", 'w', encoding="utf-8")
    xml = file_to_xml(input_file)
    output_file.write(xml)
    input_file.close()
    output_file.close()
    if show:
        print(xml)


convert_file("timetable", "timetable", True)


start_time = time.perf_counter()
time.sleep(0)
for n in range(10):
    convert_file("timetable", "timetable")
print(f'time:  {time.perf_counter() - start_time}')
