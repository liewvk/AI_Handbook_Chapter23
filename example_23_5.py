class BookAssistant:
    def __init__(self):
        self.last_book = None
        self.prices = {"AI Handbook": 28.0}
 
    def select(self, title):
        if title not in self.prices:
            return "Unknown title"
        self.last_book = title
        return f"Selected: {title}"
 
    def price(self):
        if self.last_book is None:
            return "Select a book first"
        return self.prices[self.last_book]
 
agent = BookAssistant()
print(agent.select("AI Handbook"))
print("Current price:", agent.price())

