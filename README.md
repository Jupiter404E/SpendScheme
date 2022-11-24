<p align="center">
  <b>
    Convenient text formatting
  </b>
</p>

<!-- <hr>

<a class="github-badge" href="https://melisa.readthedocs.io/en/latest/?badge=latest" tabindex="-1">
<img src="https://readthedocs.org/projects/melisa/badge/?version=latest" alt="Documentation Status"/>
</a>
<a class="github-badge" href="https://github.com/MelisaDev/melisa" tabindex="-1">
<img src="https://img.shields.io/github/repo-size/MelisaDev/melisa" alt="Repo Size"/>
</a>
<a class="github-badge" href="https://github.com/MelisaDev/melisa" tabindex="-1">
<img src="https://img.shields.io/github/last-commit/MelisaDev/melisa" alt="GitHub last commit"/>
</a>
<a class="github-badge" href="https://github.com/MelisaDev/melisa" tabindex="-1">
<img src="https://img.shields.io/github/commit-activity/m/MelisaDev/melisa?label=commits" alt="GitHub commit activity"/>
</a>
<a class="github-badge" href="https://discord.gg/QX4EG8f7aD" tabindex="-1">
<img src="https://img.shields.io/discord/951867868188934216" alt="Discord"/>
</a> -->

<hr>

<h2 align="center">
This library is currently under development.
</h2>

## About
<strong>SpendScheme</strong> is a microframework for text formatting in Python 3

An optimized library that simplifies writing code and helps with the tasks provided.

---
## Install SpendScheme

### Installing from PyPi:
```commandline
pip install SpendScheme
```
### Installing from Git:
```commandline
pip install git+https://github.com/Jupiter404E/SpendScheme
```

---

## List of possible events

```python
import SpendScheme

formatingText = SpendScheme.Formatting(text = "** Your text **")
```

Changing the color and type of text in your console:

```python
import SpendScheme

## Color

setColor = SpendScheme.Colour()

print (
    setColor.red(),
    "Red! ",
    setColor.blue(),
    "Blue! ",
    setColor.green(),
    "Green! ",
    setColor.end()
)

## Format type

setStyle = SpendScheme.Style()

print (
    setStyle.italic(),
    "Italic! "
)
```

Or you can do something like this:

```python

```

---

## Do you have any questions?

Сontact [me](https://discord.gg/). For help with SpendScheme.