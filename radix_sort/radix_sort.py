# An implementation of the Radix Sort algorithm by Michael Galliers.
from array_queue import ArrayQueue


# Inherit Queue ADT class to make some modifications for RadixSort.
class RadixQueue(ArrayQueue):
    # Override default size to allow for bigger lists to be sorted.
    DEFAULT_CAPACITY = 50

    # Override constructor to add an extra attribute.
    def __init__(self):
        # Ensure super constructor is still called.
        super().__init__()
        # Attribute that defines number of items remaining in queue from previous intermediate sort.
        self.rem = 0


# For handling sorting of lists using the Radix algorithm.
class RadixSort:
    def __init__(self):
        # Create list of 10 Radix Queues for sorting purposes.
        self.queues = [RadixQueue() for x in range(10)]

    # Sort a list of positive integers using the Radix algorithm.
    def sort(self, data):
        """

        :type data: list
        """
        # Counter for the sum of all digits at the current significant digit.
        sum_dig = 1
        # For tracking the current significant digit being sorted by (starting at ones place).
        sig_dig = 1
        # Initially load all digits into the '0' queue.
        for item in data:
            self.queues[0].enqueue(item)
        # Set remaining digits value in '0' queue to its size.
        self.queues[0].rem = len(self.queues[0])
        # Continue sorting until current significant digit is beyond any numbers being sorted.
        while sum_dig > 0:
            # Reset sum to zero before beginning iteration of sorting.
            sum_dig = 0
            # Handle numbers in each of the 10 queues.
            for queue in self.queues:
                # Handle all remaining numbers from previous intermediate sort in current queue.
                while queue.rem > 0:
                    # Decrement remaining number val in current queue.
                    queue.rem -= 1
                    # Pull a number off the queue.
                    num = queue.dequeue()
                    # Extract the current significant digit of that number.
                    dig = (num // sig_dig) % 10
                    # Increment significant digit sum by this digit.
                    sum_dig += dig
                    # Place number into queue with significant digit matching index.
                    self.queues[dig].enqueue(num)
            # Reset remaining value in each queue to the size of that queue.
            for queue in self.queues:
                queue.rem = len(queue)
            # Update current significant digit place to one higher.
            sig_dig *= 10
        # Once loop above is complete, all numbers will be sorted in '0' queue from least to greatest,
        # from end to beginning of queue.
        # Pull all numbers out of '0' queue back into original list in sorted order.
        for i in range(len(data)):
            data[i] = self.queues[0].dequeue()
        # Return sorted list (still same object passed to function).
        return data


if __name__ == '__main__':
    # Create RadixSort object.
    radix = RadixSort()
    # Print some information about the program.
    print('Welcome to an implementation of the Radix Sort algorithm by Michael Galliers')
    print('Please enter comma separated lists of positive integers (whitespace is ignored).')
    # Set to False when the user wants to exit.
    restart = True
    # User input loop.
    while restart:
        # Prompt the user for a list of numbers.
        raw = input('Enter list: ')
        # Parse into a Python list object, ignoring whitespace and converting to integers.
        data = [int(x.strip()) for x in raw.split(',')]
        # Sort it.
        data = radix.sort(data)
        # Print result.
        print('The sorted version of your list is:\n{0}'.format(str(data)))
        # Ask if user wants to enter another list of values.
        answer = input('Would you like to enter another list of numbers? (y, n): ')
        # If they do not want to proceed, update restart var to False.
        if answer.lower() == 'n':
            restart = False
            print('Thank you for using the program.')
