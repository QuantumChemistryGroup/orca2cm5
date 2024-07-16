#!/usr/bin/python
import sys, string, os, glob
import subprocess
from math import *

elements = {
       'H':'1',
       'He':'2',
       'Li':'3',
       'Be':'4',
       'B':'5',
       'C':'6',
       'N':'7',
       'O':'8',
       'F':'9',
       'Ne':'10',
       'Na':'11',
       'Mg':'12',
       'Al':'13',
       'Si':'14',
       'P':'15',
       'S':'16',
       'Cl':'17',
       'Ar':'18',
       'K':'19',
       'Ca':'20',
       'Sc':'21',
       'Ti':'22',
       'V':'23',
       'Cr':'24',
       'Mn':'25',
       'Fe':'26',
       'Co':'27',
       'Ni':'28',
       'Cu':'29',
       'Zn':'30',
       'Ga':'31',
       'Ge':'32',
       'As':'33',
       'Se':'34',
       'Br':'35',
       'Kr':'36',
       'Rb':'37',
       'Sr':'38',
       'Y':'39',
       'Zr':'40',
       'Nb':'41',
       'Mo':'42',
       'Tc':'43',
       'Ru':'44',
       'Rh':'45',
       'Pd':'46',
       'Ag':'47',
       'Cd':'48',
       'In':'49',
       'Sn':'50',
       'Sb':'51',
       'Te':'52',
       'I':'53',
       'Xe':'54',
       'Cs':'55',
       'Ba':'56',
       'La':'57',
       'Ce':'58',
       'Pr':'59',
       'Nd':'60',
       'Pm':'61',
       'Sm':'62',
       'Eu':'63',
       'Gd':'64',
       'Tb':'65',
       'Dy':'66',
       'Ho':'67',
       'Er':'68',
       'Tm':'69',
       'Yb':'70',
       'Lu':'71',
       'Hf':'72',
       'Ta':'73',
       'W':'74',
       'Re':'75',
       'Os':'76',
       'Ir':'77',
       'Pt':'78',
       'Au':'79',
       'Hg':'80',
       'Tl':'81',
       'Pb':'82',
       'Bi':'83',
       'Po':'84',
       'At':'85',
       'Rn':'86',
       'Fr':'87',
       'Ra':'88',
       'Ac':'89',
       'Th':'90',
       'Pa':'91',
       'U':'92',
       'Np':'93',
       'Pu':'94',
       'Am':'95',
       'Cm':'96',
       'Bk':'97',
       'Cf':'98',
       'Es':'99',
       'Fm':'100',
       'Md':'101',
       'No':'102',
       'Lr':'103',
       'Rf':'104',
       'Db':'105',
       'Sg':'106',
       'Bh':'107',
       'Hs':'108',
       'Mt':'109',
       'Ds':'110',
       'Rg':'111',
       'Cn':'112',
       'Uut':'113',
       'Fl':'114',
       'Uup':'115',
       'Lv':'116',
       'Uuh':'117',
       'Uuh':'118',
}


# Main program starts here

coord = []
charges = []

f = open(sys.argv[1], 'r')

for line in f:  # for each line in a file
	d = str.split(line)
	if len(d) == 5:
		a = [d[0],d[1],d[2],d[3]]
		coord.append(a)
		charges.append(d[4])
		
f.close()

# write temporary file in G03 style

f = open(sys.argv[1][0:-3]+'g03','w')
f.write (
'''
                         Standard orientation:
 ---------------------------------------------------------------------
 Center     Atomic      Atomic             Coordinates (Angstroms)
 Number     Number       Type             X           Y           Z
 ---------------------------------------------------------------------
'''
)
i=1;

for j in coord:
	f.write('%7i %10s %11s %15s %11s %11s\n' % (i, elements[j[0]], 0, j[1], j[2], j[3] ))
	i = i + 1
f.write (''' ---------------------------------------------------------------------



 Hirshfeld spin densities, charges and dipoles using
               1          2         3          4          5
'''
)
chrg = 0
for i in range(len(charges)):
	f.write('%6i %2s %11.6f %10.6f %9.6f %10.6f %10.6f\n' % (i+1, coord[i][0], 0, float(charges[i]), 0, 0, 0 ))
	chrg = chrg + float(charges[i])
f.write('%26s %2.6f\n' % ('Sum of Hirshfeld charges=', chrg))
f.write('\n')
f.close()

# the script should be in the folder that contains the CM5 code
a = os.path.abspath(__file__)
d = str.split(a,'/')
path=''
for i in range(len(d)):
	if i>0 and i<len(d)-1:
		path = path + '/' + d[i]
#print path
j = sys.argv[1][0:-3]+'g03'
a = "\s"[0:-1]+"n"
subprocess.call('/bin/bash -c "$a1"' , shell=True, env = {'a1': "export PATH="+path+":$PATH; "+"cm5pac <<< $'"+j+a+" 1'"})
# CM5 charges are done

coord = []

f = open(j,'r')
s = f.readline()
i = 0
for line in f:  # for each line in a file
	if 'Coordinates (Angstroms)' in line: i = i + 1   
print (i)

f.seek(0)
s = f.readline()

for j in range(i):
	while str.find(s, 'Coordinates (Angstroms)') == -1 and s != "": s = f.readline()
	s = f.readline()

s = f.readline()
s = f.readline()
#print s

while str.find(s, "--------") == -1:
	d = str.split(s); 
	if len(d) == 6:
		g = (d[3], d[4], d[5])
		coord.append(g); s = f.readline()
	else: print ("All the coordinates read"); s = f.readline()


# get Mulliken charges
ch_hirsh = []
f.seek(0)
while str.find(s, 'Hirshfeld spin densities') == -1 and s != "": s = f.readline()
s = f.readline()

while str.find(s, 'Sum of Hirshfeld charges') == -1 and s != "": 
	s = f.readline()
	d = str.split(s)
	ch_hirsh.append([d[1]])
ch_hirsh = ch_hirsh[0:-1]

while str.find(s, 'Charges (in A.U.) from CM5PAC version 2015') == -1 and s != "": s = f.readline()
s = f.readline()
s = f.readline()
s = f.readline()
s = f.readline()
s = f.readline()
i = 0
while str.find(s, '----------') == -1 and s != "": 
	d = str.split(s)
	ch_hirsh[i].append(d[2])
	s = f.readline()
	i = i + 1

f.close()
f1 = open(sys.argv[1][0:-4]+'.M51', 'w')

if len(coord) == len(ch_hirsh):
	for i in range(len(coord)):
		f1.write('%2s %12s %12s %12s %12s\n' % (ch_hirsh[i][0], coord[i][0], coord[i][1], coord[i][2], ch_hirsh[i][1]))
else:
	print ('Dimesnisions of chrg and coord are not equal. exit', len(coord), len(ch_hirsh), 0)
	sys.exit(0)
f1.close()

os.remove(sys.argv[1][0:-3]+'g03')


