
stockDict = {
  'APL': 'Apple',
  'MIC': 'Microsoft',
  'PPR': 'Pied Piper'
}

purchases = [
  ('APL', 100, '10-sep-2001', 48),
  ('MIC', 100, '1-apr-1999', 24),
  ('PPR', 200, '1-jul-1998', 56),
  ('APL', 80, '11-sep-2001', 44),
  ('APL', 300, '1-jun-1999', 26),
  ('PPR', 10, '1-dec-1998', 520)]

# Create a purchase history report that computes the full purchase price (share
# s times dollars) for each block of stock
# and uses the stockDict to look up the full company name. This is the basic re
# lational database join algorithm between two tables.


def create_purchase_history():
    for block in purchases:
        num_of_shares = block[1]
        price_per_share = block[3]

        full_name = stockDict[block[0]]
        total_price = num_of_shares * price_per_share

        history = ['you bought {0} shares'.format(num_of_shares)]
        history.append(' of %s stock ' % (full_name))
        history.append('at ${0}/each '.format(price_per_share))
        history.append('for a total of ${0}'.format(total_price))
        print(''.join(line for line in history))


create_purchase_history()


# Create a second purchase summary that which accumulates total investment by
# ticker symbol. In the above sample data, there are two blocks of GE. These ca
# n easily be combined by creating a dict where the key is the ticker and the v
# alue is the list of blocks purchased. The program makes one pass through the
# data to create the dict. A pass through the dict can then create a report sho
# wing each ticker symbol and all blocks of stock.

summary = dict()
for (key, value) in stockDict.items():
    summary[key] = 0

for block in purchases:
    total = block[1] * block[3]
    summary[block[0]] += total
    print(summary)
