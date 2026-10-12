"""Hello world: my first Python project."""


def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = input("What's your name? ").strip()
    print(greet(name or "World"))


if __name__ == "__main__":
    main()
