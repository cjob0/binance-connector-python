import math
import time
# API - Key
key = "DRbGDc52WF7yP3MXft0CAzyD7XXQFige4Z9g6leWBbGJx2fXD51O7B6axzdaprqe"
# 签名
secret = "HsMocfj0qqxjC2dATl6o6wbCEE9b9iH3ctzksTFIndCt3jfVEHwTzAeE071UqkiJ"
# 本地代理
proxies = {'https': 'http://127.0.0.1:4780'}
# 当前时间戳，毫秒
timestamp = math.floor(time.time() * 1000)
