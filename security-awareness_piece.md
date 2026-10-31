---
title: "Plug & Prey — the trusted device that turns on you"
description: A plain-language guide to BadUSB / HID-injection attacks, for people who aren't security engineers.
author: Eriu Technology
date: 2026-10-31
tags: [security-awareness, badusb, hid, smb-security]
---

![Plug & Prey — BadUSB awareness poster](./security-awareness_piece.png)

## The device you already trust

Most security advice is about things you download: dodgy attachments, dodgy links, dodgy installers. So we train people not to click. Fair enough.

But there's a whole class of attack that never asks you to download a thing. It walks in the front door disguised as something you plug in every day — a memory stick, a mouse, a keyboard, even a charging cable — and your computer welcomes it without a word. It's called **BadUSB**, or an **HID-injection attack**, and this is the plain-English version of how it works and how you stop it.

## What it actually is

A BadUSB device is a peripheral that lies about what it is.

You plug it in, and instead of behaving like the mouse or stick it appears to be, it quietly tells the computer: *"I'm a keyboard."* In the trade that's a **Human Interface Device**, or HID. And here's the catch that makes the whole thing work — machines trust keyboards completely. No install. No warning. No click. A keyboard is assumed to be a human being typing, and humans are allowed to do anything.

## How the attack works

It's four beats, and it's quick:

1. **Plugged in.** It looks like an ordinary stick, mouse or cable. Nothing to see.
2. **It announces itself** to the system as a keyboard.
3. **The OS trusts it automatically** — no prompt, no scan, no question asked.
4. **It "types"** a burst of commands far faster than any human could.

In a few seconds it can open a foothold on the machine and then be pulled straight back out. There's no malicious file sitting on the disk afterwards — just a record of some keystrokes, if anyone even looks.

## Why it's genuinely nasty

- **There's nothing to scan.** Antivirus looks for malicious files. This isn't a file — it's keystrokes. There's nothing for the scanner to catch.
- **It's fast, then it's gone.** Seconds to run, then unplugged and out the door.
- **It beats "never download anything" training.** The whole attack needs no download, so the usual advice doesn't touch it.
- **The trust is permanent and built-in.** Every machine trusts its own keyboard, by default, forever. That's not a bug you can patch away — it's how computers are meant to work.

## Where it hides — the disguises

The flashy proof-of-concept gadget is only the demo. The same trick fits inside anything you'd plug in without thinking:

- a **USB memory stick**
- a **mouse**
- a **keyboard**
- a **charging or data cable**

If it plugs into a USB port, assume it *could* be one of these. The "found a USB stick in the car park" trope is a cliché precisely because it keeps working.

## How you shut it down

The good news: the defences are practical and mostly about policy and habit, not magic.

- **USB device control.** Allow-list the devices you approve, and block new HIDs by policy. This is the big one.
- **Lock down the ports.** Cap or physically block unused USB ports on exposed or public-facing machines; port blockers are cheap.
- **Never plug in strays.** No found sticks, no "free" cables at a conference, no mystery dongles. Ever.
- **Flag new keyboards.** Configure endpoints to prompt for approval when a brand-new keyboard suddenly appears.
- **Physical control and autorun off.** Keep machines where people can't quietly plug things in, and disable autorun.

---

*An Eriu Technology security briefing. This is an awareness piece — concept, risk and defence only. It contains no build instructions, and it's here so people recognise the attack and lock it out, not reproduce it.*
