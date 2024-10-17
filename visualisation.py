import pandas as pd
import matplotlib.pyplot as plt
from stockmarket_eod import get_eod_data, generate_eod_data_table

def plot_line_graph(data):
	fig, ax = plt.subplots()

	for i in range(len(data)):
		open_price = data['Open'][i]
		close_price = data['Close'][i]
		percent_change = data['Change'][i]
		symbol = data['Symbol'][i]
		
		ax.plot([0, 1], [open_price, close_price], marker='o', label=symbol)
		ax.annotate(f'{percent_change}%', xy=(0.5, (open_price + close_price) / 2),
					xytext=(0.5, (open_price + close_price) / 2 + 1),
					arrowprops=dict(facecolor='black', shrink=0.05),
					ha='center')

	ax.set_xticks([0, 1])
	ax.set_xticklabels(['Open', 'Close'])
	ax.set_xlabel('Price Type')
	ax.set_ylabel('Price')
	ax.set_title('Stock Market Data')
	ax.legend()
	plt.show()

def plot_bar_graph(data):
    fig, ax = plt.subplots()

    index = range(len(data))
    percent_changes = data['Change']

    bars = ax.bar(index, percent_changes, label='Percentage Change')

    ax.set_xlabel('Symbol')
    ax.set_ylabel('Percentage Change')
    ax.set_title('Stock Market Data')
    ax.set_xticks(index)
    ax.set_xticklabels(data['Symbol'])
    ax.legend()

    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom')

    plt.show()

def main():
	input_companies = input("Enter the companies you would like to see latest stock prices on (comma-separated list, e.g., ACN, AAPL): ")
	access_key = input("Enter your access key for MarketStack (https://marketstack.com/signup/free): ")

	if not input_companies:
		companies = pd.read_csv("it_companies.csv")["Symbol"].tolist()
		input_companies = ",".join(companies)

	company_data = get_eod_data(input_companies, access_key)
	data_table = generate_eod_data_table(company_data)

	stockmarket_df = pd.DataFrame(data_table)
	stockmarket_df.to_csv("open_close.csv", index=False)
	print("Data saved to open_close.csv")

	plot_type = input("Enter 'line' to see a line graph or 'bar' to see a bar graph: ").strip().lower()
	if plot_type == 'line':
		plot_line_graph(stockmarket_df)
	elif plot_type == 'bar':
		plot_bar_graph(stockmarket_df)
	else:
		print("Invalid input. Please enter 'line' or 'bar'.")

if __name__ == "__main__":
	main()