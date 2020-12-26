from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *

import threading
import time

import pandas as pd


class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print('The next valid order id is: ', self.nextorderId)

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
              'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


def error_handler(msg):
    print ('Server Error: %s' % msg)

def reply_handler(msg):
    print ('Server Response: %s, %s' % (msg.typeName, msg))

def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 1)
app.nextorderId = None
# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

# Check if the API is connected via orderid
while True:
    if isinstance(app.nextorderId, int):
        print('connected')
        break
    else:
        print('waiting for connection')
        time.sleep(1)

# Cancel all previously open orders - helps in testing
print('Cancel open orders ...')
app.reqGlobalCancel()
time.sleep(5)

df = pd.read_csv('C:\\Users\\CXM\\Desktop\\Vistalytics\\VBalTrades.csv', header=0)
for index, row in df.iterrows():
    contract = Contract()
    contract.symbol = df.Symbol[index]
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'
    contract.primaryExchange = "NYSE"

    order = Order()
    order.action = df.Signal[index]
    order.totalQuantity = df.Quantity[index]
    order.orderType = 'MKT'
    order.referenceExchangeId = 'SMART'
    app.placeOrder(app.nextorderId, contract, order)
    print('Order placed ...')
    # Cancel order - for test only
    # print('cancelling order')
    # app.cancelOrder(app.nextorderId)
    app.nextorderId += 1

# Cancel all the open orders
# print('Cancel open orders ...')
# app.reqGlobalCancel()
time.sleep(3)
print('Disconnecting ...')
app.disconnect()