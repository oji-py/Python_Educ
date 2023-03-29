import streamlit as st
from molmass import Formula, ELEMENTS, Element, FormulaError

st.set_page_config(page_title = "General Chemistry 2 Calculator", layout = "wide", initial_sidebar_state = "collapsed")

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

ppm_solu = lambda solu, soln: (solu/soln)*10**6
def ppm (mass_solute, mass_solvent):
    mass_solute = float(mass_solute)
    mass_solvent = float(mass_solvent)
    mass_solution = mass_solute + mass_solvent
    return (mass_solute/mass_solution)*10**6
    
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

try:
    user_inp = st.selectbox("General Chemistry 2 Calculator: ", ["Mole Fraction", "Molarity", "Molality", "PPM"], key = "ones")
    if user_inp == "Molarity":
        solute = st.text_input("Enter the chemical formula for the solute properly: ", key="twot")
        # case matter in code, there are things that are negligible like space, but indents and cases are strictly not.
        solute_ask = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="twos")
        if solute_ask == "Grams [g]":
            solute_mass = float(st.number_input("Enter the mass of the solute [g]: ", key="onei"))
            solution_unit = st.selectbox("Is the solution in mL or L? ", ["Milliliters [mL]", "Liters [L]"], key="threes")
            molmass = molar_mass(solute)
            moles_solute = solute_mass/molmass  
            if solution_unit == "Milliliters [mL]":
                solution_volume = float(st.number_input("Enter the volume of the solution [mL]: ", key="twoi"))
                solution_volume_L = vol_conversion(solution_volume, "ML", "L")
                answer = molarity(moles_solute, solution_volume_L)
                st.markdown(f"Answer: {answer}M or mol/L")
            elif solution_unit == "Liters [L]":
                solution_volume = float(st.number_input("Enter the volume of the solution [L]: ", key="threei"))
                answer = molarity(moles_solute, solution_volume)
                st.markdown(f"Answer: {answer}M or mol/L")
            else: 
                pass
        elif solute_ask == "Moles [mol]":
            solute_moles = float(st.number_input("Enter the moles of the solute: ", key="fouri"))
            solution_unit = st.selectbox("Is the solution in mL or L? ", ["Milliliters [mL]", "Liters [L]"], key="fours")
            if solution_unit == "Milliliters [mL]":
                solution_volume = float(st.number_input("Enter the volume of the solution [mL]: ", key="fivei"))
                solution_volume_L = vol_conversion(solution_volume, "ML", "L")
                answer = molarity(solute_moles, solution_volume_L)
                st.markdown(f"Answer: {answer}M or mol/L")
            elif solution_unit == "Liters [L]":
                solution_volume = float(st.number_input("Enter the volume of the solution [L]: ", key="sixi"))
                answer = molarity(solute_moles, solution_volume) 
                st.markdown(f"Answer: {answer}M or mol/L")
            else:
                pass
        else:
            pass      
    
    elif user_inp == "Mole Fraction":
        solute_mf = st.text_input("Enter the chemical formula for the solute properly: ", key="twot")
        solute_askmf = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="fives")
        if solute_askmf == "Grams [g]":
            solute_mass_mf = float(st.number_input("Enter the grams of the solute: ", key="seveni"))
            solvent_mf = st.text_input("Enter the chemical formula for the solvent properly: ", key="threet")
            solvent_askmf = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="sixs")
            molmass_mf = molar_mass(solute_mf)
            moles_solute = solute_mass_mf/molmass_mf
            if solvent_askmf == "Grams [g]":
                solvent_mass_mf = float(st.number_input("Enter the grams of the solvent: ", key="eighti"))
                molmass_solvent_mf = molar_mass(solvent_mf)
                moles_solvent = solvent_mass_mf/molmass_solvent_mf
                answer = mole_fraction(moles_solute, moles_solvent)
                st.markdown(f"Answer: {answer}")
            elif solvent_askmf == "Moles [mol]":
                solvent_mole_mf = float(st.number_input("Enter the moles of the solvent: ", key="ninei"))
                answer = mole_fraction(moles_solute, solvent_mole_mf)
                st.markdown(f"Answer: {answer}")
        elif solute_askmf == "Moles [mol]":
            solute_mole_mf = float(st.number_input("Enter the moles of the solute: ", key="teni"))
            solvent_mf = st.text_input("Enter the chemical formula for the solvent properly: ", key="fourt")
            solvent_askmf = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="sevens")
            if solvent_askmf == "Grams [g]":
                solvent_mass_mf = float(st.number_input("Enter the grams of the solvent: ", key="eleveni"))
                molmass_solvent_mf = molar_mass(solvent_mf)
                moles_solvent = solvent_mass_mf/molmass_solvent_mf
                answer = mole_fraction(solute_mole_mf, moles_solvent)
                st.markdown(f"Answer: {answer}")
            elif solvent_askmf == "Moles [mol]":
                solvent_mole_mf = float(st.number_input("Enter the moles of the solvent: ", key="twelvei"))
                answer = mole_fraction(solute_mole_mf, solvent_mole_mf)
                st.markdown(f"Answer: {answer}M")
    elif user_inp == "Molality":
        solute_ml = st.text_input("Enter the chemical formula for the solute properly: ", key="fivet")
        solute_askml = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="eights")
        if solute_askml == "Grams [g]":
            solute_mass_ml = float(st.number_input("Enter the grams of the solute: ", key="thirteeni"))
            solvent_ml = st.text_input("Enter the chemical formula for the solvent properly: ", key="sixt")
            solvent_askml = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Kilograms [Kg]", "Moles [mol]"], key="nines")
            molmass_ml = molar_mass(solute_ml)
            moles_solute = solute_mass_ml/molmass_ml
            if solvent_askml == "Kilograms [Kg]":  # == is for the condition
                solvent_massml = st.number_input("Enter the kilograms of the solvent: ", key="fourteeni")  # equal to the number enterede in the input not the input
                molality(moles_solute, solvent_massml)
            elif solvent_askml == "Grams [g]":
                solvent_massml = st.number_input("Enter the grams of the solvent: ", key="fifteeni")
                solvent_massml_kg = solvent_massml/1000
                molality(moles_solute, solvent_massml_kg)
            elif solvent_askml == "Moles [mol]":
                solvent_molml = st.number_input("Enter the moles of the solvent: ", key="sixteeni")
                molarmass = molar_mass(solute_ml)
                solvent_massml_kg = (solvent_molml * molarmass)/1000
                molality(moles_solute, solvent_massml_kg)
        elif solute_askml == "Moles [mol]":
            solute_molml = st.number_input("Enter the moles of the solute: ", key="seventeeni")
            solvent_ml = st.text_input("Enter the chemical formula for the solvent properly: ", key="sixt")
            solvent_askml = st.selectbox("Is the solvent in grams or moles? ", ["Grams [g]", "Kilograms [Kg]", "Moles [mol]"], key="nines")
            if solvent_askml == "Kilograms [Kg]":  # == is for the condition
                solvent_massml = st.number_input("Enter the kilograms of the solvent: ", key="eighteeni")  # equal to the number enterede in the input not the input
                molality(solute_molml, solvent_massml)
            elif solvent_askml == "Grams [g]":
                solvent_massml = st.number_input("Enter the grams of the solvent: ", key="nineteeni")
                solvent_massml_kg = solvent_massml/1000
                molality(solute_molml, solvent_massml_kg)
            elif solvent_askml == "Moles [mol]":
                solvent_molml = st.number_input("Enter the moles of the solvent: ", key="twentyi")
                molarmass = molar_mass(solute_ml)
                solvent_massml_kg = (solvent_molml * molarmass)/1000
                molality(solute_molml, solvent_massml_kg)
            else:
                pass
    elif user_inp == "PPM":
        solute_ppm = st.text_input("Enter the chemical formula for the solute properly: ", key="sevent")
        solute_askppm = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="tens")
        solution_ask =  st.radio("Is the mass of the solution given?", ["Yes", "No"])
        if solution_ask == "No":
            solvent_ppm = st.text_input("Enter the chemical formula for the solvent properly: ", key="eightt")
            solvent_askppm = st.selectbox("Is the solute in grams or moles? ", ["Grams [g]", "Moles [mol]"], key="elevens")
            if solute_askppm == "Grams [g]":
                solute_mass = st.number_input("Enter the grams of the solute: ", key="twentyonei")
                if solvent_askppm == "Grams [g]":
                    solvent_mass = st.number_input("Enter the grams of the solvent:", key="twentytwoi")
                    ppm_solu(solute_mass, solvent_mass)
                elif solvent_askppm =="Moles":
                    solvent_mole = st.number_input("Enter the moles of the solvent", key="twentythreei")
                    molarmass = molar_mass(solvent_ppm)
                    solvent_massml_kg = (solvent_mole * molarmass)/1000
        elif solution_ask == "Yes":
            solvent_askppm = st.selectbox("What is the unit of the solution?", ["Grams [g]", "Kilogram [Kg]", "Moles [mol]", "Liter [L]", "Millileter [mL]"], key="twelves")
            if solvent_askppm == "Grams [g]":
                solution_massppm = st.number_input("Enter the grams of the solution: ")
        
except FormulaError:
    st.markdown("**Enter a valid chemical formula.**")
except ZeroDivisionError:
    st.markdown("**Make sure that the number input is not zero**")

        





