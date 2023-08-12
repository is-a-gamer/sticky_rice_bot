import json
import os

_channel_bind_data = None

def init():
    """
    初始化通道绑定
    """
    global _channel_bind_data
    # 从配置文件中读取通道绑定信息
    # 如果文件不存在,创建新文件 并返回空字典
    if not os.path.exists('channel_bind.json'):
        with open('.channel_bind.json', 'w+', encoding='utf-8') as f:
            json.dump({}, f)
            _channel_bind_data = {}
            return {}
    with open('channel_bind.json', 'r', encoding='utf-8') as f:
        _channel_bind_data = json.load(f)


def get_data():
    global _channel_bind_data
    if _channel_bind_data is None:
        _channel_bind_data = init()
    return _channel_bind_data


def add_channel_bind(server_id: str, channel_id: str):
    global _channel_bind_data
    _channel_bind_data[server_id] = channel_id
    with open('.channel_bind.json', 'w+', encoding='utf-8') as f:
        json.dump({}, f)
        _channel_bind_data = {}
        return {}
