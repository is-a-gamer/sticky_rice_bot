import json
import os

_ip_channel_bind_data = None

def init():
    """
    初始化通道绑定
    """
    global _ip_channel_bind_data
    # 从配置文件中读取通道绑定信息
    # 如果文件不存在,创建新文件 并返回空字典
    if not os.path.exists('.ip_change_channel.json'):
        with open('.ip_change_channel.json', 'w+', encoding='utf-8') as f:
            json.dump({}, f)
            _ip_channel_bind_data = {}
            return {}
    with open('.ip_change_channel.json', 'r', encoding='utf-8') as f:
        _ip_channel_bind_data = json.load(f)


def get_data():
    global _ip_channel_bind_data
    if _ip_channel_bind_data is None:
        _ip_channel_bind_data = init()
    return _ip_channel_bind_data
