#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for weight_1 in range(0, length):
        weight_2 = hash_table_retrieve(ht, limit - weights[weight_1])
        hash_table_insert(ht, weights[weight_1], weight_1)
        if weight_2 is not None:
            if weight_1 > weight_2:
                return [weight_1, weight_2]
            return [weight_2, weight_1]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
