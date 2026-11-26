# Neon diagrams for the "Host in the Shell" briefing (synthwave palette to match the poster).
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","host-in-the-shell")
PK,CY,AM,GN,YL="#ff3d9a","#22e6d6","#ffa63d","#8cff7a","#ffe27a"
INK,DK,PANEL="#fdf3ff","#12001f","#240a45"
HF="Oswald,'Arial Narrow',Impact,sans-serif"
BF="Inter,Helvetica,Arial,sans-serif"
DEFS=f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b0638"/><stop offset=".6" stop-color="#3a0a62"/><stop offset="1" stop-color="#7a1470"/></linearGradient>
<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2a0"/><stop offset=".5" stop-color="#ffb04a"/><stop offset="1" stop-color="#ff2d8f"/></linearGradient>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<mask id="sm"><rect width="200" height="200" fill="#fff"/><g fill="#000"><rect y="112" width="200" height="4"/><rect y="132" width="200" height="6"/><rect y="154" width="200" height="8"/><rect y="178" width="200" height="12"/></g></mask>
</defs>'''
def tx(x,y,s,fill=INK,fs=18,w=700,anchor="middle",font=BF,ls=0):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{fs}" font-weight="{w}" font-family="{font}" letter-spacing="{ls}">{s}</text>'
def neon(x,y,w,h,col,lines=(),fs=18,fill=PANEL,tc=INK,rx=14,sw=2.5,font=BF,fw=700):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{col}" stroke-width="{sw}" filter="url(#glow)"/>'
    n=len(lines)
    for i,l in enumerate(lines):
        yy=y+h/2+fs*0.35-(n-1)*fs*0.6+i*fs*1.2
        s+=tx(x+w/2,yy,l,tc,fs,fw,font=font)
    return s
def solid(x,y,w,h,col,text,tc=DK,fs=18,rx=14,font=BF):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{col}" filter="url(#glow)"/>'+tx(x+w/2,y+h/2+fs*0.35,text,tc,fs,800,font=font)
def pill(cx,y,text,col,w=300,fs=22):
    return f'<rect x="{cx-w/2}" y="{y}" width="{w}" height="38" rx="19" fill="{DK}" stroke="{col}" stroke-width="2.5" filter="url(#glow)"/>'+tx(cx,y+27,text,col,fs,800,font=HF,ls=2)
def frame(w,h,body,title,sun=True):
    grid="".join(f'<line x1="0" y1="{h-60+i*i*1.6}" x2="{w}" y2="{h-60+i*i*1.6}" stroke="{PK}" stroke-opacity=".18"/>' for i in range(1,8))
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">{DEFS}<rect width="{w}" height="{h}" rx="22" fill="url(#bg)"/>'
    if sun: s+=f'<g opacity=".16" transform="translate({w/2-100},{h/2-100})"><circle cx="100" cy="100" r="96" fill="url(#sun)" mask="url(#sm)"/></g>'
    s+=grid+body+f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="21" fill="none" stroke="{PK}" stroke-opacity=".5" stroke-width="2"/></svg>'
    return s
def vmcard(x,y,w,h,app="App",os_="Guest OS"):
    s=neon(x,y,w,h,GN,fill="#0d2a28",sw=2.5)+tx(x+w/2,y+18,"VM",GN,13,800,font=HF,ls=2)
    s+=solid(x+8,y+26,w-16,(h-38)*0.42,AM,app,fs=13,rx=8)+solid(x+8,y+26+(h-38)*0.42+5,w-16,(h-38)*0.58-5,"#b8a9e8",os_,fs=12,rx=8)
    return s
def arrowd(x,y1,y2,col=CY):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{col}" stroke-width="3" stroke-dasharray="7 5"/><polygon points="{x},{y2} {x-8},{y2-12} {x+8},{y2-12}" fill="{col}"/>'
def brace(x,y1,y2,label,col=YL):
    return (f'<path d="M{x} {y1} q10 0 10 10 v{(y2-y1)/2-20} q0 10 10 10 q-10 0 -10 10 v{(y2-y1)/2-20} q0 10 -10 10" fill="none" stroke="{col}" stroke-width="2.5"/>'
            +tx(x+24,(y1+y2)/2-2,label.split("|")[0],col,15,800,"start",HF,1)+tx(x+24,(y1+y2)/2+18,label.split("|")[1],col,15,800,"start",HF,1))

# ---------- 1. Type 1 vs Type 2 ----------
b=tx(450,44,"KIND 1 &amp; 2: THE HYPERVISOR",YL,30,800,font=HF,ls=3)
b+=tx(450,70,"the software that cuts one real machine into several virtual ones",INK,15,500)
# left: type 1
b+=pill(225,92,"TYPE 1 · BARE METAL",PK,300)
b+=neon(40,430,370,50,CY,["HARDWARE (the real box)"],17)
b+=solid(40,372,370,50,PK,"HYPERVISOR  ·  is the OS",tc="#fff",fs=18)
for i in range(3): b+=vmcard(40+i*125,220,120,142)
b+=brace(420,372,430,"0 | LAYERS",YL) if False else ""
b+=tx(225,512,"ESXi · Hyper-V · KVM / Proxmox",CY,17,800)
b+=tx(225,535,"Meet it in: the server room, the data centre",INK,14,500)
# right: type 2
b+=pill(675,92,"TYPE 2 · HOSTED",AM,300)
b+=neon(490,430,370,50,CY,["HARDWARE (the real box)"],17)
b+=solid(490,372,370,50,"#b8a9e8","HOST OS  (Windows / macOS)",fs=17)
b+=solid(490,314,370,50,PK,"HYPERVISOR  ·  just an app",tc="#fff",fs=18)
for i in range(2): b+=vmcard(490+i*190,148,180,156)
b+=tx(675,512,"VirtualBox · VMware Workstation · Parallels",AM,17,800)
b+=tx(675,535,"Meet it in: your laptop, a lab, a test rig",INK,14,500)
# comparison strip
b+=neon(40,552,820,62,YL,[],fill=DK)
b+=tx(450,578,"THE TEST: count the layers between the hardware and the VM",YL,16,800,font=HF,ls=1.5)
b+=tx(450,602,"Type 1 = hypervisor only.   Type 2 = host OS, then hypervisor.",INK,15,600)
open(f"{D}/diagram-hypervisors.svg","w").write(frame(900,632,b,"Type 1 hypervisors run directly on the hardware; Type 2 run as an app on a host operating system"))

# ---------- 2. VM vs container ----------
b=tx(450,44,"KIND 3: VM vs CONTAINER",YL,30,800,font=HF,ls=3)
b+=tx(450,70,"both split one machine up, but they share different amounts",INK,15,500)
b+=pill(225,92,"VIRTUAL MACHINE",PK,300)
b+=neon(40,372,370,50,CY,["HARDWARE"],17)+solid(40,314,370,50,PK,"HYPERVISOR",tc="#fff",fs=18)
for i in range(3):
    x=40+i*125
    b+=solid(x,258,120,48,"#b8a9e8","Guest OS",fs=14,rx=10)+solid(x,202,120,48,AM,"App",fs=15,rx=10)
b+=tx(225,456,"A whole computer in a box",PK,19,800,font=HF,ls=1)
b+=tx(225,480,"Own operating system each",INK,14,500)
b+=pill(675,92,"CONTAINER",AM,300)
b+=neon(490,372,370,50,CY,["HARDWARE"],17)+solid(490,314,370,50,"#b8a9e8","HOST OS · ONE SHARED KERNEL",fs=16)
b+=solid(490,258,370,48,PK,"CONTAINER ENGINE  (Docker)",tc="#fff",fs=16)
for i in range(3): b+=solid(490+i*125,202,120,48,AM,"App",fs=15,rx=10)
b+=tx(675,456,"A locked room in a shared building",AM,19,800,font=HF,ls=1)
b+=tx(675,480,"Shares the host's kernel",INK,14,500)
# chips
rows=[("SIZE","Gigabytes","Megabytes"),("STARTS","Minutes","Seconds"),("ISOLATION","Strong","Lighter")]
for i,(k,a,c) in enumerate(rows):
    y=500+i*34
    b+=neon(40,y,820,28,YL,[],fill=DK,rx=8,sw=1.5)
    b+=tx(450,y+19,k,YL,13,800,font=HF,ls=2)+tx(225,y+19,a,INK,15,700)+tx(675,y+19,c,INK,15,700)
open(f"{D}/diagram-vm-container.svg","w").write(frame(900,612,b,"A virtual machine carries its own guest OS; containers share the host kernel"))

# ---------- 3. Delivery layer ----------
b=tx(450,44,"KIND 4: THE DELIVERY LAYER",YL,30,800,font=HF,ls=3)
b+=tx(450,70,"Citrix, AVD, Horizon: how the screen reaches you",INK,15,500)
# user device
b+=neon(30,104,230,170,CY,[],fill=PANEL)
b+=tx(145,134,"YOUR COMPUTER",CY,17,800,font=HF,ls=2)
b+=neon(52,146,186,98,AM,[],fill=DK,rx=8,sw=2)+tx(145,184,"a window",AM,16,800)+tx(145,206,"showing the app",INK,14,500)+tx(145,228,"that lives elsewhere",INK,14,500)
b+=tx(145,262,"laptop · thin client · home PC",INK,12,500)
# delivery
b+=neon(335,104,230,170,PK,[],fill=PANEL)
b+=tx(450,134,"DELIVERY LAYER",PK,17,800,font=HF,ls=2)
b+=solid(355,148,190,34,PK,"CITRIX",tc="#fff",fs=16)+solid(355,188,190,34,PK,"AVD",tc="#fff",fs=16)+solid(355,228,190,34,PK,"HORIZON",tc="#fff",fs=16)
# server
b+=neon(640,104,230,170,GN,[],fill=PANEL)
b+=tx(755,134,"THE SERVER",GN,17,800,font=HF,ls=2)
b+=solid(660,146,190,34,"#b8a9e8","hypervisor",fs=15,rx=8)
b+=solid(660,188,88,56,GN,"VM",fs=15,rx=8)+solid(762,188,88,56,GN,"VM",fs=15,rx=8)+tx(755,262,"the app runs here",INK,12,500)
def arr(x1,x2,y,lab):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{CY}" stroke-width="3" stroke-dasharray="8 6"/><polygon points="{x2},{y} {x2-12},{y-8} {x2-12},{y+8}" fill="{CY}"/>'+tx((x1+x2)/2,y-12,lab,INK,12,600))
b+=arr(262,333,190,"screen")+arr(567,638,190,"connects")
# busted stamp
b+=f'<g transform="rotate(-3 450 318)"><rect x="170" y="296" width="560" height="44" rx="10" fill="{PK}" filter="url(#glow)"/>'+tx(450,326,"BUSTED: CITRIX IS NOT A HYPERVISOR",INK,22,800,font=HF,ls=2)+'</g>'
b+=tx(450,370,"You get the screen, not the machine. The files stay on the server. Simple as.",INK,16,700)
cards=[("PUBLISHED APP","one program,","streamed to your window",AM,"The usual Citrix setup"),("VDI","your own VM desktop","one VM per person",GN,"Personal desktop, remote"),("RDS / SESSION HOST","everyone shares","one server OS",CY,"A busy shared server")]
for i,(a,l1,l2,col,eg) in enumerate(cards):
    x=30+i*290
    b+=neon(x,392,270,128,col,[],fill=PANEL)
    b+=tx(x+135,422,a,col,19,800,font=HF,ls=1.5)+tx(x+135,452,l1,INK,16,700)+tx(x+135,474,l2,INK,16,700)+tx(x+135,504,eg,col,13,600)
open(f"{D}/diagram-delivery.svg","w").write(frame(900,544,b,"Citrix, AVD and Horizon deliver desktops and apps from VMs on a hypervisor to the user's device"))

# ---------- 4. Spot the kind ----------
b=tx(450,44,"CHEAT CODE: WHICH KIND IS IT?",YL,30,800,font=HF,ls=3)
b+=tx(450,70,"ask the question on the left, get the answer on the right",INK,15,500)
rows=[("It runs straight on the server hardware","TYPE 1 HYPERVISOR","ESXi · Hyper-V · Proxmox",PK),
      ("It's an app I open on my laptop","TYPE 2 HYPERVISOR","VirtualBox · Workstation",AM),
      ("It shares the host's kernel and starts in seconds","CONTAINER","Docker · Kubernetes",GN),
      ("I just get a window onto something on a server","DELIVERY LAYER","Citrix · AVD · Horizon",CY)]
for i,(q,a,eg,col) in enumerate(rows):
    y=96+i*92
    b+=neon(30,y,420,76,col,[],fill=PANEL)+tx(240,y+46,q,INK,16,700)
    b+=f'<polygon points="488,{y+38} 468,{y+26} 468,{y+50}" fill="{col}" filter="url(#glow)"/>'
    b+=solid(496,y,374,76,col,"",rx=14)+tx(683,y+34,a,DK,23,800,font=HF)+tx(683,y+58,eg,DK,14,700)
b+=tx(450,478,"Hypervisors and containers split a machine. Citrix and AVD only deliver the screen.",YL,15,700)
open(f"{D}/diagram-which-kind.svg","w").write(frame(900,500,b,"Quick guide to telling Type 1, Type 2, containers and delivery layers apart"))

# ---------- 5. Changing a VM's resources ----------
b=tx(450,44,"LEVEL UP: GIVE A VM MORE",YL,30,800,font=HF,ls=3)
b+=tx(450,70,"the VM can't ask the server itself. You change it at the hypervisor.",INK,15,500)
b+=neon(30,96,250,150,GN,[],fill=PANEL)+tx(155,124,"THE VM",GN,18,800,font=HF,ls=2)+tx(155,156,"4 GB RAM",INK,17,700)+tx(155,180,"2 CPUs",INK,17,700)+tx(155,204,"80 GB disk",INK,17,700)+tx(155,232,"runs out of room",PK,13,700)
b+=neon(325,96,250,150,PK,[],fill=PANEL)+tx(450,124,"THE HYPERVISOR",PK,18,800,font=HF,ls=2)+tx(450,154,"Edit settings",INK,17,700)+tx(450,178,"set RAM, CPU, disk",INK,15,500)+tx(450,206,"vSphere · Hyper-V Manager",AM,13,700)+tx(450,226,"Proxmox · VirtualBox",AM,13,700)
b+=neon(620,96,250,150,CY,[],fill=PANEL)+tx(745,124,"THE SERVER (HOST)",CY,18,800,font=HF,ls=2)+tx(745,156,"a pool of real",INK,15,500)+tx(745,178,"CPU · RAM · disk",INK,17,700)+tx(745,206,"hands a bigger slice",INK,15,500)+tx(745,228,"to the VM",INK,15,500)
def ar(x1,x2,y,lab,col):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="3" stroke-dasharray="8 6"/><polygon points="{x2},{y} {x2-12},{y-8} {x2-12},{y+8}" fill="{col}"/>'+tx((x1+x2)/2,y-12,lab,INK,12,600))
b+=ar(282,323,171,"you ask",CY)+ar(577,618,171,"it gives",GN)
steps=[("1","SNAPSHOT","a save point, in case it goes wrong"),("2","POWER OFF","unless hot-add is switched on"),("3","EDIT SETTINGS","raise the RAM, CPUs or disk"),("4","POWER ON","check it boots and sees the new RAM"),("5","DISK ONLY","extend the partition inside the OS")]
for i,(n,a,c) in enumerate(steps):
    y=270+i*46
    b+=neon(30,y,840,38,YL if i<4 else AM,[],fill=DK,rx=10,sw=2)
    b+=f'<circle cx="62" cy="{y+19}" r="14" fill="{YL if i<4 else AM}"/>'+tx(62,y+25,n,DK,16,800,font=HF)
    b+=tx(92,y+25,a,YL if i<4 else AM,17,800,"start",HF,1.5)+tx(300,y+25,c,INK,15,600,"start")
b+=tx(450,520,"On a managed system you raise a ticket. The virtualisation team does steps 1 to 4.",INK,15,700)
b+=tx(450,545,"Containers are different: set the limit when you start them (docker run --memory 512m).",AM,14,600)
open(f"{D}/diagram-resources.svg","w").write(frame(900,572,b,"How to give a virtual machine more RAM, CPU or disk by editing its settings on the hypervisor"))
print("diagrams written")
