# eriu-security-blog

The **Eriu Technology** security-awareness series: short, story-led, plain-English briefings on the threats that actually hit small businesses. Each one has a story, a one-page poster and an explainer. Awareness and defence only, with no build instructions.

**Read it:** https://lolo737.github.io/eriu-security-blog/

## The 17 briefings

1. [**Plug & Prey**](https://lolo737.github.io/eriu-security-blog/plug-and-prey/): BadUSB and the found USB stick.
2. [**Free Wi-Fi, Dear Price**](https://lolo737.github.io/eriu-security-blog/free-wifi/): Public and rogue Wi-Fi, evil twins.
3. [**Wire & Deceit**](https://lolo737.github.io/eriu-security-blog/wire-and-deceit/): How business email compromise quietly reroutes your money — and the one phone call that stops it.
4. [**The Phish & Chips**](https://lolo737.github.io/eriu-security-blog/the-phish-and-chips/): How a single convincing email hands over the keys — and how to spot it before you click.
5. [**Held to Ransom**](https://lolo737.github.io/eriu-security-blog/held-to-ransom/): How ransomware takes a business hostage — and why the backup you've never restored is just a prayer.
6. [**Keys to the Kingdom**](https://lolo737.github.io/eriu-security-blog/keys-to-the-kingdom/): Why reusing passwords hands over everything — and why MFA is the cheapest insurance you'll ever buy.
7. [**The Voice on the Phone**](https://lolo737.github.io/eriu-security-blog/the-voice-on-the-phone/): AI voice-clones and deepfakes have given CEO fraud a human voice — here's how not to be fooled.
8. [**The Leaving Do**](https://lolo737.github.io/eriu-security-blog/the-leaving-do/): The accounts, keys and access that outlive an employee — and why offboarding is a security job, not just HR's.
9. [**Cloudy with a Chance of Breach**](https://lolo737.github.io/eriu-security-blog/cloudy-with-a-chance-of-breach/): Microsoft 365 and Google account takeover — and the 'approve this app' box that hands over the keys.
10. [**Shadow IT**](https://lolo737.github.io/eriu-security-blog/shadow-it/): Every app a staff member signs up for holds a piece of your business — here's how to see the ones you can't.
11. [**Patch or Perish**](https://lolo737.github.io/eriu-security-blog/patch-or-perish/): Why 'remind me tomorrow' leaves a door open at the back of the house — and how to stop the snooze.
12. [**The Lost Laptop**](https://lolo737.github.io/eriu-security-blog/the-lost-laptop/): A lost laptop is an inconvenience if it's encrypted — and a data breach if it isn't.
13. [**The Smart Office**](https://lolo737.github.io/eriu-security-blog/the-smart-office/): Printers, cameras and routers are full computers on your network — and the ones nobody ever secures.
14. [**GDPR for the Terrified**](https://lolo737.github.io/eriu-security-blog/gdpr-for-the-terrified/): What data protection actually asks of a small Irish business — in plain words, without the jargon.
15. [**Command Not Found**](https://lolo737.github.io/eriu-security-blog/command-not-found/): A ‘no internet’ fault on a Linux laptop, and how to think your way through it layer by layer — whatever the operating system.
16. [**Host in the Shell**](https://lolo737.github.io/eriu-security-blog/host-in-the-shell/): Hypervisors, VMs, containers, Citrix and AVD: what runs on what, in plain English, with pictures.
17. [**The Gateway Distro**](https://lolo737.github.io/eriu-security-blog/the-gateway-distro/): The everyday Ubuntu commands, animated, and the handful of habits that keep a Linux laptop safe.

Also on the site: [Wurzel and the One Night](https://lolo737.github.io/eriu-security-blog/wurzel-and-the-night-shift/), the story of how Eriu was set up in a night, and a few checklists.

## How each briefing is built

A story-led intro in a personal voice, a cinematic one-page poster, then a plain-English explainer: what it is, how it works, why it's dangerous, how you stop it. Dark cyber look with cyan, amber, red and green accents.

Each post lives in its own folder (`index.html`, `poster.html`, the poster PNG and a Markdown copy). The copy sits in `tools/blog_content.py` and `tools/gen_blog.py` builds the pages, so adding a post means adding an entry and running the generator.

## Run it locally

Open `index.html` in a browser. There is no build step for reading.

## Licence and status

Written by Niall O'Hara for [Eriu Technology](https://eriu.tech), an IT and cyber security consultancy for small organisations in Fingal and north Dublin. Awareness and defence only. Not legal advice.
