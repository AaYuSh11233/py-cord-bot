user_memory = {}

def add_to_memory(user_id: int, message: str):
    if user_id not in user_memory:
        user_memory[user_id] = []
    user_memory[user_id].append(message)
    user_memory[user_id] = user_memory[user_id][-10:]  # keep last 10

def get_memory(user_id: int):
    return "\n".join(user_memory.get(user_id, []))
