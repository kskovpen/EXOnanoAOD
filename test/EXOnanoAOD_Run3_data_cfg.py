import os
import sys
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

from Configuration.Eras.Modifier_run3_nanoAOD_pre142X_cff import run3_nanoAOD_pre142X
process = cms.Process('NANO',run3_nanoAOD_pre142X)

# Input arguments
options = VarParsing('analysis')
options.register('nEvents',
                    1000,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.int,
                    "Number of events to process"
                )
options.register('runOnData',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "If running on data"
                )
options.register('year',
                    "2022ReReco",
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.string,
                    "Year of the dataset"
                )
options.parseArguments()

nevents = options.nEvents
if nevents == 0:
    nevents=-1
    
print('-- Running on '+str(nevents)+' number of events')
if options.runOnData:
    print('-- Running on data')
else:
    print('-- Running on mc')

#if options.runOnData:
#    if options.year == "2022ReReco":
#        process = cms.Process('NANO',Run3)
#    if options.year == "2022Prompt":
#        process = cms.Process('NANO',Run3)
#    if options.year == "2023":
#        process = cms.Process('NANO',Run3_2023)
        
#else:
#    if options.year == "2022PreEE":
#        process = cms.Process('NANO',Run3)
#    if options.year == "2022PostEE":
#        process = cms.Process('NANO',Run3)
#    if options.year == "2023PreBPix":
#        process = cms.Process('NANO',Run3_2023)
#    if options.year == "2023PostBPix":
#        process = cms.Process('NANO',Run3_2023) 
#    if options.year == "2024":
#        process = cms.Process('NANO',Run3_2023)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 100000  # Set reportEvery to control the frequency of report messages
# process.MessageLogger.threshold = cms.untracked.string('ERROR')  # Set the output threshold to ERROR

if not options.runOnData:
    process.load('SimGeneral.MixingModule.mixNoPU_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nevents)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring(),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
)

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

datatier = 'NANOAODSIM'
outputcommands = process.NANOAODSIMEventContent.outputCommands
if options.runOnData:
    outputcommands = process.NANOAODEventContent.outputCommands

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(datatier),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:{0}'.format(options.outputFile)),
    outputCommands = outputcommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
globalTag = ""
if options.runOnData:
    if options.year == "2022ReReco":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_v2', '')
    if options.year == "2022Prompt":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_PromptAnalysis_v1', '')
    if options.year == "2023":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_PromptAnalysis_v1', '')
else:
    if options.year == "2022PreEE":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_v5', '')
    if options.year == "2022PostEE":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_postEE_v6', '')
    if options.year == "2023PreBPix":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_v14', '')
    if options.year == "2023PostBPix":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_postBPix_v2', '')
    if options.year == "2024":
        globalTag = GlobalTag(process.GlobalTag, '133X_mcRun3_2024_realistic_v8', '')
process.GlobalTag = globalTag
    
# Path and EndPath definitions
if options.runOnData:
    process.nanoAOD_step = cms.Path(process.nanoSequence)
else:
    process.nanoAOD_step = cms.Path(process.nanoSequenceMC)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Displaced Jet table                                                                                                                         
process.dispJetTable = cms.EDProducer("DispJetTableProducer",
    rho=cms.InputTag("fixedGridRhoFastjetAll"),
    electrons=cms.InputTag("linkedObjects","electrons"),
    muons=cms.InputTag("linkedObjects","muons"),
    jets=cms.InputTag("linkedObjects","jets"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    secondaryVertex = cms.InputTag("displacedInclusiveSecondaryVertices")
)

process.load('PhysicsTools.EXOnanoAOD.displacedInclusiveVertexing_cff')
process.nanoAOD_step += process.displacedInclusiveVertexing
process.nanoAOD_step += process.dispJetTable

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 
#call to customisation function nanoAOD_customizeData imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
