from vk import VK
import random

gid = 123123
token = "your_token"


def get_api():
    vk = VK(access_token=token)
    api = vk.get_api()
    return api


def get_vk():
    vk = VK(access_token=token)
    return vk


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])