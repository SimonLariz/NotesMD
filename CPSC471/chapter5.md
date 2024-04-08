## Chapter 5: Network Layer

## Network Layer Functions
- Forwarding: Move packets from router's input to appropriate router output
- Routing: Determine route taken by packets from source to destination

- Per-router control plane: Individual routing algorithm components in each and every router (traditional routing algorithms)
- Logically centralized control plane: Network-wide logic in a single place (software-defined networking)

## Per-router control plane
- Individual routing algorithm components in each and every router
- Router will have information on nearby routers and the cost to reach them

## Software Defined Networking (SDN)
- Remote controller computes, installs routing tables in routers
- OpenFlow: Protocol for remote controllers to modify routing tables
