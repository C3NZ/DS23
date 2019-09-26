def main():
    result = {}
    words = ["yes", "yes", "yes"]
    word = map(
        lambda x: eval(f"global result; result[{x}] = result[{x}] + 1; print('hi')")
        if x in result
        else eval(f"global result; result[{x}] = 1; print('hi')"),
        words,
    )

    print(result)


if __name__ == "__main__":
    main()
