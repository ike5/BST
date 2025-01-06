from Node import Node


def main() -> None:
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)

    print(root.value)
    print(root.left.value)
    print(root.right.value)


if __name__ == "__main__":
    main()
