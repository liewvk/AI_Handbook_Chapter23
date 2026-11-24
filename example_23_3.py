def lookup_stock(book):
    stock = {"AI Handbook": 12, "Python Basics": 4}
    return stock.get(book, 0)
 
def estimate_total(quantity, unit_price):
    if type(quantity) is not int or not 1 <= quantity <= 100:
        raise ValueError("Invalid quantity")
    return round(quantity * float(unit_price), 2)
 
TOOLS = {"lookup_stock": lookup_stock,
         "estimate_total": estimate_total}
 
def run_tool(name, arguments):
    if name not in TOOLS:
        raise ValueError("Tool not permitted")
    return TOOLS[name](**arguments)
 
print(run_tool("lookup_stock", {"book": "AI Handbook"}))
print(run_tool("estimate_total", {"quantity": 2,
                                  "unit_price": 28.0}))

