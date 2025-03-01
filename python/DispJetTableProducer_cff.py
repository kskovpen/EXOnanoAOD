import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

outputTable = cms.EDProducer("DispJetTableProducer",
    rho=cms.InputTag("fixedGridRhoFastjetAll"),
    electrons=cms.InputTag("linkedObjects","electrons"),
    muons=cms.InputTag("linkedObjects","muons"),
    jets=cms.InputTag("linkedObjects","jets"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    secondaryVertex = cms.InputTag("displacedInclusiveSecondaryVertices")
)

def add_customTables_template(process):

    process.outputTable = outputTable
    process.exonanoaodTask = cms.Task(process.outputTable)
    process.nanoTableTaskCommon.add(process.exonanoaodTask)

    return process
