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
