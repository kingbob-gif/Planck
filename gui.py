import tkinter as tk
import physics
from nodes import Button, Label, Entry

window = tk.Tk()
window.title("Plank")
window.geometry("600x200")

menu = tk.Frame(window)
tunnel_frame = tk.Frame(window)
entangle_frame = tk.Frame(window)
Energy_frame = tk.Frame(window)
wave_frame = tk.Frame(window)

E_clearT = tk.StringVar()
V0_clear = tk.StringVar()
m_clear = tk.StringVar()
a_clear = tk.StringVar()

s00_clear = tk.StringVar()
s01_clear = tk.StringVar()
s10_clear = tk.StringVar()
s11_clear = tk.StringVar()
A_clear = tk.StringVar()

WavR_clear = tk.StringVar()
WavI_clear = tk.StringVar()
E_clearW = tk.StringVar()
time_clear = tk.StringVar()

m_clearE = tk.StringVar()
L_clear = tk.StringVar()
n_clear = tk.StringVar()

def clear(x):
    if x == 1:
        tunnel_output.configure(text="")
        E_clearT.set("")
        V0_clear.set("")
        m_clear.set("")
        a_clear.set("")
    if x == 2:
        entangle_output.configure(text="")
        s00_clear.set("")
        s01_clear.set("")
        s10_clear.set("")
        s11_clear.set("")
        A_clear.set("")
    if x == 3:
        wave_output.configure(text="")
        WavR_clear.set("")
        WavI_clear.set("")
        E_clearW.set("")
        time_clear.set("")
    if x == 4:
        Energy_output.configure(text="")
        m_clearE.set("")
        L_clear.set("")
        n_clear.set("")

def clear_all():
    clear(1)
    clear(2)
    clear(3)
    clear(4)

def back():
    tunnel_frame.pack_forget()
    entangle_frame.pack_forget()
    wave_frame.pack_forget()
    Energy_frame.pack_forget()
    clear_all()
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

def Energy_setup():
    menu.pack_forget()
    Energy_frame.pack()

def calc_tunnel():
    try:
        E = float(E_entryT.get())
        V0 = float(V0_entry.get())
        m = float(m_entry.get())
        a = float(a_entry.get())
        answer = physics.tunnel(E, V0, m, a)
        tunnel_output.configure(text=answer)
    except ValueError:
        tunnel_output.configure(text="Please enter a Number in all fields")

def calc_entangle():
    try:
        s00 = float(s00_entry.get())
        s01 = float(s01_entry.get())
        s10 = float(s10_entry.get())
        s11 = float(s11_entry.get())
        A = float(A_entry.get())
        answer = physics.entangle(s00, s01, s10, s11, A)
        entangle_output.configure(text=answer)
    except ValueError:
        entangle_output.configure(text="Please enter a number in all fields")

def calc_wave():
    try:
        WavR = float(WavR_entry.get())
        WavI = float(WavI_entry.get())
        E = float(E_entryW.get())
        time = float(time_entry.get())
        answer = physics.wave(WavR, WavI, E, time)
        wave_output.configure(text=answer)
    except ValueError:
        wave_output.configure(text="Please enter a number in all fields")

def calc_Energy():
    try:
        m = float(m_entryE.get())
        L = float(L_entry.get())
        n = float(n_entry.get())
        answer = physics.Energy(m, L, n)
        Energy_output.configure(text=answer)
    except ValueError:
        Energy_output.configure(text="Please enter a number in all fields")

label = Label("Select a calculation", 0, 0, 1, menu)

tunnel_button = Button(tunnel_setup, "Determine the percent chance of quantum tunneling", 1, 0, menu)

entangle_button = Button(entangle_setup, "Measure an entangled particle", 2, 0, menu)

wave_button = Button(wave_setup, "evaluate the evolution of a wave function", 3, 0, menu)

Energy_button = Button(Energy_setup, "Measure particle in a box energy", 4, 0, menu)

tunnel_output = Label("", 0, 0, 2, tunnel_frame)

E_promptT = Label("Enter particles energy in J's", 1, 0, 1, tunnel_frame)

E_entryT = Entry(tunnel_frame, E_clearT, 1, 1)

V0_prompt = Label("Enter particle's potential barrier height in J's", 2, 0, 1, tunnel_frame)

V0_entry = Entry(tunnel_frame, V0_clear, 2, 1)

m_prompt = Label("Enter particle's mass in kg's", 3, 0, 1, tunnel_frame)

m_entry = Entry(tunnel_frame, m_clear, 3, 1)

a_prompt = Label("Enter particle's barrier width in m's", 4, 0, 1, tunnel_frame)

a_entry = Entry(tunnel_frame, a_clear, 4, 1)

submit_tunnel = Button(calc_tunnel, "Submit", 6, 1, tunnel_frame)

clear_tunnel = Button(lambda: clear(1), "Clear", 6, 0, tunnel_frame)

back_tunnel = Button(back, "Back", 7, 0, tunnel_frame)

entangle_output = Label("", 0, 0, 2, entangle_frame)

s00_prompt = Label("Enter the amplistude of state 00", 1, 0, 1, entangle_frame)

s00_entry = Entry(entangle_frame, s00_clear, 1, 1)

s01_prompt = Label("Enter the amplitude of state 01", 2, 0, 1, entangle_frame)

s01_entry = Entry(entangle_frame, s01_clear, 2, 1)

s10_prompt = Label("Enter the amplitude of state 10", 3, 0, 1, entangle_frame)

s10_entry = Entry(entangle_frame, s10_clear, 3, 1)

s11_prompt = Label("Enter the amplitude of state 11", 4, 0, 1, entangle_frame)

s11_entry = Entry(entangle_frame, s11_clear, 4, 1)

A_prompt = Label("Enter the measurement of particle A, 1 or 0", 5, 0, 1, entangle_frame)

A_entry = Entry(entangle_frame, A_clear, 5, 1)

submit_entangle = Button(calc_entangle, "Submit", 6, 1, entangle_frame)

clear_entangle = Button(lambda: clear(2), "Clear", 6, 0, entangle_frame)

back_entangle = Button(back, "Back", 7, 0, entangle_frame)

wave_output = Label("", 0, 0, 2, wave_frame)

WavR_entry = Label("Enter the normalized initial value of the wave function (real part)", 1, 0, 1, wave_frame)

WavR_entry = Entry(wave_frame, WavR_clear, 1, 1)

WavI_prompt = Label("Enter the normalized initial value of the wave function (imaginary part)", 2, 0, 1, wave_frame)

WavI_entry = Entry(wave_frame, WavI_clear, 2, 1)

E_promptW = Label("Enter the particle's energy in J's", 3, 0, 1, wave_frame)

E_entryW = Entry(wave_frame, E_clearW, 3, 1)

time_prompt = Label("How many seconds do you want to evaluate the wave function at", 4, 0, 1, wave_frame)

time_entry = Entry(wave_frame, time_clear, 4, 1)

submit_wave = Button(calc_wave, "Submit", 5, 1, wave_frame)

clear_wave = tk.Button(wave_frame, text="Clear", command=lambda: clear(3))
clear_wave.grid(row=5, column=0)

clear_wave = Button(lambda: clear(3), "Clear", 5, 0, wave_frame)

back_wave = Button(back, "Back", 6, 0, wave_frame)

Energy_output = Label("", 0, 0, 2, Energy_frame)

m_promptE = Label("Enter the particle's mass in kg's", 1 ,0, 1, Energy_frame)

m_entryE = Entry(Energy_frame, m_clearE, 1, 1)

L_prompt = Label("Enter the box length in m's", 2, 0, 1, Energy_frame)

L_entry = Entry(Energy_frame, L_clear, 2, 1)

n_prompt = Label("Enter the quantum number", 3, 0, 1, Energy_frame)

n_entry = Entry(Energy_frame, n_clear, 3, 1)

submit_Energy = Button(calc_Energy, "Submit", 4, 1, Energy_frame)

clear_Energy = tk.Button(Energy_frame, text="Clear", command=lambda: clear(4))
clear_Energy.grid(row=4, column=0)

clear_Energy = Button(lambda: clear(4), "Clear", 4, 0, Energy_frame)

back_Energy = tk.Button(Energy_frame, text="Back", command=back)
back_Energy.grid(row=5, column=0)

back_Energy = Button(back, "Back", 5, 0, Energy_frame)

menu.pack()

window.mainloop()