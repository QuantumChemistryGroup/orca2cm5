# orca2cm5
Conversion of the Hirshfeld charges in ORCA to CM5
## How to use
1) Download and unpack the archive orca2cm5-1.0.zip on your Linux computer

a) click on "Source code (zip)" here https://github.com/QuantumChemistryGroup/orca2cm5/releases/tag/v1.0

b) on your Linux machine:
```unzip orca2cm5-1.0.zip```

c) ```cd orca2cm5-1.0```

d) ```chmod u=rwx *```

2) Prepare your ORCA input with the following option included:
```
%output
Print [P_Hirshfeld] 1
end
```
3) Run your ORCA job
4) Run **get_hrs_orca.py** script on your ORCA output with the charges:

```python3 /path/to/orca2cm5-1.0/get_hrs_orca.py your_ORCA_job.out```

5) The result is the file which contains the Cartesian coordinates and the Hirshfeld charges in the last column, see your_ORCA_job.HRS:

```
 C   0.688264   0.911986   4.168096   0.335927
 O   1.382346  -0.084144   4.713222  -0.105731
 O   1.462743   1.841647   3.605061  -0.112823

```

6) Run **hrs_to_m51.py** script on your_ORCA_job.HRS:

```python3 /path/to/orca2cm5-1.0/hrs_to_m51.py your_ORCA_job.HRS```

7) The result is the file which contains the Cartesian coordinates and the CM5 charges in the last column, see your_ORCA_job.M51:

```
 C     0.688264     0.911986     4.168096     0.418118
 O     1.382346    -0.084144     4.713222    -0.179589
 O     1.462743     1.841647     3.605061    -0.183283

```
8) The resulting file your_ORCA_job.M51 can be used to calculate the solvation Gibbs free energy with our SOLV program, see more at https://github.com/QuantumChemistryGroup/solv

> [!IMPORTANT]
> **When using this code (orca2cm5) please cite the following publications:**
> 1) Marenich, A. V.; Jerome, S. V.; Cramer, C. J.; Truhlar, D. G.
Charge Model 5: An Extension of Hirshfeld Population Analysis for the
Accurate Description of Molecular Interactions in Gaseous and
Condensed Phases. J. Chem. Theory Comput. 2012, 8, 527−541.
> 2) Duanmu, K.; Truhlar, D. G. Partial Ionic Character beyond the
Pauling Paradigm: Metal Nanoparticles. J. Phys. Chem. C 2014, 118,
28069−28074.
> 3) Duanmu, K.; Wang, B.; Marenich, A. V.; Cramer, C. J.; Truhlar,
D. G.. CM5PAC Version, 2015.   
> 4) Minenkov, Y. Solv: An Alternative Continuum Model Implementation Based on Fixed Atomic Charges, Scaled
Particle Theory, and the Atom–Atom Potential Method. J. Chem. Theor. Comput. 2023, 19, 5221 – 5230 (DOI: 10.1021/acs.jctc.3c00410)    
