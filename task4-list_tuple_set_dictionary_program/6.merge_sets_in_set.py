def merge_sets(set1, set2):
    """Return the union of two sets."""
    return set1.union(set2)


def main():
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = merge_sets(set1, set2)
    print(set3)


if __name__ == "__main__":
    main()
