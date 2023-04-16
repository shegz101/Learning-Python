class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newAddress = ""
        for element in range(0, len(address)):
            present = address[element]
            if (present == "."):
                present = present.replace(present, "[.]")
            newAddress += present
        return newAddress