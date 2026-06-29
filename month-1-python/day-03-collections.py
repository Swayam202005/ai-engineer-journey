"""Day 3 - Python Collections

What you learn today:
- Lists, tuples, sets, dictionaries
- Comprehensions (list/dict/set)
- Nested structures and common patterns (frequency, grouping)

Run:
  python day-03-collections.py
"""

from __future__ import annotations


def filter_evens(nums: list[int]) -> list[int]:
    """Return only even numbers."""
    return [n for n in nums if n % 2 == 0]


def squares(nums: list[int]) -> list[int]:
    """Return squares of numbers."""
    return [n * n for n in nums]


def top_k_largest(nums: list[int], k: int = 3) -> list[int]:
    """Return the top k largest values (simple approach without sorting-heavy logic).

    Notes:
    - For learning, we’ll just sort once.
    - In future days, we can discuss heap-based approaches.
    """
    return sorted(nums, reverse=True)[:k]


def frequency(words: list[str]) -> dict[str, int]:
    """Count frequency of each word."""
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def group_by_city(records: list[dict[str, str]]) -> dict[str, list[str]]:
    """Group record names by their city.

    Example input:
      [{"name":"A", "city":"Pune"}, {"name":"B", "city":"Pune"}, ...]
    Output:
      {"Pune": ["A","B"], "Mumbai": ["C"]}
    """
    grouped: dict[str, list[str]] = {}
    for r in records:
        city = r["city"]
        name = r["name"]
        grouped.setdefault(city, []).append(name)
    return grouped


def set_operations(a: list[int], b: list[int]) -> dict[str, set[int]]:
    """Compute common set operations to practice uniqueness + overlaps."""
    set_a = set(a)
    set_b = set(b)

    return {
        "unique_in_a": set_a - set_b,
        "union": set_a | set_b,
        "intersection": set_a & set_b,
    }


def demo():
    # -------- Exercise A: Lists & slicing --------
    nums = [1, 2, 7, 10, 3, 12, 5, 6]

    evens = filter_evens(nums)
    sq = squares(nums)
    top3 = top_k_largest(nums, k=3)

    print("Exercise A - Lists")
    print("nums      :", nums)
    print("evens     :", evens)
    print("squares   :", sq)
    print("top3      :", top3)
    print()

    # -------- Exercise B: Dictionary frequency count --------
    words = ["ai", "ml", "ai", "data", "ml", "ai", "python"]
    counts = frequency(words)

    print("Exercise B - Dictionary frequency")
    print("words     :", words)
    print("counts    :", counts)
    print()

    # -------- Exercise C: Group by key --------
    records = [
        {"name": "A", "city": "Pune"},
        {"name": "B", "city": "Pune"},
        {"name": "C", "city": "Mumbai"},
        {"name": "D", "city": "Mumbai"},
    ]

    grouped = group_by_city(records)

    print("Exercise C - Group by city")
    print("records   :", records)
    print("grouped   :", grouped)
    print()

    # -------- Exercise D: Set uniqueness/overlap --------
    a = [1, 2, 2, 3, 8]
    b = [2, 3, 5, 8, 13]
    ops = set_operations(a, b)

    print("Exercise D - Set operations")
    print("a         :", a)
    print("b         :", b)
    print("unique in a (a-b):", ops["unique_in_a"])
    print("union (a|b)      :", ops["union"])
    print("intersection (a&b):", ops["intersection"])
    print()

    # -------- Exercise E: Comprehensions --------
    # Example: use comprehensions to derive a dict of word->len
    word_lengths = {w: len(w) for w in counts.keys()}

    print("Exercise E - Comprehensions")
    print("word_lengths (dict comprehension):", word_lengths)


if __name__ == "__main__":
    demo()

