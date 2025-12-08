import os
import re

# List of files to scan
files_to_scan = [
    '00_01_thesis.tex',
    '00_03_abstract.tex',
    '01_introduction.tex',
    '02_Related_works.tex',
    '03_Proposed_framework.tex',
    '04_RESULT.tex',
    '05_conclusion.tex'
]

# Current abbreviations from the file
current_abbrs = {
    '3GPP': '3rd Generation Partnership Project',
    'AMF': 'Access and Mobility Management Function',
    'DDQN': 'Double Deep Q-Network',
    'DNN': 'Deep Neural Network',
    'DRL': 'Deep Reinforcement Learning',
    'DQN': 'Deep Q-Network',
    'ECEF': 'Earth-Centered, Earth-Fixed',
    'EIRP': 'Effective Isotropic Radiated Power',
    'FCC': 'Federal Communications Commission',
    'FLSO': 'Feeder Link Switchover',
    'FSPL': 'Free Space Path Loss',
    'GEO': 'Geostationary Earth Orbit',
    'GPU': 'Graphics Processing Unit',
    'GW': 'Gateway',
    'gNB': 'Next Generation NodeB',
    'HO': 'Handover',
    'IIR': 'Infinite Impulse Response',
    'ISL': 'Inter-Satellite Link',
    'KPI': 'Key Performance Indicator',
    'L3': 'Layer 3',
    'LEO': 'Low Earth Orbit',
    'LoS': 'Line-of-Sight',
    'MDP': 'Markov Decision Process',
    'mMTC': 'massive Machine Type Communications',
    'MTS': 'Minimum Time-of-Stay',
    'NG': 'Next Generation interface',
    'NLoS': 'Non-Line-of-Sight',
    'NP': 'Non-deterministic Polynomial time',
    'NR': 'New Radio',
    'NTN': 'Non-Terrestrial Networks',
    'PER': 'Prioritized Experience Replay',
    'QoS': 'Quality of Service',
    'RB': 'Resource Block',
    'RL': 'Reinforcement Learning',
    'RRM': 'Radio Resource Management',
    'RRC': 'Radio Resource Control',
    'RSRP': 'Reference Signal Received Power',
    'SDN': 'Software-Defined Networking',
    'TAC': 'Tracking Area Code',
    'TD': 'Temporal-Difference',
    'TLE': 'Two-Line Element set',
    'ToS': 'Time-of-Stay',
    'UE': 'User Equipment',
    'UFLSO': 'Unnecessary Feeder Link Switchover'
}

# Set of found abbreviations
found_abbrs = set()
# Potential new abbreviations (words with 2+ uppercase letters)
potential_new = {}

base_path = r'c:\Users\winner\Dropbox\winner\개인폴더\김민식\15.졸업준비\Master_thesis_kms_main'

for filename in files_to_scan:
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Check for existing abbreviations
        for abbr in current_abbrs:
            # Simple check: is the abbreviation in the text?
            # We use word boundaries to avoid partial matches (e.g. 'GW' in 'GWh')
            # But '3GPP' starts with digit, \b might be tricky.
            if abbr == '3GPP':
                if '3GPP' in content:
                    found_abbrs.add(abbr)
            elif abbr == 'gNB':
                if 'gNB' in content:
                    found_abbrs.add(abbr)
            elif abbr == 'mMTC':
                if 'mMTC' in content:
                    found_abbrs.add(abbr)
            else:
                if re.search(r'\b' + re.escape(abbr) + r'\b', content):
                    found_abbrs.add(abbr)
        
        # Find potential new ones
        # Look for words with at least 2 uppercase letters, possibly numbers
        matches = re.findall(r'\b[A-Z][A-Z0-9]+\b', content)
        for m in matches:
            if m not in current_abbrs and len(m) >= 2:
                potential_new[m] = potential_new.get(m, 0) + 1

# Identify unused
unused = set(current_abbrs.keys()) - found_abbrs

print("Unused Abbreviations (to remove):")
for abbr in sorted(unused):
    print(abbr)

print("\nPotential New Abbreviations (frequency > 1):")
for abbr, count in sorted(potential_new.items(), key=lambda x: x[1], reverse=True):
    if count > 1:
        print(f"{abbr}: {count}")
