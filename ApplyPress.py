FileName='Presstable.csv'
StepName='MI-Start_Up'
#---------------
from step import *
from load import *
ModelName=session.sessionState['Viewport: 1']['modelName']
n=len(mdb.models[ModelName].steps)
NameList=mdb.models[ModelName].steps.keys()
Count=0
i=0
if StepName=='': Flag=True
else: Flag=False
while Flag and i<n:
	if mdb.models[ModelName].steps[NameList[i]].procedureType==STATIC_GENERAL:
		Flag=False
		StepName=NameList[i]
	i=i+1
f=open(FileName)
line=f.readline()
while True:
	line=f.readline().strip()
	if not line:
		break
	TextValue=line.split(';')
	n=len(TextValue)
	PressValue=(float(TextValue[1])-1)*100000
	if len(TextValue[1])>2:TextValue[1]=TextValue[1].replace('.','_').ljust(5,'0')
	else: TextValue[1]=TextValue[1]+'_00'
	if TextValue[3]=='':
	  	for InstanceName in mdb.models[ModelName].rootAssembly.allInstances.keys():
	  		for SurfaceName in mdb.models[ModelName].rootAssembly.allInstances[InstanceName].surfaces.keys():
	  			if SurfaceName==TextValue[0]:
	  				Count=Count+1
	  				BCname='Pr'+TextValue[1]+'_'+InstanceName+'_'+SurfaceName
					mdb.models[ModelName].Pressure(amplitude=TextValue[2], createStepName=StepName, \
    						distributionType=UNIFORM, field='', magnitude=PressValue, name=BCname, \
    						region=mdb.models[ModelName].rootAssembly.instances[InstanceName].surfaces[SurfaceName]) 
	else:
		i=3
		while TextValue[i]!='':
			InstanceName=TextValue[i]
	  		for SurfaceName in mdb.models[ModelName].rootAssembly.allInstances[InstanceName].surfaces.keys():
	  			if SurfaceName==TextValue[0]:
	  				Count=Count+1
					BCname='Pr'+TextValue[1]+'_'+InstanceName+'_'+SurfaceName
					mdb.models[ModelName].Pressure(amplitude=TextValue[2], createStepName=StepName, \
    						distributionType=UNIFORM, field='', magnitude=PressValue, name=BCname, \
    						region=mdb.models[ModelName].rootAssembly.instances[InstanceName].surfaces[SurfaceName])
			i=i+1
			if i==n:
				break
f.close()
print str(Count)+' pressure loads have been created at '+StepName
print 'ambient pressure has been diducted'
