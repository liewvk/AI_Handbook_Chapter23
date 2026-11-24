from ollama import chat
 
MODEL = "qwen3.5:4b"  # Replace with an installed, tool-capable model.
 
def multiply(a: int, b: int) -> int:
    """Multiply two integers.
 
    Args:
        a: First integer.
        b: Second integer.
 
    Returns:
        Their product.
    """
    if type(a) is not int or type(b) is not int:
        raise ValueError("Integers required")
    return a * b
 
messages = [{"role": "user", "content": "What is 7 multiplied by 8?"}]
response = chat(model=MODEL, messages=messages, tools=[multiply])
messages.append(response.message)
allowed = {"multiply": multiply}
 
if response.message.tool_calls:
    for call in response.message.tool_calls:
        name = call.function.name
        if name != "multiply":
            result = "Tool not permitted"
        else:
            try:
                result = str(allowed[name](**call.function.arguments))
            except (TypeError, ValueError) as error:
                result = f"Tool error: {error}"
        messages.append({"role": "tool", "tool_name": name,
                         "content": result})
    final = chat(model=MODEL, messages=messages, tools=[multiply])
    print(final.message.content)
else:
    print(response.message.content)

