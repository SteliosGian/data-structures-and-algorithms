class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        """
        Get item at index

        Args:
            index: Index number
        """
        return self.data[index]

    def push(self, item):
        """
        Push item at the end of the array

        Args:
            item: Item to push
        """
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        """
        Remove last item of the array
        """
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def delete(self, index):
        """
        Delete item at specified index. O(1)

        Args:
            index: Index number
        """
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        """
        Shift items one position starting from position at index

        Args:
            index: Index number
        """
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

    def len(self):
        """
        Return length of the array
        """
        return self.length

    def __str__(self):
        """
        Format to print the array
        """
        return str(self.data)


new_array = MyArray()

new_array.push('hi')
new_array.push('you')
new_array.push('!')

new_array.delete(0)

new_array.push('are')
new_array.push('nice')

new_array.delete(1)

print(new_array)
