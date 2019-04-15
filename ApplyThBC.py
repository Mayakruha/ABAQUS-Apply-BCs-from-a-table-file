FileName='ThBCtable.csv'
StepName=''
#---------------
from step import *
from interaction import *
ModelName=session.sessionState['Viewport: 1']['modelName']
n=len(mdb.models[ModelName].steps)
NameList=mdb.models[ModelName].steps.keys()
Count=0
i=0
if StepName=='': Flag=True
else: Flag=False
while Flag and i<n:
	if mdb.models[ModelName].steps[NameList[i]].procedureType==COUPLED_TEMP_DISPLACEMENT:
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
	if TextValue[5]=='':
	  	for InstanceName in mdb.models[ModelName].rootAssembly.allInstances.keys():
	  		for SurfaceName in mdb.models[ModelName].rootAssembly.allInstances[InstanceName].surfaces.keys():
	  			if SurfaceName==TextValue[0]:
	  				Count=Count+1
	  				BCname='T'+TextValue[1]+'_HTC'+TextValue[2]+'_'+InstanceName+'_'+SurfaceName
					mdb.models[ModelName].FilmCondition(createStepName=StepName, definition=EMBEDDED_COEFF, \
    						filmCoeff=float(TextValue[2]), filmCoeffAmplitude=TextValue[4], name=BCname, \
    						sinkAmplitude=TextValue[3], sinkDistributionType=UNIFORM, sinkFieldName='', sinkTemperature=float(TextValue[1]), \
    						surface=mdb.models[ModelName].rootAssembly.instances[InstanceName].surfaces[SurfaceName]) 
	else:
		i=5
		while TextValue[i]!='':
			InstanceName=TextValue[i]
	  		for SurfaceName in mdb.models[ModelName].rootAssembly.allInstances[InstanceName].surfaces.keys():
	  			if SurfaceName==TextValue[0]:
	  				Count=Count+1
					BCname='T'+TextValue[1]+'_HTC'+TextValue[2]+'_'+InstanceName+'_'+SurfaceName
					mdb.models[ModelName].FilmCondition(createStepName=StepName, definition=EMBEDDED_COEFF, \
    						filmCoeff=float(TextValue[2]), filmCoeffAmplitude=TextValue[4], name=BCname, \
    						sinkAmplitude=TextValue[3], sinkDistributionType=UNIFORM, sinkFieldName='', sinkTemperature=float(TextValue[1]), \
    						surface=mdb.models[ModelName].rootAssembly.instances[InstanceName].surfaces[SurfaceName]) 
			i=i+1
			if i==n:
				break
f.close()
print str(Count)+' thermal BCs have been created at '+StepName
