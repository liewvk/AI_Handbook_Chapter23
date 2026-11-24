def quote(quantity: int, unit_price: float) -> float:
    if type(quantity) is not int or not 1 <= quantity <= 100:
        raise ValueError("Quantity must be an integer from 1 to 100")
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)):
        raise TypeError("Price must be numeric")
    if not 0 <= unit_price <= 10000:
        raise ValueError("Price is outside the allowed range")
    return round(quantity * unit_price, 2)
 
print("Total:", quote(3, 28.0))

