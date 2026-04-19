import os
import sys
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

# Input arguments
options = VarParsing('analysis')
options.register('year',
                    "2022",
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.string,
                    "Year of the dataset"
                )
options.parseArguments()

if options.year == "2022":
    process = cms.Process('NANO',Run3)
elif options.year == "2022EE":
    process = cms.Process('NANO',Run3)
elif options.year == "2023":
    process = cms.Process('NANO',Run3_2023)
elif options.year == "2023BPix":
    process = cms.Process('NANO',Run3_2023) 
elif options.year == "2024":
    process = cms.Process('NANO',Run3_2024)

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

process.load('SimGeneral.MixingModule.mixNoPU_cfi')

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
if options.year == "2022":
    globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_v5', '')
elif options.year == "2022EE":
    globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_postEE_v6', '')
elif options.year == "2023":
    globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_v14', '')
elif options.year == "2023BPix":
    globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_postBPix_v2', '')
elif options.year == "2024":
    globalTag = GlobalTag(process.GlobalTag, '150X_mcRun3_2024_realistic_v2', '')
process.GlobalTag = globalTag

process.load('PhysicsTools.EXOnanoAOD.displacedInclusiveVertexing_cff')
process.dispJetTable = cms.EDProducer("DispJetTableProducer",
    rho=cms.InputTag("fixedGridRhoFastjetAll"),
    electrons=cms.InputTag("linkedObjects","electrons"),
    muons=cms.InputTag("linkedObjects","muons"),
    jets=cms.InputTag("linkedObjects","jets"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    secondaryVertex = cms.InputTag("displacedInclusiveSecondaryVertices")
)
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
    
process.nanoAOD_step += process.displacedInclusiveVertexing
process.nanoAOD_step += process.dispJetTable

process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded

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
