# Azure Virtual Networks

A VNet provides a private network boundary for supported Azure resources.

When planning a VNet:
1. Choose an address range that does not overlap with connected networks.
2. Divide it into suitable subnets.
3. Plan required inbound and outbound flows.
4. Plan DNS before configuring private endpoints.
5. Document the network design.

Do not create a VNet just to tick a box. Understand which resources will connect to it and how.
