import os
import csv
from data_types import Purchase
import statistics

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------')
    print('    Real Estate Scrape ')
    print('------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'data.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # print('bed count: {}'.format(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases
        # print(purchases[0].__dict__)
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(row)


def get_price(p):
    return p.price


def query_data(data):
    # data.sort(key=get_price)

    data.sort(key=lambda p: p.price)
    # most expensive house
    high_purchase = data[-1]
    print('The most expensive is ${:,.2f}'.format(high_purchase.price))

    # least expensive house
    low_purchase = data[0]
    print('The cheapest is ${:,.2f}'.format(low_purchase.price))


    # average price house
    # prices = []
    # for pur in data:
        # prices.append(pur.price)
    
    prices = [
        p.price
        for p in data
    ]
    ave_price = statistics.mean(prices)
    print('The average price is ${:,.2f}'.format(ave_price))

    # average price 2 bedroom houses
    two_bed_homes = (p for p in data if p.beds == 2)

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sq_ft = statistics.mean((p.sq__ft for p in homes))
    print('The average price (2 bedroom) is ${:,.2f} // baths: {} // sq ft: {}'
    .format(ave_price, round(ave_baths, 1), round(ave_sq_ft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
