import csv
import copy
import shutil

abbr = {'Graph Matching': 'GM', 'Travelling Salesman Problem': 'TSP', 'Vehicle Routing Problem': 'VRP',
        'Job Shop Scheduling Problem': 'JSSP', 'Flow Shop Problem': 'FSP', 'Bin Packing Problem': 'BPP', 'Graph Edit Distance': 'GED',
        'Maximal Common Subgraph': 'MCS', 'Maximal Independent Set': 'MIS', 'Boolean Satisfiability': 'SAT',
        'Quadratic Assignment Problem': 'QAP',
        'Hamiltonian Cycle Problem': 'HCP',
        'Multiple Travelling Salesman Problem': 'mTSP',
        'Electronic Design Automation': 'EDA',
        'Orienteering Problem': 'OP',
        'Virtual Network Embedding': 'VNE',
        'Optical Power Flow': 'OPF',
        'Sorting & Ranking':'Sort&Rank',
        'Facility Location Problem': 'FLP',
        'Portfolio Optimization': 'PortOpt',
        'Mixed Integer Programming': 'MIP',
        }

# Canonical problem order for the Content table and ### sections (Thinklab awesome-ml4co).
PROBLEM_CATEGORY_ORDER = (
    'Job Shop Scheduling Problem',
    'Flow Shop Problem',
    'Sorting & Ranking',
    'Graph Matching',
    'Quadratic Assignment Problem',
    'Travelling Salesman Problem',
    'Portfolio Optimization',
    'Maximal Cut',
    'Vehicle Routing Problem',
    'Maximum Independent Set',
    'Generalization',
    'Orienteering Problem',
    'Knapsack',
    'Boolean Satisfiability',
    'Computing Resource Allocation',
    'Bin Packing Problem',
    'Graph Edit Distance',
    'Hamiltonian Cycle Problem',
    'Graph Coloring',
    'Maximal Common Subgraph',
    'Influence Maximization',
    'Max Clique',
    'Mixed Integer Programming',
    'Causal Discovery',
    'Game Theoretic Semantics',
    'Differentiable Optimization',
    'Car Dispatch',
    'Electronic Design Automation',
    'Conjunctive Query Containment',
    'Virtual Network Embedding',
    'Predict+Optimize',
    'Optimal Power Flow',
    'Facility Location Problem',
    'Combinatorial Drug Recommendation',
    'Stochastic Combinatorial Optimization',
    'Vertex Cover',
)


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

    discovered = set()
    for paper in raw_papers:
        if ";" in paper[0]:
            for cls in paper[0].split(";"):
                discovered.add(cls.strip())
        else:
            discovered.add(paper[0].strip())

    problem_classes = [c for c in PROBLEM_CATEGORY_ORDER if c in discovered]
    unknown = discovered - {'Survey Papers'} - set(PROBLEM_CATEGORY_ORDER)
    for c in sorted(unknown):
        problem_classes.append(c)

    content_order = []
    if 'Survey Papers' in discovered:
        content_order.append('Survey Papers')
    content_order.extend(problem_classes)

    for c in content_order:
        p = []
        for paper in raw_papers:
            if c in paper[0]:
                new_paper = copy.deepcopy(paper)
                new_paper[0] = c
                p.append(new_paper)
        p.sort(key=sort_by_time)
        papers = papers + p

    shutil.copy(header, mdFile)
    with open(mdFile, "a", encoding='utf-8') as file:
        # Problems index in the Content table (pairs per row)
        for i in range((len(problem_classes) + 1) // 2):
            name1 = problem_classes[2 * i]
            num1 = 2 * i + 1
            name_index1 = name1.replace(" ", "-").lower()
            file.writelines('<tr>\n')
            if name1 in abbr:
                file.writelines(
                    '\t<td>&emsp;<a href=#{}>2.{} {} ({})</a></td>\n'.format(
                        name_index1, num1, name1, abbr[name1]))
            else:
                file.writelines(
                    '\t<td>&emsp;<a href=#{}>2.{} {}</a></td>\n'.format(name_index1, num1, name1))
            if 2 * i + 1 < len(problem_classes):
                name2 = problem_classes[2 * i + 1]
                num2 = 2 * i + 2
                name_index2 = name2.replace(" ", "-").lower()
                if name2 in abbr:
                    file.writelines(
                        '\t<td>&emsp;<a href=#{}>2.{} {} ({})</a></td>\n'.format(
                            name_index2, num2, name2, abbr[name2]))
                else:
                    file.writelines(
                        '\t<td>&emsp;<a href=#{}>2.{} {}</a></td>\n'.format(name_index2, num2, name2))
            else:
                file.writelines('<td>&ensp;</td>\n')
            file.writelines('</tr>\n')
        file.writelines('</table>\n')

        # write content
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
