.. _domain-search-list:

Domain-search-list
==================

This sections adds domain names to the domain search list sent to the
client. If there are multiple sections of this type then they will be
combined into one set of domain names which is sent to the client.


Example
-------

.. code-block:: dhcpkitconf

    <domain-search-list>
        domain-name example.com
        domain-name example.net
        domain-name example.org
    </static-csv>

.. _domain-search-list_parameters:

Section parameters
------------------

domain-name (required, multiple allowed)
    The domain name to add to the search list.

    **Example**: "example.com"
