from pathlib import Path

ROOT = Path(__file__).parent
STUDENTS = ROOT / "students"
INDEX = ROOT / "index.html"

START = "<!-- STUDENT_CARDS_START -->"
END = "<!-- STUDENT_CARDS_END -->"

html = INDEX.read_text(encoding="utf-8")
before, rest = html.split(START, 1)
_, after = rest.split(END, 1)

cards = []
for file in sorted(STUDENTS.glob("*.html")):
    if file.name.startswith("_"):
        continue
    cards.append(file.read_text(encoding="utf-8").strip())

if cards:
    content = "\n\n".join(cards)
else:
    content = """<article class="student-card example-card">
  <div class="avatar">EX</div>
  <h2>Example Student</h2>
  <p class="specialty">Software Engineering</p>
  <p><strong>GitHub:</strong> @example</p>
  <p><strong>Favorite tech:</strong> Java</p>
</article>"""

INDEX.write_text(
    before + START + "\n      " + content.replace("\n", "\n      ") + "\n      " + END + after,
    encoding="utf-8"
)

print(f"Built {len(cards)} student card(s) into index.html")
