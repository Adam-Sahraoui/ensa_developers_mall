# ENSA Developers Wall

A collaborative Git & GitHub exercise where every student contributes one visible developer card.

## Student workflow

1. Fork the original repository.
2. Clone your fork:

```bash
git clone <YOUR_FORK_URL>
cd ensa_developers_wall_starter_v2
```

3. Create your branch:

```bash
git switch -c feature/your-name
```

4. Create your file inside `students/`:

```text
students/your-name.html
```

Copy `students/_template.html` and change:
- initials
- name
- specialty
- GitHub username
- favorite technology

5. Check changes:

```bash
git status
```

6. Stage:

```bash
git add .
```

7. Commit:

```bash
git commit -m "Add Ahmed developer card"
```

8. Push:

```bash
git push -u origin feature/ahmed-card
```

9. Open a Pull Request to the original repository.

10. Review and merge.

## Final reveal

After all Pull Requests are merged, the trainer runs:

```bash
git switch main
git pull
python build.py
```

Then open `index.html`.

## Workflow

Fork -> Clone -> Branch -> Code -> Add -> Commit -> Push -> Pull Request -> Review -> Merge
