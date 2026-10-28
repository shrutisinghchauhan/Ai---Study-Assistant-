
import csv
import re
from collections import defaultdict

import matplotlib.pyplot as plt

INPUT_FILE = "rag_comparison_results.csv"

# Extract answers from the CSV
with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    results = list(csv.DictReader(f))


def is_correct(answer, expected):
    """
    Basic automatic correctness check.
    Suitable for short factual answers.
    Review ambiguous cases manually.
    """
    answer = answer.lower().strip()
    expected = expected.lower().strip()

    if expected == "repeatable read":
        return "repeatable read" in answer

    if expected == "atlasdb":
        return "atlasdb" in answer

    if expected == "02:15":
        return bool(
            re.search(r"(?<!\d)0?2:15(?!\d)", answer)
        )

    # Match numeric values without matching parts
    # of longer numbers.
    return bool(
        re.search(
            rf"(?<!\d){re.escape(expected)}(?!\d)",
            answer
        )
    )


summary = defaultdict(
    lambda: {
        "total": 0,
        "correct": 0,
        "latencies": []
    }
)

for row in results:
    if row["status"] != "success":
        continue

    mode = row["mode"]
    summary[mode]["total"] += 1

    if is_correct(row["answer"], row["expected_answer"]):
        summary[mode]["correct"] += 1

    summary[mode]["latencies"].append(
        float(row["total_latency_seconds"])
    )


print("\nRAG VS NON-RAG EVALUATION")
print("=" * 45)

for mode in ("No RAG", "RAG"):
    data = summary[mode]

    accuracy = (
        100 * data["correct"] / data["total"]
        if data["total"] else 0
    )

    avg_latency = (
        sum(data["latencies"]) / len(data["latencies"])
        if data["latencies"] else 0
    )

    print(f"\n{mode}")
    print(f"Correct answers: {data['correct']}/{data['total']}")
    print(f"Estimated accuracy: {accuracy:.1f}%")
    print(f"Average latency: {avg_latency:.2f}s")


# Accuracy comparison chart
modes = ["No RAG", "RAG"]

accuracies = [
    (
        100 * summary[mode]["correct"] / summary[mode]["total"]
        if summary[mode]["total"] else 0
    )
    for mode in modes
]

plt.figure(figsize=(7, 5))
plt.bar(modes, accuracies)
plt.ylabel("Estimated Answer Accuracy (%)")
plt.title("Qwen2.5 1.5B: RAG vs Non-RAG")
plt.ylim(0, 105)

for i, value in enumerate(accuracies):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.savefig("rag_accuracy_comparison.png", dpi=200)
plt.show()

print("\nChart saved: rag_accuracy_comparison.png")
