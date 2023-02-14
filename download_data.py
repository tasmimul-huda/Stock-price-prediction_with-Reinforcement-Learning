import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

yahoo_financials = YahooFinancials('TSLA')

# train_df = yahoo_financials.get_historical_price_data(start_date='2013-01-01', 
#                                                   end_date='2022-12-31', 
#                                                   time_interval='daily')
# train_df = pd.DataFrame(train_df['TSLA']['prices'])
# train_df = train_df.drop('date', axis=1).set_index('formatted_date')
# train_df.to_csv('data/train.csv')

test_df = yahoo_financials.get_historical_price_data(start_date='2020-01-01', 
                                                  end_date='2023-01-01', 
                                                  time_interval='daily')
test_df = pd.DataFrame(test_df['TSLA']['prices'])
test_df = test_df.drop('date', axis=1).set_index('formatted_date')
test_df.to_csv('data/test.csv')