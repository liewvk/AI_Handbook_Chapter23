inventory = {"AI Handbook": {"stock": 12, "price": 28.0}}
 
def prepare_quote(book, quantity):
    item = inventory.get(book)
    if item is None:
        return "Title unavailable"
    if type(quantity) is not int or quantity < 1:
        return "Invalid quantity"
    if item["stock"] < quantity:
        return "Insufficient stock"
    total = quantity * item["price"]
    return f"Available: {quantity} copies; draft total: ${total:.2f}"
print(prepare_quote("AI Handbook", 5))

