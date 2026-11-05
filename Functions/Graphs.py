"""Plotext terminal charts for recorded session activity."""

from collections import Counter


def activity_category(message):
    message = str(message).lower()
    if message.startswith("[!]"):
        return "Security warnings"
    for keywords, category in (
        (("analytics", "analytical graph"), "Analytical Graph"),
        (("password generator",), "Password generator"),
        (("strength",), "Strength checker"),
        (("vault", "password manager"), "Password vault"),
        (("encrypt", "decrypt"), "Encryption / decryption"),
        (("history",), "History views"),
        (("logged", "exited"), "Session access"),
    ):
        if any(keyword in message for keyword in keywords):
            return category
    return "Other activity"


def plot_activity(entries, *, show=True):
    """Build a terminal chart and return its text; print it when show is True."""
    counts = Counter(activity_category(entry) for entry in entries)
    if not counts:
        chart = "No session activity recorded yet."
    else:
        import plotext as plt
        from shutil import get_terminal_size

        categories, values = zip(*reversed(counts.most_common()))
        labels = [f"{category} ({count})" for category, count in zip(categories, values)]
        width = get_terminal_size(fallback=(100, 30)).columns
        plt.clear_figure()
        plt.plotsize(min(width, 120), max(12, len(labels) * 2 + 6))
        plt.bar(labels, values, orientation="horizontal", color="cyan")
        plt.title("Analytical Graph")
        plt.xlabel(f"Recorded events ({sum(values)} total)")
        # Keep the count axis integral, even for small or very large sessions.
        step = max(1, (max(values) + 5) // 6)
        ticks = list(range(0, max(values) + 1, step))
        plt.xticks(ticks, [str(tick) for tick in ticks])
        chart = plt.build()
        chart += "\nCurrent session only - counts include tool opens."
    if show:
        print(chart)
    return chart

def Graph():
    import UI
    from Functions.Action_Hist import history

    UI.header("Analytical Graph", "Recorded activity grouped by category")
    try:
        plot_activity(list(history))
    except ModuleNotFoundError as exc:
        if exc.name != "plotext":
            raise
        UI.info('Plotext is required. Install plotext<6.0.0 with: pip install "plotext>=5.3.2,<6.0.0"')
    except AttributeError:
        UI.error('The installed Plotext version is incompatible. Install plotext<6.0.0 with: pip install "plotext>=5.3.2,<6.0.0"')


if __name__ == "__main__":
    plot_activity([])
