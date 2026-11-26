# Diagrams for the "Guests of the Host" briefing (house palette, dark panels, rounded boxes).
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","guests-of-the-host")
CY,AM,RD,GN,LAV,INK="#00dbcc","#ffb81a","#f54447","#40ea99","#b8a9e8","#d7e7ea"
F='font-family="Inter,Helvetica,Arial,sans-serif"'
def box(x,y,w,h,fill,text,tc="#02141a",fs=17,weight=700,stroke="none",rx=14):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    if text:
        lines=text.split("\n"); n=len(lines)
        for i,l in enumerate(lines):
            yy=y+h/2+fs*0.35-(n-1)*fs*0.6+i*fs*1.2
            s+=f'<text x="{x+w/2}" y="{yy}" text-anchor="middle" fill="{tc}" font-size="{fs}" font-weight="{weight}" {F}>{l}</text>'
    return s
def t(x,y,s,fill=INK,fs=18,weight=400,anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{fs}" font-weight="{weight}" {F}>{s}</text>'
def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><rect width="{w}" height="{h}" rx="18" fill="#04161b" stroke="rgba(0,219,204,.35)" stroke-width="2"/>{body}</svg>'
def hw(x): return box(x,330,370,52,"#1d3b46","HARDWARE",INK,19,700,CY)
def vm(x,y,w,h,label_y_off=20):
    # green VM card with a label, an app and a guest OS inside
    s=box(x,y,w,h,GN,"")+t(x+w/2,y+19,"VM","#02141a",15,700)
    s+=box(x+10,y+28,w-20,32,AM,"App",fs=14)+box(x+10,y+66,w-20,h-76,LAV,"Guest OS",fs=13)
    return s

# 1. Type 1 vs Type 2
b=t(225,40,"TYPE 1 · BARE METAL",AM,24,700)+t(675,40,"TYPE 2 · HOSTED",AM,24,700)
st=""
st+=hw(40)+box(40,268,370,52,RD,"HYPERVISOR","#fff",19)
for i in range(3): st+=vm(40+i*125,138,120,120)
st+=hw(490)+box(490,268,370,52,LAV,"HOST OS  (Windows / macOS)","#02141a",17)+box(490,206,370,52,RD,"HYPERVISOR APP","#fff",19)
for i in range(2): st+=vm(490+i*190,76,180,120)
st+=t(225,418,"ESXi · Hyper-V · KVM / Proxmox",INK,17,700)+t(225,442,"Servers and data centres",INK,16)
st+=t(675,418,"VirtualBox · VMware Workstation · Parallels",INK,17,700)+t(675,442,"Laptops, labs and testing",INK,16)
b+=f'<g transform="translate(0,-8)">{st}</g>'
open(f"{D}/diagram-hypervisors.svg","w").write(svg(900,448,b,"Type 1 hypervisors run on the hardware; Type 2 run as an app on a host operating system"))

# 2. VM vs container
b=t(225,40,"VIRTUAL MACHINE",AM,24,700)+t(675,40,"CONTAINER",AM,24,700)
st=hw(40)+box(40,268,370,52,RD,"HYPERVISOR","#fff",19)
for i in range(3):
    x=40+i*125
    st+=box(x,214,120,44,LAV,"Guest OS",fs=14)+box(x,160,120,44,AM,"App",fs=15)
st+=hw(490)+box(490,268,370,52,LAV,"HOST OS  ·  one shared kernel","#02141a",17)+box(490,206,370,52,RD,"CONTAINER ENGINE  (Docker)","#fff",17)
for i in range(3): st+=box(490+i*125,152,120,44,AM,"App",fs=15)
st+=t(225,418,"Its own operating system each",INK,17,700)+t(225,442,"Heavy, strongly isolated",INK,16)
st+=t(675,418,"Shares the host's kernel",INK,17,700)+t(675,442,"Light, starts in seconds",INK,16)
b+=f'<g transform="translate(0,-72)">{st}</g>'
open(f"{D}/diagram-vm-container.svg","w").write(svg(900,400,b,"A virtual machine carries its own guest OS; containers share the host kernel"))

# 3. Delivery layer
b=t(450,46,"WHO RUNS IT, AND WHO DELIVERS IT",AM,22,700)
b+=box(30,100,200,150,"#0c2a31","",stroke=CY)
b+=t(130,150,"USER'S DEVICE",CY,15,700)+t(130,180,"laptop · thin client",INK,15)+t(130,204,"phone · home PC",INK,15)
b+=box(350,100,200,150,LAV,"DELIVERY LAYER\nCitrix · AVD\nHorizon","#02141a",17)
b+=box(670,100,200,150,"#0c2a31","",stroke=RD)+t(770,128,"HYPERVISOR",RD,15,700)
b+=box(690,142,70,92,GN,"VM",fs=15)+box(780,142,70,92,GN,"VM",fs=15)
def arrow(x1,x2,y,label):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{CY}" stroke-width="3" stroke-dasharray="8 6"/>'
            f'<polygon points="{x2},{y} {x2-12},{y-8} {x2-12},{y+8}" fill="{CY}"/>'+t((x1+x2)/2,y-14,label,INK,14))
b+=arrow(232,348,175,"screen + keys")+arrow(552,668,175,"connects to")
b+=t(450,290,"The user gets the screen, not the machine. The files stay on the server.",INK,17,700)
for i,(a,c1,c2,col) in enumerate([("PUBLISHED APP","Just one program","streamed to you",AM),("VDI","Own VM desktop","for each user",GN),("RDS / SESSION HOST","Everyone shares","one server OS",CY)]):
    x=30+i*290
    b+=box(x,320,270,110,"#0c2a31","",stroke=col)+t(x+135,356,a,col,16,700)+t(x+135,386,c1,INK,16)+t(x+135,408,c2,INK,16)
open(f"{D}/diagram-delivery.svg","w").write(svg(900,460,b,"Citrix, AVD and Horizon deliver desktops and apps from VMs on a hypervisor to the user's device"))
print("diagrams written")
