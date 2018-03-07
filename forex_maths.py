class FOREX_calcs:

    def leverage_to_margin(lev):
        for leverage in lev:
            for i, j in lev:
                margin = '%007.003f' % (j/i * 100)
        return margin

    def margin_to_leverage(mar):
        for i in mar:
            num = round((100/i))
        leverage = [(num, 1)]
        return leverage

    def convert_to_USD(currency_pair, profit):
        return profit_USD

    def profit_USD(units, buy_price, sell_price):

        convert_to_USD(currency_pair, profit)
        return (profit, profit_USD)

    def total_equity(cash, op_profits, op_losses):
        """Total Equity = Cash + Open Position Profits - Open Position Losses"""

    def margin_requirement():
        """Margin Requirement = Current Price × Units Traded × Margin"""

    def pips():
        """a pip is equal to .01% of the quote currency, thus, 10,000 pips = 1 unit of currency"""
