# If earth were a blackbody with mean emission temperature T_e
# From the stephan boltzman law:

stephanBoltzmanConst = 5.67e-8 # W m^-2 K^-4

def EmissionTemperature(outgoingLongwaveRad):
    return (outgoingLongwaveRad/stephanBoltzmanConst)**0.25

# With global annual mean outgoing longwave radiation 238.5 W m_-22

earth_emissionTemp = EmissionTemperature(238.5)

print(f"Emission to space: {earth_emissionTemp} K")
print("Note that this is -18.5 C, much lower than the global mean temperature and hence earth as a blackbody is a bad assumption")
print("This is due to the greenhouse effect")