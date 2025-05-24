from rdkit import Chem 
import os 
import pickle 

def read_xyz_to_mol(fn):
    sdf_fn = f"{fn[:-4]}.sdf"
    os.system(f"obabel {fn} -O {fn[:-4]}.sdf")
    mol = Chem.SDMolSupplier(sdf_fn)[0] 
    return mol

mol_list = []
gap_list = []
for i in range(1, 1001):
    fn = f"./data/dsgdb9nsd_{str(i).zfill(6)}.xyz"
    f = open(fn, "r")
    line = f.readlines()[1].strip().split()[9]
    line = str(line)          
    mol = read_xyz_to_mol(fn)
    if mol is None:
        continue
    mol.SetProp("gap", line)
    mol_list.append(mol)
    gap_list.append(float(line))
    #print(mol.GetProp("gap"))
    
pickle.dump(mol_list, open("./mol.pkl", "wb"))
pickle.dump(gap_list, open("./gap.pkl", "wb"))
