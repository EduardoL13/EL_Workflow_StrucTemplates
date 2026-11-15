# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:46:43 2026

@author: ELC
"""


# Import material and geometry
import ModulesEL.englib.material as mat
import ModulesEL.englib.profile as geo

# Import math basic functions
from ModulesEL.mathE.generalFunctions import *

# Import Structural Library functions
import ModulesEL.structural.solidMechanics as sm
from ModulesEL.structural.beamFuncs import *

unitsSystem = "IMP"

# Geometric Parameters

heightPost = 16 # [ft]
heightPost = heightPost*12 #[in]

heightWindArea = 8 #[ft]
heightWindArea = heightWindArea*12 #[in]

widthWindArea = 2 #[ft]
widthWindArea = widthWindArea*12 #[in]

diaPost = 4 #[in]
thkPost = 0.25 #[in]

# Material Parameters

# Aluminium 5052-H32
E_Al = 10.2e06 #[psi]
yieldStress_Al = 28000 #[psi]
density_Al = 0.0968 #[lb/in^3]
poisson_Al = 0.33

# Stainless Steel 304
E_SS = 28e06 #[psi]
yieldStress_SS = 30000 #[psi]
density_SS = 0.289 #[lb/in^3]
poisson_SS = 0.3

# Steel ASTM A500
E_St = 50e06 #[psi]
yieldStress_St = 50000 #[psi]
density_St = 0.284 #[lb/in^3]
poisson_St = 0.3


# Geometry object declaration
post = geo.circular()
post.setProfile(diaPost,thkPost)

matAl = mat.customMaterial(E_Al, density_Al,"IMP")
matSS = mat.customMaterial(E_SS, density_SS,"IMP")
matSt = mat.customMaterial(E_St, density_St,"IMP")

# Wind Pressure Boundary conditions
# PREGUNTAR A CHATGPT SI EL PUEDE PONER EL DATO DIRECTAMENTE SI LE DOY LA RUTA
windPressure = 38.7 # [psf]
windPressure = windPressure * 1/144 #[psi]

#Calculations of Bending Stress At Base
loadWind = windPressure*heightWindArea*widthWindArea #[lb]
momentAtBase = loadWind*heightPost #[lb*in]
bendingStress = sm.bendStress(momentAtBase, post)

print("Maximum bending stess at base [psi]",bendingStress)
