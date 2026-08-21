from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.set_text_color(44, 62, 80)
# Corrected syntax for older fpdf2 compatibility
pdf.cell(0, 10, "LeetCode Practice Questions - Topic Wise", 0, 1, "L")
pdf.ln(5)

# Table Header
pdf.set_font("helvetica", "B", 10)
pdf.set_fill_color(44, 62, 80)
pdf.set_text_color(255, 255, 255)

col_widths = [15, 22, 90, 63]
headers = ["Q. No.", "LC #", "Question Name", "Topic"]
for i, h in enumerate(headers):
    pdf.cell(col_widths[i], 8, h, 1, 0, "C" if i<2 else "L", fill=True)
pdf.ln()

# Table Data
data = [
    ["1", "1", "Two Sum", "Array, Hash Table"],
    ["2", "217", "Contains Duplicate", "Array, Hash Table"],
    ["3", "242", "Valid Anagram", "String, Hash Table"],
    ["4", "387", "First Unique Character in a String", "String, Hash Table"],
    ["5", "169", "Majority Element", "Array, Hash Table, Greedy"],
    ["6", "383", "Ransom Note", "String, Hash Table"],
    ["7", "49", "Group Anagrams", "String, Hash Table, Sorting"],
    ["8", "349", "Intersection of Two Arrays", "Array, Hash Set"],
    ["9", "136", "Single Number", "Array, Bit Manipulation"],
    ["10", "347", "Top K Frequent Elements", "Array, Hash Table, Heap"],
    ["11", "125", "Valid Palindrome", "String, Two Pointers"],
    ["12", "151", "Reverse Words in a String", "String"],
    ["13", "509", "Fibonacci Number", "Dynamic Programming, Recursion"],
    ["14", "70", "Climbing Stairs", "Dynamic Programming"],
    ["15", "50", "Pow(x, n)", "Recursion, Binary Exponentiation"],
    ["16", "62", "Unique Paths", "Dynamic Programming, Combinatorics"],
    ["17", "54", "Spiral Matrix", "Array, Matrix, Simulation"],
    ["18", "78", "Subsets", "Array, Backtracking, Bit Manipulation"],
    ["19", "46", "Permutations", "Array, Backtracking"],
    ["20", "39", "Combination Sum", "Array, Backtracking"],
]

pdf.set_font("helvetica", "", 9)
pdf.set_text_color(51, 51, 51)
for row in data:
    pdf.cell(col_widths[0], 6, row[0], 1, 0, "C")
    pdf.cell(col_widths[1], 6, row[1], 1, 0, "C")
    pdf.cell(col_widths[2], 6, row[2], 1, 0, "L")
    pdf.cell(col_widths[3], 6, row[3], 1, 0, "L")
    pdf.ln()

pdf.ln(5)

# Topics Covered
pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(52, 73, 94)
pdf.cell(0, 8, "Topics Covered", 0, 1, "L")
pdf.set_font("helvetica", "", 9)
pdf.set_text_color(51, 51, 51)

topics_text = (
    "        Arrays & Hashing: 1, 2, 5, 8, 9, 10 \n        Strings: 3, 4, 6, 7, 11, 12\n"
    "        Two Pointers: 11 \n        Bit Manipulation: 9, 18 \n        Dynamic Programming: 13, 14, 16\n"
    "        Recursion: 13, 15 \n        Backtracking: 18, 19, 20 \n        Matrix / Simulation: 17\n"
    "        Heap / Priority Queue: 10 \n        Combinatorics: 16 \n        Sorting: 7"
)
pdf.multi_cell(0, 5, topics_text)
pdf.ln(3)

# Student Instructions
pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(52, 73, 94)
pdf.cell(0, 8, "Student Instructions", 0, 1, "L")
pdf.set_font("helvetica", "", 9)
pdf.set_text_color(51, 51, 51)

instructions = (
    "        - Solve each problem on LeetCode using the assigned problem number.\n"
    "        - First understand the problem statement and constraints.\n"
    "        - Try a brute-force approach before optimizing.\n"
    "        - Practice writing clean and readable code.\n"
    "        - Revise the underlying topic/pattern after completing each question."
)
pdf.multi_cell(0, 5, instructions)

pdf.output("LeetCode_Practice_Questions.pdf")