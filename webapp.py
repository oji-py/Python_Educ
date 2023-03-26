import streamlit as st
from molmass import Formula, ELEMENTS, Element, FormulaError

def molarity(mol_solute, volume):
    return mol_solute/volume
    
def molality(mol_solute, mass_solvent):
    mol_solute = float(mol_solute)
    mass_solvent= float(mass_solvent)
    return mol_solute/mass_solvent
    
def mole_fraction(mol_solute, mol_solvent):
    mol_solute = float(mol_solute)  # this works because you can't directly call the parameters as floats.
    mol_solvent = float(mol_solvent)  # the parameters and variables in functions are local
    solution_tot = mol_solute + mol_solvent
    return mol_solute/solution_tot
    
def molar_mass(comp):
    formula = Formula(comp)
    molarmass = formula.mass
    return molarmass

def vol_conversion(volume, orig_unit, new_unit):
    volume = float(volume)
    if orig_unit.upper() == "ML" and new_unit.upper() == "L":
        return volume/1000
    elif orig_unit.upper() == "G" and new_unit.upper() == "L":
        return volume/1000
def mass_conversion(mass, orig_unit, new_unit):
    mass = float(mass)
    if orig_unit.upper() == "G" and new_unit.upper() == "KG":
        return mass/1000
    elif orig_unit.upper() == "ML" and new_unit.upper() == "KG":
        return mass/1000
    
    


is_running = True
st.title("MOLE FRACTION, MOLARITY, MOLALITY, AND PPM CALCULATOR")
st.markdown("""
***Personal coding project for practice. Integrates knowledge from Chemistry classes and coding tutorials.***

""")
while is_running:
    try:
        user_inp = st.selectbox("General Chemistry 2 Calculator: ", ["Mole Fraction", "Molarity", "Molality"], key="1s")
        if user_inp == "Molarity":
            solute = st.text_input("Enter the chemical formula for the solute properly: ", key="1p")
            # case matter in code, there are things that are negligible like space, but indents and cases are strictly not.
            solute_ask = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="2s")
            if solute_ask == "Grams [g]":
                solute_mass = float(st.number_input("Enter the mass of the solute [g]: ", key="1d"))
                solution_unit = st.selectbox("Is the solution in mL or L? ", ["Milliliters [mL]", "Liters [L]"], key="3s")
                molmass = molar_mass(solute)
                moles_solute = solute_mass/molmass  
                if solution_unit == "Milliliters [mL]":
                    solution_volume = float(st.number_input("Enter the volume of the solution [mL]: ", key="2p"))
                    solution_volume_L = vol_conversion(solution_volume, "ML", "L")
                    answer = molarity(moles_solute, solution_volume_L)
                    st.markdown(f"Answer: {answer}M or mol/L")
                elif solution_unit == "Liters [L]":
                    solution_volume = float(st.number_input("Enter the volume of the solution [L]: ", key="3p"))
                    answer = molarity(moles_solute, solution_volume)
                    st.markdown(f"Answer: {answer}M or mol/L")
                else: 
                    pass
            elif solute_ask == "Moles [mol]":
                solute_moles = float(st.number_input("Enter the moles of the solute: ", key="4"))
                solution_unit = st.selectbox("Is the solution in mL or L? ", ["Milliliters [mL]", "Liters [L]"], key="4")
                if solution_unit == "Milliliters [mL]":
                    solution_volume = float(st.number_input("Enter the volume of the solution [mL]: ", key="5"))
                    solution_volume_L = vol_conversion(solution_volume, "ML", "L")
                    answer = molarity(solute_moles, solution_volume_L)
                    st.markdown(f"Answer: {answer}M or mol/L")
                elif solution_unit == "Liters [L]":
                    solution_volume = float(st.number_input("Enter the volume of the solution [L]: ", key="6"))
                    answer = molarity(solute_moles, solution_volume) 
                    st.markdown(f"Answer: {answer}M or mol/L")
                else:
                    pass
            else:
                pass
                
        
        elif user_inp == "Mole Fraction":
            solute_mf = st.text_input("Enter the chemical formula for the solute properly: ", key="2")
            solute_askmf = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="5")
            if solute_askmf == "Grams [g]":
                solute_mass_mf = float(st.number_input("Enter the grams of the solute: ", key="7"))
                solvent_mf = st.text_input("Enter the chemical formula for the solvent properly: ", key="3")
                solvent_askmf = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="6")
                molmass_mf = molar_mass(solute_mf)
                moles_solute = solute_mass_mf/molmass_mf
                if solvent_askmf == "Grams [g]":
                    solvent_mass_mf = float(st.number_input("Enter the grams of the solvent: ", key="8"))
                    molmass_solvent_mf = molar_mass(solvent_mf)
                    moles_solvent = solvent_mass_mf/molmass_solvent_mf
                    answer = mole_fraction(moles_solute, moles_solvent)
                    st.markdown(f"Answer: {answer}")
                elif solvent_askmf == "Moles [mol]":
                    solvent_mole_mf = float(st.number_input("Enter the moles of the solvent: ", key="9"))
                    answer = mole_fraction(moles_solute, solvent_mole_mf)
                    st.markdown(f"Answer: {answer}")
            elif solute_askmf == "Moles [mol]":
                solute_mole_mf = float(st.number_input("Enter the moles of the solute: ", key="10"))
                solvent_mf = st.text_input("Enter the chemical formula for the solvent properly: ", key="4")
                solvent_askmf = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="7")
                if solvent_askmf == "Grams [g]":
                    solvent_mass_mf = float(st.number_input("Enter the grams of the solvent: ", key="11"))
                    molmass_solvent_mf = molar_mass(solvent_mf)
                    moles_solvent = solvent_mass_mf/molmass_solvent_mf
                    answer = mole_fraction(solute_mole_mf, moles_solvent)
                    st.markdown(f"Answer: {answer}")
                elif solvent_askmf == "Moles [mol]":
                    solvent_mole_mf = float(st.number_input("Enter the moles of the solvent: ", key="12"))
                    answer = mole_fraction(solute_mole_mf, solvent_mole_mf)
                    st.markdown(f"Answer: {answer}M")
        elif user_inp == "Molality":
            solute_ml = st.text_input("Enter the chemical formula for the solute properly: ", key="5")
            solute_askml = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="8")
            solvent_ml = st.text_input("Enter the chemical formula for the solvent properly: ", key="6")
            solvent_askml = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Kilograms [Kg]", "Moles [mol]"], key="9")
            if solute_askml == "Grams [g]":
                solute_mass_ml = float(st.number_input("Enter the grams of the solute: ", key="13"))
                molmass_ml = molar_mass(solute_ml)
                moles_solute = solute_mass_ml/molmass_ml
                if solvent_askml == "Kilograms [Kg]":  # == is for the condition
                    solvent_massml = st.number_input("Enter the kilograms of the solvent: ", key="14")  # equal to the number enterede in the input not the input
                    molality(moles_solute, solvent_massml)
                elif solvent_askml == "Grams [g]":
                    solvent_massml = st.number_input("Enter the grams of the solvent: ", key="15")
                    solvent_massml_kg = solvent_massml/1000
                    molality(moles_solute, solvent_massml_kg)
                elif solvent_askml == "Moles [mol]":
                    solvent_molml = st.number_input("Enter the moles of the solvent: ", key="16")
                    molarmass = molar_mass(solute_ml)
                    solvent_massml_kg = (solvent_molml * molarmass)/1000
                    molality(moles_solute, solvent_massml_kg)
            elif solute_askml == "Moles [mol]":
                solute_molml = st.number_input("Enter the moles of the solute: ", key="17")
                if solvent_askml == "Kilograms [Kg]":  # == is for the condition
                    solvent_massml = st.number_input("Enter the kilograms of the solvent: ", key="18")  # equal to the number enterede in the input not the input
                    molality(solute_molml, solvent_massml)
                elif solvent_askml == "Grams [g]":
                    solvent_massml = st.number_input("Enter the grams of the solvent: ", key="19")
                    solvent_massml_kg = solvent_massml/1000
                    molality(solute_molml, solvent_massml_kg)
                elif solvent_askml == "Moles [mol]":
                    solvent_molml = st.number_input("Enter the moles of the solvent: ", key="20")
                    molarmass = molar_mass(solute_ml)
                    solvent_massml_kg = (solvent_molml * molarmass)/1000
                    molality(solute_molml, solvent_massml_kg)
                else:
                    pass
                
    except FormulaError:
        st.markdown("**Enter a valid chemical formula.**")
    
        





