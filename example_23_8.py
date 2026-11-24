from ollama import chat
 
MODEL = "qwen3.5:4b"  # Replace with your installed model.
MAX_ROUNDS = 3
 
def add(a: int, b: int) -> int:
    """Add two integers.
 
    Args:
        a: First integer.
        b: Second integer.
 
    Returns:
        The sum.
    """
    if type(a) is not int or type(b) is not int:
        raise ValueError("Integers required")
    return a + b
 
messages = [{"role": "user", "content": "Add 18 and 24."}]
for round_number in range(MAX_ROUNDS):
    response = chat(model=MODEL, messages=messages, tools=[add])
    messages.append(response.message)
    calls = response.message.tool_calls or []
    if not calls:
        print("Assistant:", response.message.content)
        break
    for call in calls:
        if call.function.name != "add":
            result = "Tool not permitted"
        else:
            try:
                result = str(add(**call.function.arguments))
            except (TypeError, ValueError) as error:
                result = f"Tool error: {error}"
        messages.append({"role": "tool",
                         "tool_name": call.function.name,
                         "content": result})
else:
    print("Stopped: maximum tool rounds reached")

