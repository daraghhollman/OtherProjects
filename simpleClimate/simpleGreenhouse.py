### LONGWAVE ###

# Tranmitivity of 0.61 was chosen to match observations

OLRobserved = 238.5 # W m^-2 (Outgoing longwave radiation)
stephanBoltzman = 5.67e-8 # W m^-2 K^-4
tempObserved = 288. # Global average surface temperature

def Transmitivity(OLR, T):
    return OLR / (stephanBoltzman * T**4)

transmitivity = Transmitivity(OLRobserved, tempObserved)

print(f"Transmitivity: {transmitivity}")

### SHORTWAVE ###

# Insolation = area-averaged incoming solar radiation
insolation = 341.3 # W m^-2

# Planetary albedo
fluxReflected = 101.9 # W m^-2 reflected shortwave flux

albedo = fluxReflected / insolation
print(f"Albedo: {albedo}")

# Absorbed shortwave reflection (ASR) = (1-albedo)*Q
ASRobserved = insolation - fluxReflected
print(f"ASR: {ASRobserved} W m^-2")

### EQUILIBRIUM TEMPERATURE ###
# Earth is in energy blanace when energy in = energy out: ASR = OLR

def EquilibirumTemperature(albedo, insolation, transmitivity):
    return ((1-albedo) * insolation / (transmitivity * stephanBoltzman))**0.25

equilibriumTempObserved = EquilibirumTemperature(albedo, insolation, transmitivity)
print(f"Equilibirum Temperature Observed: {equilibriumTempObserved} K")