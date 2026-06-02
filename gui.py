import tkinter as tk
import physics

window = tk.Tk()
window.title("quantum calculator")
window.geometry("600x200")

menu = tk.Frame(window)
tunnel_frame = tk.Frame(window)
entangle_frame = tk.Frame(window)
wave_frame = tk.Frame(window)

def back():
    tunnel_frame.pack_forget()
    entangle_frame.pack_forget()
    wave_frame.pack_forget()
    menu.pack()

def tunnel_setup():
    menu.pack_forget()
    tunnel_frame.pack()

def entangle_setup():
    menu.pack_forget()
    entangle_frame.pack()

def wave_setup():
    menu.pack_forget()
    wave_frame.pack()

def calc_tunnel():
    try:
        E = float(E_entryT.get())
        V0 = float(V0_entry.get())
        m = float(m_entry.get())
        a = float(a_entry.get())
        h = float(h_entryT.get())
        answer = physics.tunnel(E, V0, m, a, h)
        tunnel_output.config(text=answer)
    except ValueError:
        tunnel_output.config(text="Please enter a Number in all fields")

def calc_entangle():
    try:
        s00 = float(s00_entry.get())
        s01 = float(s01_entry.get())
        s10 = float(s10_entry.get())
        s11 = float(s11_entry.get())
        A = float(A_entry.get())
        answer = physics.entangle(s00, s01, s10, s11, A)
        entangle_output.config(text=answer)
    except ValueError:
        entangle_output.config("Please enter a number in all fields")

def calc_wave():
    try:
        WavR = float(WavR_entry.get())
        WavI = float(WavI_entry.get())
        h = float(h_entryW.get())
        E = float(E_entryW.get())
        time = float(time_entry.get())
        answer = physics.wave(WavR, WavI, h, E, time)
        wave_output.config(text=answer)
    except ValueError:
        wave_output.config(text="Please enter a number in all fields")

label = tk.Label(menu, text="select a calculation")
label.grid(row=0, column=0)

tunnel_button = tk.Button(menu, text="Determine the percent chance of quantum tunneling", command=tunnel_setup)
tunnel_button.grid(row=1, column=0)

entangle_button = tk.Button(menu, text="Measure an entangled particle", command=entangle_setup)
entangle_button.grid(row=2, column=0)

wave_button = tk.Button(menu, text="Evaluate the evolution of a wave function", command=wave_setup)
wave_button.grid(row=3, column=0)

tunnel_output = tk.Label(tunnel_frame)
tunnel_output.grid(row=0, column=0, columnspan=2)

E_promptT = tk.Label(tunnel_frame, text="Enter particle's energy in J's")
E_promptT.grid(row=1, column=0)

E_entryT = tk.Entry(tunnel_frame)
E_entryT.grid(row=1, column=1)

V0_prompt = tk.Label(tunnel_frame, text="Enter particle's potential barrier height in J's")
V0_prompt.grid(row=3, column=0)

V0_entry = tk.Entry(tunnel_frame)
V0_entry.grid(row=3, column=1)

m_prompt = tk.Label(tunnel_frame, text="Enter particle's mass in kg's")
m_prompt.grid(row=4, column=0)

m_entry = tk.Entry(tunnel_frame)
m_entry.grid(row=4, column=1)

a_prompt = tk.Label(tunnel_frame, text="Enter particle's barrier width in m's")
a_prompt.grid(row=5, column=0)

a_entry = tk.Entry(tunnel_frame)
a_entry.grid(row=5, column=1)

h_promptT = tk.Label(tunnel_frame, text="Enter the reduced Planck constant in joules times seconds")
h_promptT.grid(row=6, column=0)

h_entryT = tk.Entry(tunnel_frame)
h_entryT.grid(row=6, column=1)

submit_tunnel = tk.Button(tunnel_frame, text="Submit", command=calc_tunnel)
submit_tunnel.grid(row=7, column=1)

back_tunnel = tk.Button(tunnel_frame, text="Back", command=back)
back_tunnel.grid(row=7, column=0)

entangle_output = tk.Label(entangle_frame)
entangle_output.grid(row=0, column=0, columnspan=2)

s00_prompt = tk.Label(entangle_frame, text="Enter the amplitude of state 00")
s00_prompt.grid(row=1, column=0)

s00_entry = tk.Entry(entangle_frame)
s00_entry.grid(row=1, column=1)

s01_prompt = tk.Label(entangle_frame, text="Enter the amplitude of state 01")
s01_prompt.grid(row=2, column=0)

s01_entry = tk.Entry(entangle_frame)
s01_entry.grid(row=2, column=1)

s10_prompt = tk.Label(entangle_frame, text="Enter the amplitude of state 10")
s10_prompt.grid(row=3, column=0)

s10_entry = tk.Entry(entangle_frame)
s10_entry.grid(row=3, column=1)

s11_prompt = tk.Label(entangle_frame, text="Enter the amplitude of state 11")
s11_prompt.grid(row=4, column=0)

s11_entry = tk.Entry(entangle_frame)
s11_entry.grid(row=4, column=1)

A_prompt = tk.Label(entangle_frame, text="Enter measurement of particle A, 1 or 0")
A_prompt.grid(row=5, column=0)

A_entry = tk.Entry(entangle_frame)
A_entry.grid(row=5, column=1)

submit_entangle = tk.Button(entangle_frame, text="Submit", command=calc_entangle)
submit_entangle.grid(row=6, column=1)

back_entangle = tk.Button(entangle_frame, text="Back", command=back)
back_entangle.grid(row=6, column=0)

wave_output = tk.Label(wave_frame)
wave_output.grid(row=0, column=0, columnspan=2)

WavR_prompt = tk.Label(wave_frame, text="Enter the normalized initial value of the wave function (real part)")
WavR_prompt.grid(row=1, column=0)

WavR_entry = tk.Entry(wave_frame)
WavR_entry.grid(row=1, column=1)

WavI_prompt = tk.Label(wave_frame, text="Enter the normalized initial value of the wave function (imaginary part)")
WavI_prompt.grid(row=2, column=0)

WavI_entry = tk.Entry(wave_frame)
WavI_entry.grid(row=2, column=1)

h_promptW = tk.Label(wave_frame, text="Enter the reduced Planck constant in joules times seconds")
h_promptW.grid(row=3, column=0)

h_entryW = tk.Entry(wave_frame)
h_entryW.grid(row=3, column=1)

E_promptW = tk.Label(wave_frame, text="Enter the particle's energy in J's")
E_promptW.grid(row=4, column=0)

E_entryW = tk.Entry(wave_frame)
E_entryW.grid(row=4, column=1)

time_prompt = tk.Label(wave_frame, text="How many seconds do you want to calculate the wave function at")
time_prompt.grid(row=5, column=0)

time_entry = tk.Entry(wave_frame)
time_entry.grid(row=5, column=1)

submit_wave = tk.Button(wave_frame, text="Submit", command=calc_wave)
submit_wave.grid(row=6, column=1)

back_wave = tk.Button(wave_frame, text="Back", command=back)
back_wave.grid(row=6, column=0)

menu.pack()

window.mainloop()