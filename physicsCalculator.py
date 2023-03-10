import numpy as np

# Constants go here

# STANDARD PHYSICS

c = 299_792_458 # m s⁻¹ // Speed of light in a vacuum

G = 6.674_30e-11 # N m² Kg⁻¹ // Universal Gravitation Constant

e = 1.602_176_634e-19 # C // Elementary Charge

# QUANTUM MECHANICS

h = 6.626_070_15e-34 # J s // Planck's Constant
h_eV = 4.135_667_696_9e-15 # eV s // ^^^

hbar = h / (2 * np.pi) # J s // Reduced Planck's Constant
hbar_eV = h_eV / (2 * np.pi) # eV s // ^^^

constsList = [c, G, e, h, h_eV, hbar, hbar_eV]

# Functions

def J2eV(numberInJoules):
    
    numberInElectronVolts = numberInJoules / e # Divide by the fundamental charge

    return numberInElectronVolts