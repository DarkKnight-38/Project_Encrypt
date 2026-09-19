history = []

def pull_hist():
    if not history:
        print("[i] No actions recorded in this session yet.")
        return
    print("\n--- SESSION ACTION HISTORY ---")
    for i, entry in enumerate(history, 1):
        print(f"[{i}] {entry}")
    print()

def push_hist(message):
    history.append(str(message))
