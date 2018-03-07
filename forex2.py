import forex_maths as fx

lev = [(75, 1)] #tuple with leverage at 50: 1
mar = [(1.333)]
print(fx.FOREX_calcs.leverage_to_margin(lev),'%')
print(fx.FOREX_calcs.margin_to_leverage(mar))
