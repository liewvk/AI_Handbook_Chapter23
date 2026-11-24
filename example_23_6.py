def safe_add(a, b):
    if not all(type(x) in (int, float) for x in (a, b)):
        raise ValueError("Numeric inputs required")
    return a + b
 
action = {"tool": "safe_add", "arguments": {"a": 12, "b": 8}}
allowed = {"safe_add": safe_add}
if action["tool"] not in allowed:
    raise ValueError("Unknown action")
answer = allowed[action["tool"]](**action["arguments"])
print("Tool result:", answer)

