"""
Option handlers for the DNS options defined in dhcpkit.ipv6.extensions.sntp
"""

import configparser
from ipaddress import IPv6Address

from dhcpkit.ipv6 import option_handler_registry
from dhcpkit.ipv6.extensions.sntp import SNTPServersOption
from dhcpkit.ipv6.option_handlers import SimpleOptionHandler, OptionHandler


class SNTPServersOptionHandler(SimpleOptionHandler):
    """
    Handler for putting SNTPServersOptions in responses
    """

    def __init__(self, sntp_servers: [IPv6Address]):
        option = SNTPServersOption(sntp_servers=sntp_servers)
        option.validate()

        super().__init__(option)

    # noinspection PyDocstring
    @classmethod
    def from_config(cls, section: configparser.SectionProxy, option_handler_id: str=None) -> OptionHandler:
        addresses = []
        for name, value in section.items():
            # Strip numbers from the end, this can be used to supply the same option multiple times
            name = name.rstrip('0123456789-')

            if name != 'server-address':
                continue

            addresses.append(IPv6Address(value))

        return cls(addresses)


option_handler_registry.register(SNTPServersOptionHandler)