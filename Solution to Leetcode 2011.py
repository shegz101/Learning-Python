class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Thought Process
        # X is first assigned a value of zero
        # loop through the array to detect the operations present
        # Increment or decrement based on the operation
        x = 0
        for i in range(0,len(operations)):
            if (operations[i] == '--X' or operations[i] == 'X--'):
                x = x - 1
            elif (operations[i] == '++X' or operations[i] == 'X++'):
                x = x + 1
        return x