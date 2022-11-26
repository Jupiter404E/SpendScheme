<p align="center">
  <b>
    Convenient text formatting
  </b>
</p>

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
### If a feature doesn't work, check if your console supports it.
---

## Do you have any questions?

Сontact [me](https://discord.gg/). For help with SpendScheme.
