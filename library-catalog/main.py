import csv
import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from library import Library

from models import Book
      
def find_by_title(title_query):
    """
    Find books whose title contains the query string(case-sensitive)
    """
    results = []
    query = title_query.lower()

    for book in isbn_index.values():
        if query in book.title.lower():
            results.append(book)

    return results

def measure_search_time(csv_path, search_term, step=500):
    """
    Measure how search time grows as more books are loaded.
    """
    base_library = Library()
    base_library.load_books_from_csv(csv_path)
    all_books = list(base_library.isbn_index.values())

    timings = []

    for size in range(step, len(all_books)+1, step):
        test_library = Library()

        for book in all_books[:size]:
            test_library.add_book(book)

        start = time.perf_counter()
        find_by_title(search_term)
        end = time.perf_counter()

        timings.append({
            "Books Loaded": size, 
            "Search Time (seconds)": end - start
        })
    
    return pd.DataFrame(timings)

def plot_search_time(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(8,5))
    sns.lineplot(
        data=df,
        x="Books Loaded",
        y="Search Time (seconds)",
        marker="o"
    )

    plt.title("Search Time vs Number of Books")
    plt.xlabel("Number of Books")
    plt.ylabel("Search Time (seconds)")
    plt.tight_layout()
    plt.show()

def find_by_author(author_name):
    """
    Return all books by a given author.
    """
    return author_index.get(author_name, [])

if __name__ == "__main__":
    csv_path = "data/Books.csv"
    search_term = "python"

    df = measure_search_time(csv_path, search_term, step=500)
    print(df)

    plot_search_time(df)
