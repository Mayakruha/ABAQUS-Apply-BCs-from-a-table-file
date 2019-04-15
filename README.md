# ABAQUS-Apply-BCs-from-a-table-file
The scripts apply pressure / thermal boundary conditions in ABAQUS CAE on basis of a table file
ApplyPress.py applies pressure
ApplyThBc.py applies thermal boundary conditions

--Scope--
If there is a number of models with same boundary conditions the scripts can be used to decrease time for building models. It's necessary to made a table file with boundary conditions data and after that you has to create sets with corresponding names for all models.

--Table file--
*The table file is a comma delimited CSV file. Examples: Presstable.csv and ThBCtable.csv

PRESSURE TABLE FILE:
First column - name of faces (sets for faces)
Second column - pressure
Third column - Name of amplitude function ("" - if pressure is constant)
Following columns - names of parts (a column for every part)

THERMAL BCs TABLE FILE:
First column - name of faces (sets for faces)
Second column - Bulk temperature
Third column - Heat transfer coefficient
Fourth column - Name of amplitude function for bulk temperature ("" - if bulk temperature is constant)
Fifth column - Name of amplitude function for heat transfer coefficient ("" - if heat transfer coefficient is constant)
Following columns - names of parts (a column for every part)

--Steps--
- Edit the scripts before running them. Set a name of a table file in FILENAME. Set a name of the step in STEPNAME if boundary conditions should be applied after the first step (if boundary conditions are applied in the first step STEPNAME="").
- Open a model in Abaqus CAE
- Run the script
