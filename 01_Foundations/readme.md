# Foundations of Machine and Network

**Goal:** Understand how computers, operating systems, and networks actually work before writing any networked software. The event loop, database I/O, and distributed systems all rest on these primitives.

---

## Core Concepts

### Operating System Fundamentals

- Process vs thread: address space isolation, context switching cost, scheduling
- Memory layout: stack (fixed size, thread-local), heap (dynamic, shared), data segment


### Networking Fundamentals

- OSI model: why layers exist, what each layer adds (encapsulation)
- IP: addressing, subnets, routing basics, NAT
- TCP vs UDP: reliability guarantees, ordering, flow control, when each is appropriate
- TCP three-way handshake and its latency cost (1 RTT before data)
- TCP TIME_WAIT: why it exists, why it causes port exhaustion, tuning implications
- TCP flow control vs congestion control: receiver window vs CWND
- DNS: recursive vs iterative resolution, TTL, propagation delay, why DNS failures cascade
- Ports and sockets: socket lifecycle (bind, listen, accept, connect, close)
- RTT, bandwidth, latency: why they are different things and why both matter

### Command Line and Automation

- Shell scripting: variables, loops, conditionals, pipes, redirection
- Process management: ps, top, htop, lsof, strace
- Network tools: curl, ping, traceroute, netstat, ss, tcpdump (read-level)
- Text processing: awk, sed, grep, sort, uniq — essential for log analysis
- Git: branching, rebasing, cherry-pick, squash, bisect, reflog

---
