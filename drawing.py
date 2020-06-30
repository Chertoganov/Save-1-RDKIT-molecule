import argparse
import cairosvg
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import DrawingOptions
 
parser = argparse.ArgumentParser( 'smiles to png inmage' )
parser.add_argument( 'smiles' )
parser.add_argument( '--filename', default="mol." )
DrawingOptions.atomLabelFontSize = 55
DrawingOptions.dotsPerAngstrom = 100
DrawingOptions.bondLineWidth = 3.0
 
parser.add_argument( 'smiles' )
 
if __name__=='__main__':
    param = parser.parse_args()
    smiles = param.smiles
    fname = param.filename
    mol = Chem.MolFromSmiles( smiles )
    Draw.MolToFile( mol, fname+"png" )
    Draw.MolToFile( mol, "temp.svg" )
    cairosvg.svg2png( url='./temp.svg', write_to= "svg_"+fname+"png" )
