from vk_bot.base.enums import BaseEnum


class ProxyType(BaseEnum):
    SOCKS5 = 'socks5'
    HTTPS = 'https'

    values = {
        SOCKS5: 'socks5',
        HTTPS: 'https'
    }
