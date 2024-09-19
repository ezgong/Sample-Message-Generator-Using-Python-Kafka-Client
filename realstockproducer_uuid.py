from faker.providers import BaseProvider
import random
import time
from yahoo_fin import stock_info as si
import uuid
from datetime import datetime 

StockNames = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "DOGE-USD"]


class RealStockProvider_uuid(BaseProvider):
    def stock_name(self):
        return random.choice(StockNames)

    def stock_value(self, stockname):
        nextval = si.get_live_price(stockname)
        return nextval

    def produce_msg(self):
        stockname = self.stock_name()
        ts = time.time()
        message = {
            "message_uuid": str(uuid.uuid4()),
            "stock_name": stockname,
            "stock_value": self.stock_value(stockname),
            "message_timestamp": str(datetime.now().astimezone().isoformat()),
        }
        key = {"stock_name": stockname}
        return message, key
