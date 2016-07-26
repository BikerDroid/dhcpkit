0.9.1 - Unreleased
------------------

New features
^^^^^^^^^^^^

- It is now possible to use IDNs everywhere in DHCPKit, including configuration files.
- Implement a domain socket to control the server process.
- Added :ref:`ipv6-dhcpctl` to control the server process through the domain socket.
- Added a configuration section ``<statistics>`` to specify categories that you would like statistics on. Currently it is
  possible to gather statistics per interface, client subnet or relay.
- Added ``stats`` and ``stats-json`` commands for `ipv6-dhcpctl`.

Changes for users
^^^^^^^^^^^^^^^^^

- Create PID file /var/run/ipv6-dhcpd.pid by default.
- Create domain socket /var/run/ipv6-dhcpd.sock control the server by default.

Changes for developers
^^^^^^^^^^^^^^^^^^^^^^

- Added support for Internationalized Domain Names (IDN) in :meth:`~dhcpkit.utils.parse_domain_bytes` and
  :meth:`~dhcpkit.utils.encode_domain`.
- Created ForOtherServerError as a subclass of CannotRespondError, to enable more accurate logging, and to make it
  possible to gather better statistics.
- Replaced :attr:`.IncomingPacketBundle.interface_id` ``bytes``
  with :attr:`~.IncomingPacketBundle.interface_name` ``str``,
  providing :attr:`~.IncomingPacketBundle.interface_id` for backwards compatibility.
- Added :attr:`~.TransactionBundle.relays` property to more easily enumerate all the relays a message went through.
- Moved responsibility of creating the :class:`.TransactionBundle` from the :class:`.MessageHandler` to :mod:`.worker`.
  It gives a cleaner API and helps with statistics counting.
- Added :mod:`.statistics` and updated :mod:`.worker` and :class:`.MessageHandler` to update relevant counters.


0.9.0 - 2016-07-16
------------------

- A complete rewrite of the DHCPv6 server with a new configuration style.