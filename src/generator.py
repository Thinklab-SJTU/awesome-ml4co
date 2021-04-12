import csv
import os
import copy


def md2csv(mdFile, csvFile):  # From the md file to generate a csv file that contains the paper list.
    f = open(mdFile)
    line = f.readline()
    problem_start = False
    paper_list = []
    category = None
    while line:
        print(line)
        if problem_start and "### [" in line:
            category = line[line.find("[") + 1: line.find("]")]
        if problem_start and '0' <= line[0] <= '9':
            new_paper = ["" for _ in range(7)]  # 0 category, 1 title, 2 publisher, 3 year, 4 type, 5 link, 6 authors;
            new_paper[0] = category
            index = 1
            i = -1
            while i + 1 < len(line):
                i += 1
                if i < line.find(". **") + 4:
                    continue
                new_paper[index] += line[i]
                if i == line.find(".**") and index == 1:  # title -> publisher
                    i += 3
                    index += 1
                    continue
                if line[i + 1] == "," and index == 2:  # publisher -> year
                    i += 2
                    index += 1
                    continue
                if line[i + 1] == "." and index == 3:  # year -> type
                    i += 3
                    index += 1
                    continue
                if line[i + 1] == "]" and index == 4:  # type -> link
                    i += 2
                    index += 1
                    continue
                if line[i + 1] == ")" and index == 5:  # link->authors
                    index += 1
                    break
            assert index == 6
            _ = f.readline()
            line = f.readline()
            new_paper[index] = line[line.find('*') + 1:-2]
            paper_list.append(new_paper)

        if "</table>" in line:
            problem_start = True
        line = f.readline()
    f.close()
    with open(csvFile, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "title", "publisher", "year", "type", "link", "authors"])
        for paper in paper_list:
            writer.writerow(paper)


def sort_by_time(elem):
    return elem[3]


def csv2md(csvFile, mdFile, header):
    csvFile = open(csvFile, "r", encoding='utf-8')
    reader = csv.reader(csvFile)
    raw_papers = []
    papers = []
    for item in reader:
        if reader.line_num == 1:
            continue
        raw_papers.append(item)
    csvFile.close()

    classes = []
    for paper in raw_papers:
        if ";" in paper[0]:
            paper_classes = paper[0].split(";")
            paper_classes = [cls.strip() for cls in paper_classes]
        else:
            paper_classes = [paper[0].strip()]
        for cls in paper_classes:
            if cls not in classes:
                classes.append(cls)

    for c in classes:
        p = []
        for paper in raw_papers:
            if c in paper[0]:
                new_paper = copy.deepcopy(paper)
                new_paper[0] = c
                p.append(new_paper)
        p.sort(key=sort_by_time)
        papers = papers + p

    command = "cp " + header + " " + mdFile
    os.system(command)
    with open(mdFile, "a") as file:
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        num = 0
        category = papers[0][0]
        file.writelines("### [{}](#content)".format(category))
        file.write('\n')
        file.write('\n')
        for paper in papers:
            paper = [p.strip() for p in paper]
            if paper[0] != category:
                if category == "Survey Papers":
                    file.writelines("## [Problems](#content)")
                    file.write('\n')
                    file.write('\n')
                category = paper[0]
                file.writelines("### [{}](#content)".format(category))
                file.write('\n')
                file.write('\n')
                num = 0
            num += 1
            # "category", "title", "publisher", "year", "type", "link", "authors, *code"
            if paper[7] == "":
                file.writelines(
                    "{}. **{}** {}, {}. [{}]({})".format(num, paper[1], paper[2], paper[3], paper[4], paper[5]))
            else:
                file.writelines(
                    "{}. **{}** {}, {}. [{}]({}), [code]({})".format(num, paper[1], paper[2], paper[3], paper[4],
                                                                     paper[5], paper[7]))
            file.write('\n')
            file.write('\n')
            file.writelines("    *{}*".format(paper[6]))
            file.write('\n')
            file.write('\n')


if __name__ == '__main__':
    # md2csv("../README.md", "../data/papers.csv")
    csv2md("../data/papers.csv", "../README.md", "../data/header.md")
