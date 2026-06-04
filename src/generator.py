import csv
import copy
import html
import math
import os
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
    'Travelling Salesman Problem',
    'Job Shop Scheduling Problem',
    'Flow Shop Problem',
    'Sorting & Ranking',
    'Graph Matching',
    'Quadratic Assignment Problem',
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

PROBLEM_ALIASES = {
    'TSP': 'Travelling Salesman Problem',
}

GAP_PERCENT_DISPLAY_LIMIT = 5.0
BENCHMARK_GAP_DISPLAY_LIMITS = {
    "Uniform TSP-500": 3.5,
}


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


def slugify(text):
    keep = []
    for ch in text.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in (" ", "-", "_", "/"):
            keep.append("-")
    return "-".join(part for part in "".join(keep).split("-") if part)


def parse_float(value):
    if value is None or value == "":
        return None
    return float(value)


def parse_bool(value, default=True):
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "lower_is_better"}


def get_float(row, *columns):
    for column in columns:
        if not column:
            continue
        value = parse_float(row.get(column))
        if value is not None:
            return value
    return None


def get_row_float(row, pointer_column, fallback_columns):
    return get_float(row, row.get(pointer_column, "").strip(), *fallback_columns)


def get_row_float_with_column(row, pointer_column, fallback_columns):
    pointed_column = row.get(pointer_column, "").strip()
    for column in [pointed_column] + list(fallback_columns):
        if not column:
            continue
        value = parse_float(row.get(column))
        if value is not None:
            return value, column
    return None, ""


def display_problem_name(problem):
    return PROBLEM_ALIASES.get(problem, problem)


def display_benchmark_name(benchmark):
    if " " in benchmark:
        return benchmark.replace("Tsp", "TSP")
    parts = benchmark.replace("-", "_").split("_")
    if len(parts) == 3 and parts[0] == "uniform" and parts[1] == "tsp":
        return "Uniform TSP-{}".format(parts[2])
    return benchmark.replace("_", " ").title()


def display_metric_name(metric):
    return metric.replace("_", " ")


def row_method(row):
    return (row.get("method", "").strip()
            or row.get("method_id", "").strip()
            or row.get("plot_series_key", "").strip()
            or row.get("paper_title", "").strip())


def row_series_key(row):
    return (row.get("plot_series_key", "").strip()
            or row.get("method_id", "").strip()
            or row_method(row))


def row_series_label(row):
    return row_method(row) or row_series_key(row)


def method_venue_label(method, rows):
    for row in rows:
        publisher = row.get("publisher", "").strip()
        year = row.get("year", "").strip()
        if publisher and year:
            return "{} ({} {})".format(method, publisher, year)
        if year:
            return "{} ({})".format(method, year)
        if publisher:
            return "{} ({})".format(method, publisher)
    return method


def read_benchmark_results(csvFile):
    if not csvFile or not os.path.exists(csvFile):
        return {}

    benchmark_results = {}
    with open(csvFile, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            problem = display_problem_name(row.get("problem", "").strip())
            benchmark_id = row.get("benchmark", "").strip()
            benchmark = display_benchmark_name(benchmark_id)
            y_column = row.get("plot_y_default", "").strip()
            x_column = row.get("plot_x", "").strip()
            performance, y_source_column = get_row_float_with_column(row, "plot_y_default", ["performance", "gap_percent", "objective_length", "tour_length"])
            runtime = parse_float(row.get("runtime_seconds"))
            runtime_instances = parse_float(row.get("runtime_instances"))
            normalized_runtime = get_row_float(
                row,
                "plot_x",
                [
                    "normalized_runtime_seconds_1000_instances",
                    "time_seconds_1000_instances",
                    "time_1000_instances_sec",
                ],
            )

            if not problem or not benchmark_id or performance is None:
                continue

            if normalized_runtime is None and runtime is not None and runtime_instances:
                normalized_runtime = runtime * 1000.0 / runtime_instances
            if normalized_runtime is None:
                continue

            row["problem"] = problem
            row["benchmark"] = benchmark
            row["benchmark_id"] = benchmark_id
            row["performance"] = performance
            row["normalized_runtime_seconds_1000_instances"] = normalized_runtime
            row["performance_metric"] = y_column or y_source_column or "performance"
            row["runtime_metric"] = x_column or "normalized_runtime_seconds_1000_instances"
            row["series_key"] = row_series_key(row)
            row["series_label"] = row_series_label(row)
            row["lower_is_better"] = parse_bool(row.get("gap_direction") or row.get("lower_is_better"), default=True)
            benchmark_results.setdefault(problem, {}).setdefault(benchmark, []).append(row)

    return benchmark_results


def format_time(seconds):
    if seconds < 60:
        return "{:.0f}s".format(seconds)
    if seconds < 3600:
        return "{:.0f}m".format(seconds / 60)
    return "{:.1f}h".format(seconds / 3600)


def format_metric_value(value):
    if abs(value) >= 100:
        return "{:.0f}".format(value)
    if abs(value) >= 10:
        return "{:.1f}".format(value)
    if abs(value) >= 1:
        return "{:.2f}".format(value)
    return "{:.3f}".format(value)


def nice_ticks(min_value, max_value, count=5):
    if min_value == max_value:
        return [min_value]
    span = max_value - min_value
    step = span / float(count - 1)
    return [min_value + i * step for i in range(count)]


def shorten(text, limit):
    if len(text) <= limit:
        return text
    return text[:limit - 3].rstrip() + "..."


def rectangles_overlap(a, b, padding=3):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return not (
        ax + aw + padding <= bx
        or bx + bw + padding <= ax
        or ay + ah + padding <= by
        or by + bh + padding <= ay
    )


def choose_label_rect(x, y, width, height, occupied, plot_bounds):
    left, top, right, bottom = plot_bounds
    candidate_offsets = [
        (10, -height - 10),
        (-width - 10, -height - 10),
        (10, 10),
        (-width - 10, 10),
        (-width / 2, -height - 18),
        (-width / 2, 18),
        (18, -height / 2),
        (-width - 18, -height / 2),
    ]
    for distance in (0, 12, 24, 36, 52, 70):
        for dx, dy in candidate_offsets:
            candidate_x = min(max(x + dx, left), right - width)
            candidate_y = min(max(y + dy + (distance if dy >= 0 else -distance), top), bottom - height)
            rect = (candidate_x, candidate_y, width, height)
            if not any(rectangles_overlap(rect, other) for other in occupied):
                return rect
    candidate_x = min(max(x + 10, left), right - width)
    candidate_y = min(max(y + 10, top), bottom - height)
    return (candidate_x, candidate_y, width, height)


def benchmark_sort_key(item):
    benchmark, rows = item
    sizes = [get_float(row, "benchmark_size", "n_nodes") for row in rows]
    sizes = [size for size in sizes if size is not None]
    return (min(sizes) if sizes else float("inf"), benchmark)


def method_sort_key(item):
    key, rows = item
    labels = [row.get("series_label", key) for row in rows]
    orders = [get_float(row, "plot_order_within_method_benchmark") for row in rows]
    orders = [order for order in orders if order is not None]
    return (labels[0].lower() if labels else key.lower(), min(orders) if orders else float("inf"))


def is_main_experiment_row(row):
    text = " ".join([
        row.get("source_table", ""),
        row.get("test_set_notes", ""),
        row.get("notes", ""),
    ]).lower()
    excluded_markers = (
        "additional",
        "extra",
        "footnote",
        "second proposed",
    )
    return not any(marker in text for marker in excluded_markers)


def pareto_improving_rows(rows):
    by_method = {}
    for row in rows:
        method = row.get("series_label", "").strip() or row_method(row)
        by_method.setdefault(method, []).append(row)

    kept = []
    for method_rows in by_method.values():
        method_rows = sorted(method_rows, key=lambda row: (
            row["normalized_runtime_seconds_1000_instances"],
            row["performance"],
            get_float(row, "plot_order_within_method_benchmark") or float("inf"),
        ))
        lower_is_better = method_rows[0].get("lower_is_better", True)
        best = None
        for row in method_rows:
            value = row["performance"]
            if best is None:
                kept.append(row)
                best = value
                continue
            improves = value < best if lower_is_better else value > best
            if improves:
                kept.append(row)
                best = value
    return sorted(kept, key=lambda row: row["normalized_runtime_seconds_1000_instances"])


def gap_display_limit(rows):
    if not rows:
        return GAP_PERCENT_DISPLAY_LIMIT
    benchmark = rows[0].get("benchmark", "")
    return BENCHMARK_GAP_DISPLAY_LIMITS.get(benchmark, GAP_PERCENT_DISPLAY_LIMIT)


def rows_for_chart(rows):
    if not rows:
        return []
    metric_id = rows[0].get("performance_metric", "performance")
    rows = [row for row in rows if is_main_experiment_row(row)]
    if "gap" in metric_id.lower():
        limit = gap_display_limit(rows)
        rows = [row for row in rows if row["performance"] <= limit]
    return pareto_improving_rows(rows)


def render_benchmark_chart(problem, benchmark, rows, output_path, chart_label=None):
    rows = sorted(rows, key=lambda row: row["normalized_runtime_seconds_1000_instances"])
    if not rows:
        return False

    width = 920
    height = 560 if len(rows) <= 35 else 640
    margin_left = 82
    margin_right = 305
    margin_top = 82
    margin_bottom = 82
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom
    palette = [
        "#2F6BFF", "#D24B3A", "#1C8C5A", "#7B4BB3", "#B57900",
        "#008C9E", "#C23B7A", "#5E6D2C", "#555555", "#E07A2F",
    ]

    xs = [row["normalized_runtime_seconds_1000_instances"] for row in rows]
    ys = [row["performance"] for row in rows]
    x_min = min(xs)
    x_max = max(xs)
    metric_id = rows[0].get("performance_metric", "performance")
    metric = display_metric_name(metric_id)
    is_gap_metric = "gap" in metric_id.lower()
    gap_limit = gap_display_limit(rows)
    use_log_y = is_gap_metric and gap_limit > 5.0
    if is_gap_metric:
        y_min = 0.0
        y_max = gap_limit
        if use_log_y:
            positive_ys = [value for value in ys if value > 0]
            y_min = min(positive_ys) / 1.25
            y_log_min = math.log10(y_min)
            y_log_max = math.log10(y_max)
    else:
        y_min = min(0.0, min(ys))
        y_max = max(ys)
        if y_max == y_min:
            y_max = y_min + 1.0
        y_max = y_max * 1.08

    x_scale = sorted(xs)[len(xs) // 2] if xs else 1.0
    x_scale = max(x_scale, 1e-9)
    x_scaled_min = math.asinh(x_min / x_scale)
    x_scaled_max = math.asinh(x_max / x_scale)

    def x_pos(value):
        if x_max == x_min:
            return margin_left + plot_width / 2
        return margin_left + (math.asinh(value / x_scale) - x_scaled_min) / (x_scaled_max - x_scaled_min) * plot_width

    x_tick_values = [x_scale * math.sinh(tick) for tick in nice_ticks(x_scaled_min, x_scaled_max, count=8)]
    x_axis_note = "Normalized runtime for 1000 instances (asinh scale)"

    if use_log_y:
        def y_pos(value):
            value = max(value, y_min)
            return margin_top + (y_log_max - math.log10(value)) / (y_log_max - y_log_min) * plot_height

        y_tick_values = [10 ** tick for tick in nice_ticks(y_log_min, y_log_max, count=7)]
        y_axis_label = "{} log scale (<= {}%)".format(metric, format_metric_value(gap_limit))
    else:
        def y_pos(value):
            return margin_top + (y_max - value) / (y_max - y_min) * plot_height

        y_tick_values = nice_ticks(y_min, y_max, count=7)
        y_axis_label = "{} (<= {}%)".format(metric, format_metric_value(gap_limit)) if is_gap_metric else metric

    methods = []
    for row in rows:
        method = row.get("series_label", "").strip() or row_method(row)
        if method not in methods:
            methods.append(method)
    method_colors = {method: palette[i % len(palette)] for i, method in enumerate(methods)}
    direction = "lower is better" if rows[0].get("lower_is_better", True) else "higher is better"
    title = benchmark if not chart_label else "{} - {}".format(benchmark, chart_label)
    draw_point_numbers = len(rows) <= 35

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}" viewBox="0 0 {0} {1}" role="img" aria-labelledby="title desc">'.format(width, height),
        '<title id="title">{}</title>'.format(html.escape("{}: {}".format(problem, title))),
        '<desc id="desc">Time-performance scatter plot. Runtime is normalized to 1000 instances.</desc>',
        '<rect width="100%" height="100%" fill="#FFFFFF"/>',
        '<text x="32" y="38" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#222">{}</text>'.format(html.escape(title)),
        '<text x="32" y="62" font-family="Arial, sans-serif" font-size="13" fill="#555">{}; {}</text>'.format(html.escape(metric), html.escape(direction)),
        '<line x1="{0}" y1="{1}" x2="{2}" y2="{1}" stroke="#222" stroke-width="1.4"/>'.format(margin_left, margin_top + plot_height, margin_left + plot_width),
        '<line x1="{0}" y1="{1}" x2="{0}" y2="{2}" stroke="#222" stroke-width="1.4"/>'.format(margin_left, margin_top, margin_top + plot_height),
    ]

    for tick in x_tick_values:
        x = x_pos(tick)
        lines.extend([
            '<line x1="{0:.1f}" y1="{1}" x2="{0:.1f}" y2="{2}" stroke="#E2E2E2"/>'.format(x, margin_top, margin_top + plot_height),
            '<text x="{0:.1f}" y="{1}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#555">{2}</text>'.format(x, margin_top + plot_height + 22, html.escape(format_time(tick))),
        ])

    for tick in y_tick_values:
        y = y_pos(tick)
        lines.extend([
            '<line x1="{0}" y1="{1:.1f}" x2="{2}" y2="{1:.1f}" stroke="#E2E2E2"/>'.format(margin_left, y, margin_left + plot_width),
            '<text x="{0}" y="{1:.1f}" text-anchor="end" dominant-baseline="middle" font-family="Arial, sans-serif" font-size="11" fill="#555">{2}</text>'.format(margin_left - 10, y, html.escape(format_metric_value(tick))),
        ])

    lines.extend([
        '<text x="{0}" y="{1}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#333">{2}</text>'.format(margin_left + plot_width / 2, height - 28, html.escape(x_axis_note)),
        '<text x="22" y="{0}" text-anchor="middle" transform="rotate(-90 22 {0})" font-family="Arial, sans-serif" font-size="12" fill="#333">{1}</text>'.format(margin_top + plot_height / 2, html.escape(y_axis_label)),
    ])

    series_rows = {}
    for row in rows:
        method = row.get("series_label", "").strip() or row_method(row)
        series_rows.setdefault(method, []).append(row)
    for method, method_rows in series_rows.items():
        if len(method_rows) < 2:
            continue
        method_rows = sorted(method_rows, key=lambda row: (
            row["normalized_runtime_seconds_1000_instances"],
            row["performance"],
        ))
        points = " ".join(
            "{:.1f},{:.1f}".format(
                x_pos(row["normalized_runtime_seconds_1000_instances"]),
                y_pos(row["performance"]),
            )
            for row in method_rows
        )
        lines.append(
            '<polyline points="{}" fill="none" stroke="{}" stroke-width="2" stroke-opacity="0.55" stroke-linejoin="round" stroke-linecap="round"/>'.format(
                html.escape(points),
                method_colors[method],
            )
        )

    legend_x = margin_left + plot_width + 36
    legend_y = margin_top
    lines.append('<text x="{0}" y="{1}" font-family="Arial, sans-serif" font-size="13" font-weight="700" fill="#222">Methods / variants</text>'.format(legend_x, legend_y - 18))

    for index, row in enumerate(rows, start=1):
        method = row.get("series_label", "").strip() or row_method(row)
        variant = (row.get("variant", "").strip()
                   or row.get("source_table", "").strip()
                   or row.get("record_id", "").strip())
        color = method_colors[method]
        x = x_pos(row["normalized_runtime_seconds_1000_instances"])
        y = y_pos(row["performance"])
        label = "{}. {}".format(index, method)
        if variant:
            label += " ({})".format(variant)
        tooltip = "{}\n{}\n{}: {:.3f}\nNormalized runtime: {}".format(
            method,
            variant or benchmark,
            metric,
            row["performance"],
            format_time(row["normalized_runtime_seconds_1000_instances"]),
        )
        lines.extend([
            '<g>',
            '<title>{}</title>'.format(html.escape(tooltip)),
            '<circle cx="{0:.1f}" cy="{1:.1f}" r="{2}" fill="{3}" stroke="#FFFFFF" stroke-width="1.5"/>'.format(x, y, 6 if draw_point_numbers else 4, color),
        ])
        if draw_point_numbers:
            lines.append('<text x="{0:.1f}" y="{1:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Arial, sans-serif" font-size="7" font-weight="700" fill="#FFFFFF">{2}</text>'.format(x, y, index))
        lines.append('</g>')

    legend_methods = list(series_rows)
    legend_step = min(24, max(14, (height - legend_y - 36) / max(len(legend_methods), 1)))
    legend_font_size = 10 if legend_step < 20 else 11
    for legend_index, method in enumerate(legend_methods, start=1):
        ly = legend_y + legend_index * legend_step
        legend_label = method_venue_label(method, series_rows[method])
        color = method_colors[method]
        lines.extend([
            '<circle cx="{0}" cy="{1:.1f}" r="4.5" fill="{2}"/>'.format(legend_x, ly - 4, color),
            '<text x="{0}" y="{1:.1f}" font-family="Arial, sans-serif" font-size="{2}" fill="#333">{3}</text>'.format(legend_x + 13, ly, legend_font_size, html.escape(shorten(legend_label, 48))),
        ])

    occupied_label_rects = []
    plot_bounds = (
        margin_left,
        margin_top,
        margin_left + plot_width,
        margin_top + plot_height,
    )
    chart_label_methods = sorted(series_rows, key=lambda method: min(
        x_pos(row["normalized_runtime_seconds_1000_instances"]) - margin_left
        + (margin_top + plot_height - y_pos(row["performance"]))
        for row in series_rows[method]
    ))
    for method in chart_label_methods:
        method_rows = sorted(series_rows[method], key=lambda row: (
            x_pos(row["normalized_runtime_seconds_1000_instances"]) - margin_left
            + (margin_top + plot_height - y_pos(row["performance"])),
            row["normalized_runtime_seconds_1000_instances"],
        ))
        anchor_row = method_rows[0]
        anchor_x = x_pos(anchor_row["normalized_runtime_seconds_1000_instances"])
        anchor_y = y_pos(anchor_row["performance"])
        color = method_colors[method]
        label = shorten(method, 24)
        label_width = len(label) * 6.2 + 10
        label_height = 18
        label_x, label_y, _, _ = choose_label_rect(
            anchor_x,
            anchor_y,
            label_width,
            label_height,
            occupied_label_rects,
            plot_bounds,
        )
        occupied_label_rects.append((label_x, label_y, label_width, label_height))
        lines.extend([
            '<line x1="{0:.1f}" y1="{1:.1f}" x2="{2:.1f}" y2="{3:.1f}" stroke="{4}" stroke-width="1" stroke-opacity="0.75"/>'.format(anchor_x, anchor_y, label_x, label_y + label_height / 2, color),
            '<rect x="{0:.1f}" y="{1:.1f}" width="{2:.1f}" height="{3}" rx="3" fill="#FFFFFF" fill-opacity="0.88" stroke="{4}" stroke-width="1"/>'.format(label_x, label_y, label_width, label_height, color),
            '<text x="{0:.1f}" y="{1:.1f}" font-family="Arial, sans-serif" font-size="10" font-weight="700" fill="{2}">{3}</text>'.format(label_x + 5, label_y + 12.5, color, html.escape(label)),
        ])

    lines.append("</svg>")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return True


def write_benchmark_section(file, mdFile, category, benchmark_results, chartDir):
    benchmarks = benchmark_results.get(category, {})
    if not benchmarks:
        return

    file.writelines("#### Benchmark Results (Beta)")
    file.write("\n\n")
    file.writelines("*Beta feature: benchmark charts are generated from `data/benchmark_results.csv`. The results, sourced directly from original papers using common benchmarks, are presented to directly illustrate the evolution of performance. Runtime is normalized to 1000 instances by instance count only; hardware is not normalized. Gap charts show main-experiment points within benchmark-specific gap bounds (3.5% for TSP-500, 5% otherwise); within each baseline, slower points are shown only when they improve gap.*")
    file.write("\n\n")

    md_dir = os.path.dirname(os.path.abspath(mdFile))
    for benchmark, rows in sorted(benchmarks.items(), key=benchmark_sort_key):
        chart_rows = rows_for_chart(rows)
        if not chart_rows:
            continue
        file.writelines("##### {}".format(benchmark))
        file.write("\n\n")

        chart_name = "{}_{}_all-baselines.svg".format(slugify(category), slugify(benchmark))
        chart_path = os.path.join(chartDir, chart_name)
        render_benchmark_chart(category, benchmark, chart_rows, chart_path, chart_label="All baselines")
        chart_rel = os.path.relpath(os.path.abspath(chart_path), md_dir)
        file.writelines("[![{} benchmark chart]({})]({})".format(benchmark, chart_rel, chart_rel))
        file.write("\n\n")


def csv2md(csvFile, mdFile, header, benchmarkFile="../data/benchmark_results.csv", chartDir="../assets/benchmarks"):
    csvFile = open(csvFile, "r", encoding='utf-8')
    reader = csv.reader(csvFile)
    raw_papers = []
    papers = []
    for item in reader:
        if reader.line_num == 1:
            continue
        raw_papers.append(item)
    csvFile.close()
    benchmark_results = read_benchmark_results(benchmarkFile)

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
        write_benchmark_section(file, mdFile, category, benchmark_results, chartDir)
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
                write_benchmark_section(file, mdFile, category, benchmark_results, chartDir)
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
