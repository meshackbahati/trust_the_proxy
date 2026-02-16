# Trust the Proxy – G24Sec CTF Challenge

## Category
Web Exploitation

## Difficulty
Medium

## Description

A new internal dashboard was deployed behind a reverse proxy.  
Developers claim it is secure because access to `/admin` is restricted to localhost (`127.0.0.1`).

Can you bypass the restriction and retrieve the flag?

---

## Learning Objectives

- Understand why trusting client-supplied headers is dangerous
- Exploit misconfigured reverse proxy setups
- Bypass IP-based access control using `X-Forwarded-For`

---

## Vulnerability Overview

The application trusts the `X-Forwarded-For` header to determine if a request originates from `127.0.0.1`.

Since this header is client-controlled and not validated, an attacker can spoof it to gain unauthorized access.
