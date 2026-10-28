
import csv
import time
from pathlib import Path

from ollama import chat

MODEL_NAME = "qwen2.5:1.5b"

QUESTIONS = [
    ("OOP", "What is polymorphism in Java?"),
    ("OOP", "Explain inheritance with an example."),
    ("OS", "What is a deadlock?"),
    ("OS", "What is the difference between a process and a thread?"),
    ("DBMS", "What is database normalization?"),
    ("DBMS", "Explain ACID properties."),
    ("DSA", "What is binary search?"),
    ("DSA", "Explain the time complexity of merge sort."),
    ("CN", "What is the difference between TCP and UDP?"),
    ("Python", "What is the difference between a list and a tuple?")
]

RESULTS_FILE = Path("evaluation_results.csv")


def evaluate():
    results = []

    print(f"Evaluating model: {MODEL_NAME}")
    print("-" * 50)

    for index, (topic, question) in enumerate(QUESTIONS, 1):
        print(f"\nQuestion {index}/{len(QUESTIONS)}")
        print(f"Topic: {topic}")
        print(f"Question: {question}")

        try:
            start = time.perf_counter()

            response = chat(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a computer science tutor. "
                            "Answer accurately and concisely."
                        )
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                options={
                    "temperature": 0,
                    "num_predict": 300
                }
            )

            latency = time.perf_counter() - start

            tokens = response.eval_count or 0
            generation_seconds = (
                (response.eval_duration or 0) / 1e9
            )

            speed = (
                tokens / generation_seconds
                if generation_seconds > 0
                else 0
            )

            answer = response.message.content or ""

            print(f"Latency: {latency:.2f}s")
            print(f"Output tokens: {tokens}")
            print(f"Speed: {speed:.2f} tokens/sec")

            results.append({
                "topic": topic,
                "question": question,
                "answer": answer,
                "latency_seconds": round(latency, 2),
                "output_tokens": tokens,
                "tokens_per_second": round(speed, 2),
                "status": "success"
            })

        except Exception as error:
            print(f"Error: {error}")

            results.append({
                "topic": topic,
                "question": question,
                "answer": "",
                "latency_seconds": "",
                "output_tokens": "",
                "tokens_per_second": "",
                "status": f"error: {error}"
            })

    # Save results to CSV
    with RESULTS_FILE.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "topic",
                "question",
                "answer",
                "latency_seconds",
                "output_tokens",
                "tokens_per_second",
                "status"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    successful = [
        result for result in results
        if result["status"] == "success"
    ]

    if successful:
        average_latency = sum(
            result["latency_seconds"]
            for result in successful
        ) / len(successful)

        average_speed = sum(
            result["tokens_per_second"]
            for result in successful
        ) / len(successful)

        print("\n" + "=" * 50)
        print("EVALUATION SUMMARY")
        print("=" * 50)

        print(f"Total questions: {len(QUESTIONS)}")
        print(f"Successful responses: {len(successful)}")
        print(f"Average latency: {average_latency:.2f}s")
        print(f"Average generation speed: {average_speed:.2f} tokens/sec")
        print(f"Results saved to: {RESULTS_FILE}")

    else:
        print("No successful responses were generated.")


if __name__ == "__main__":
    evaluate()
