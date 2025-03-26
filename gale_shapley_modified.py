"""
                ----- PSEUDOCODE FOR MODIFIED GALE-SHAPLEY ALGORITHM -----

GENERATE unmatched_hospital_list with hospital names.
INITIALIZE hospital_match to have hospital names with empty lists.
INITIALIZE resident_match to have resident names with None values.
INITIALIZE hospital_proposals to have hospital names with values set to 0.
GENERATE resident_preferences with resident names and a dictionary of hospital preferences with ranks as values.
    
WHILE unmatched_hospital_list is not empty:

	SET hospital to the first element of unmatched_hospital_list.
	GET preference list and slot of the hospital.
	GET current index of hospital from hospital_proposals, SET as resident_index.
	
	IF hospital slots are fulfilled: 
		REMOVE hospital from unmatched_hospital_list and continue.
	IF the index has reached the end of preference list:
		REMOVE hospital from unmatched_hospital_list and continue.
    	
	GET resident from the preference_list based on resident index, SET as resident 
	INCREMENT the hospital's index in hospital_proposals.
    
	IF resident is not matched:
    		ADD resident to the hospital in hospital_match.
    		IF hospital slots are full, 
    			REMOVE hospital from unmatched_hospital_list.

    ELSE IF resident is matched:
    		Compare the existing match of resident with the new hospital.
    		IF resident prefers new hospital over the old hospital:
    			UPDATE the hospital_match by removing resident from its old hospital
				ADD resident to the new hospital in hospital_match.
			
			GET slots size of old hospital
			IF old hospital slots are not fulfilled:
    			ADD old hospital to unmatched_hospital_list.
    		
			IF new hospital slots are full:
				REMOVE new hospital from unmatched_hospital_list.

RETURN hospital_match

                --------------------------------------------------------
"""

import csv
from datetime import datetime


def process_input_from_csv(file_path):

    hospitals = []
    residents = []

    #to read .csv or .txt file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        read_hospitals = True
        for row in reader:
            #condition to check a line break
            if not row or all(cell.strip() == '' for cell in row):
                read_hospitals = False
                continue
            
            if read_hospitals:
                #extract first two items for hospitals and slots
                hospital = row[0].strip()
                slot = row[1].strip()
            
                #convert the remaining items to lists which are residents
                pref_list = [r.strip() for r in row[2:] if r.strip()]
            
                #structure as dictionary
                hospital_dict = {
                    "Hospitals": hospital,
                    "Slots": slot,
                    "Preference_list": pref_list
                }
                hospitals.append(hospital_dict)
                
            else:
                #extract the first item for residents
                resident = row[0].strip()
        
                #convert the remaining items to lists which are residents
                item_list = [r.strip() for r in row[1:] if r.strip()]
            
                residents_dict = {
                    "Residents": resident,
                    "Res_Preference_list": item_list
                }
                residents.append(residents_dict)
                          
    return hospitals, residents

def gale_shapley_algo(hospital_dict, residents_dict):

    unmatched_hospital_list = [dct['Hospitals'] for dct in hospital_dict]
    hospital_match = {dct['Hospitals']: [] for dct in hospital_dict}
    resident_match = {dct['Residents']: None for dct in residents_dict}
    hospital_proposals = {dct['Hospitals']: 0 for dct in hospital_dict}

    #resident's preference list of hospitals with rank generated (for easy lookups during conflict)
    resident_preferences = {
        dct['Residents']: {hospital: rank for rank, hospital in enumerate(dct['Res_Preference_list'])}
        for dct in residents_dict
    }
    import pdb; pdb.set_trace()
    #loop over unmatched hospital list
    while unmatched_hospital_list:

        hospital = unmatched_hospital_list[0]
        pref_list, slot = next(((dct['Preference_list'], dct['Slots']) for dct in hospital_dict if dct['Hospitals'] == hospital), None)
        resident_index = hospital_proposals[hospital]
        
        #slot fulfillment condition (if true, remove hospital from unmatched list)
        if len(hospital_match[hospital]) >= int(slot):
            unmatched_hospital_list.pop(0)
            continue

        #check end of preference list (if true, remove hospital from unmatched list)
        if resident_index >= len(pref_list):
            unmatched_hospital_list.pop(0)
            continue
        
        resident = pref_list[resident_index]
        hospital_proposals[hospital] += 1

        #check if resident is unmatched
        if resident_match[resident] is None:
            #add hospital-resident to resultant dict
            hospital_match[hospital].append(resident)
            resident_match[resident] = hospital
        
            if len(hospital_match[hospital]) >= int(slot):
                unmatched_hospital_list.pop(0)
        
        # check if matched residents have higher preferences for current hospital
        # if yes, 1. remove resident from old hospital and add to new 2. Add old hospital back to unmatched list 3. check new hospital slot size
        else:
            #set hospital of previously matched resident
            old_hospital = resident_match[resident]
            res_current_pref = resident_preferences.get(resident).get(hospital)
            res_old_pref = resident_preferences.get(resident).get(old_hospital)
            
            #add condition to check if hospital exist in resident's preferences list
            if res_current_pref and res_current_pref < res_old_pref:
                #remove the resident from current hospital
                hospital_match[old_hospital].remove(resident)
                #add hospital-resident to resultant dict
                hospital_match[hospital].append(resident)
                resident_match[resident] = hospital

                #get slot size of old hospital
                old_hospital_slot = next((dct['Slots'] for dct in hospital_dict if dct['Hospitals'] == old_hospital), None)

                #add old hospital back to unmatched list
                if len(hospital_match[old_hospital]) < int(old_hospital_slot):
                    unmatched_hospital_list.append(old_hospital)

                if len(hospital_match[hospital]) >= int(slot):
                    unmatched_hospital_list.pop(0)

    return hospital_match


if __name__ == '__main__':

    #add your file path to read input or set file_num for existing
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    path = f"input_data/hospital_resident_preferences_9.csv"

    hospital_dict, residents_dict = process_input_from_csv(path)
    match_result = gale_shapley_algo(hospital_dict, residents_dict)
    # print(match_result)

    #convert matched result to desired format and write to file
    with open(f"output_data/match_result_{timestamp}.txt", "w") as r:
        for hospital, residents in match_result.items():
            r.write(",".join([hospital, ", ".join(residents)]) + "\n")



