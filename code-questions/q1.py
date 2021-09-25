# Sample coding question 1: 
# Given an array of strings products and a string searchWord. 
# We want to design a system that suggests at most three product names
# from products after each character of searchWord is typed. 
# Suggested products should have common prefix with the searchWord. 
# If there are more than three products with a common prefix return the three 
# lexicographically minimums products. 
# Return list of lists of the suggested products after each character of searchWord 
# is typed. (solution)
import random
from typing import List


def filter_by_lex(items: List, size: int = 3):
    """
    Selects lexicographically minimums products.
    """
    sorted_items = sorted(items)
    return sorted_items[:size]


def recommendations_v1(products: List, search_word: str):
    """
    Suggests products given a list of products and a search word.

    Suggested products have a common prefix with the search_word.
    At most, 3 products are returned.

    Solution has complexity O(n) = n.log(n) + n (for all searchs).
    It's not optimal.
    """
    search_results = []
    for product in products:
        if product.startswith(search_word):
            search_results.append(product)

    search_results = filter_by_lex(search_results, size=3)
    return search_results


def binary_search(words: List, prefix: str):
    """
    Performs a binary search that finds the start position of words with given prefix.

    Assumes words is an ordered list.
    """
    i, j = 0, len(words)
    while i < j:
        mid = (j + i) // 2

        if words[mid][:len(prefix)] >= prefix:
            j = mid
        else:
            i = mid + 1
    return i


def recommendations_v2(products: List, search_word: str):
    """
    Suggests products given a list of products and a search word.

    Suggested products have a common prefix with the search_word.
    At most, 3 products are returned.
    
    Sort products beforehand, then perform a binary search on the 
    array in order to find the first element.

    Solution has complexity log(n) (for all searchs), and n.log(n) during creation time.
    """    
    sorted_products = sorted(products)

    start_index = binary_search(sorted_products, search_word)
    return sorted_products[start_index:start_index + 3]


if __name__ == "__main__":
    random.seed(2509)
    products = ["bata", "batata", "bateria", "tomate", "tomada", "tombola", "tocador", "texugo"]
    random.shuffle(products)
    search_word = input("Enter a subword: ")
    rec_1 = recommendations_v1(products, search_word)
    print(f"rec_1 = {rec_1}")
    rec_2 = recommendations_v2(products, search_word)
    print(f"rec_2    = {rec_2}")
