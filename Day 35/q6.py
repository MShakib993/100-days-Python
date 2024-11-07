class ListManager:
    def __init__(self):
        self.items = []  # Initialize an empty list

    def append_item(self, item):
        """Append an item to the list."""
        self.items.append(item)
        print(f"Appended {item}: {self.items}")

    def insert_item(self, index, item):
        """Insert an item at a specified index in the list."""
        self.items.insert(index, item)
        print(f"Inserted {item} at index {index}: {self.items}")

    def extend_items(self, new_items):
        """Extend the list by appending elements from another iterable."""
        self.items.extend(new_items)
        print(f"Extended with {new_items}: {self.items}")

    def count_item(self, item):
        """Count occurrences of an item in the list."""
        count = self.items.count(item)
        print(f"Item {item} occurs {count} times in the list.")
        return count

# Example usage
if __name__ == "__main__":
    manager = ListManager()

    manager.append_item(5)
    manager.append_item(10)
    manager.insert_item(1, 7)  # Inserting 7 at index 1
    manager.extend_items([20, 30, 40])  # Extending the list
    manager.count_item(10)  # Counting occurrences of 10
    manager.count_item(100)  # Counting occurrences of a non-existing item
