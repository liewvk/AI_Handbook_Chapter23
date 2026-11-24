def submit_order(book, quantity, approved=False):
    if approved is not True:
        return "Order not submitted: approval required"
    if type(quantity) is not int or quantity <= 0:
        return "Order rejected: invalid quantity"
    return f"Simulation only: {quantity} copy/copies of {book}"
 
print(submit_order("AI Handbook", 2))
print(submit_order("AI Handbook", 2, approved=True))

