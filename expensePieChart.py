import matplotlib.pyplot as plt

def main():
    categories = {'Rent': 1000, 'Gas': 250, 'Food': 350, 'Clothing': 200, 'Car Payment': 375, 'Misc': 800}

    try:
        labels = list(categories.keys())
        sizes = [categories[label] for label in labels]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, startangle=90)
        ax.axis('equal')  
        plt.title('Monthly Expenses Distribution')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
