class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def FractionalKnapsack(items, weight):
    items.sort(key=lambda x: (x.profit/x.weight), reverse=True)

    finalProfit = 0
    finalWeights = [0 for i in range(len(items))]

    for i in range(len(items)):
        if items[i].weight <= weight:
            weight -= items[i].weight
            finalProfit += items[i].profit
            finalWeights[i] = 1

        else:
            finalWeights[i] = weight/items[i].weight
            finalProfit += items[i].profit * finalWeights[i]
            break

    return finalProfit, finalWeights

def main():
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
 
    # Function call
    max_val, weights = FractionalKnapsack(arr, W)
    print(max_val)
    print(weights)

main()