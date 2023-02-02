<p align="center">
  <b>
    Convenient text formatting
  </b>
</p>

<hr>

<a href="https://pypi.org/project/SpendScheme/">
<img src="https://img.shields.io/pypi/v/SpendScheme?style=for-the-badge" alt="PyPi"/>
</a>
<a href="https://pypi.org/project/SpendScheme/">
<img src="https://img.shields.io/pypi/dm/SpendScheme?color=green&style=for-the-badge&label=downloads" alt="PyPi"/>
</a>
<a href="https://github.com/Jupiter404E/SpendScheme/" tabindex="-1">
<img src="https://img.shields.io/github/repo-size/Jupiter404E/SpendScheme?style=for-the-badge" alt="Repo Size"/>
</a>
<a href="https://github.com/Jupiter404E/SpendScheme/" tabindex="-1">
<img src="https://img.shields.io/github/last-commit/Jupiter404E/SpendScheme?style=for-the-badge" alt="GitHub last commit"/>
</a>
<a href="https://github.com/Jupiter404E/SpendScheme/" tabindex="-1">
<img src="https://img.shields.io/github/commit-activity/m/Jupiter404E/SpendScheme?style=for-the-badge" alt="GitHub commit activity"/>
</a>
<a href="https://pypi.org/project/SpendScheme/">
<img src="https://img.shields.io/badge/Page-PyPi-lightgrey?style=for-the-badge" alt="PyPi"/>
</a>
<a href="https://ko-fi.com/Jupiter404E">
<img src="https://img.shields.io/badge/Buy%20me-a%20coffee-ff69b4?style=for-the-badge", alt="ko-fi"/>
</a>

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

print (
    SpendScheme.Color.red,
    "Red! ",
    SpendScheme.Color.blue,
    "Blue! ",
    SpendScheme.Color.green,
    "Green! ",
    SpendScheme.Color.end
)

## Format type

print (
    SpendScheme.Style.italic,
    "Italic! "
)
```

Or you can do something like this:

```python
import SpendScheme

formatingText = SpendScheme.Formatting(text = "** Your text **")
formatingText.lowerTranslit()

print (
    formatingText.answer()
)
```

## Making tables:

```python
import SpendScheme

data = [
    [
        "Product", "Cost"
    ],
    {
        "Strawberry": "2$",
        "Blueberry":  "2,71$",
        "Banana":     "1,63$",
        "Apple":      "30¢", 
        "Limon":      "2$",
    }
]

tableCreate = SpendScheme.Table()

print (
    tableCreate.createTable(data = data)
)
```

---

<a href="https://github.com/Jupiter404E/SpendScheme/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Jupiter404E/SpendScheme" />
</a>

---
### If a feature doesn't work, check if your console supports it.
---

## Do you have any questions?

Сontact [me](https://discord.gg/). For help with SpendScheme.
