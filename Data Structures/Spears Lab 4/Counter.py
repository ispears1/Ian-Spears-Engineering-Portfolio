#A class that creates a counter object to count comparisons and exchanges
class Counter:

    #Initialization fucntion
    def __init__(self):
        self.comparisons = 0
        self.exchanges = 0

    #A function that increments comparisons
    def incrementComparisons(self):
        self.comparisons += 1

    #A function that increments exchanges
    def incrementExchanges(self):
        self.exchanges += 1

    #A function that resets comparisons and exchanges
    def reset(self):
        self.comparisons = 0
        self.exchanges = 0