def book_price(title):
    catalogue = {"AI Handbook": 28.0, "Python Basics": 22.0}
    return catalogue.get(title)
 
def handle(request):
    if request == "price of AI Handbook":
        price = book_price("AI Handbook")
        return f"Price: ${price:.2f}" if price else "Not found"
    return "Please ask about an available title."
 
print(handle("price of AI Handbook"))

