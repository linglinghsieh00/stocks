!pip install pandas_datareader

import os
import pandas_datareader as pdr
# 取得Google股票的價格，美股代號GOOG
df = pdr.get_data_tiingo('GOOG', api_key='f99ffa048e6615cc9537f36fec51769a4dcff494')
