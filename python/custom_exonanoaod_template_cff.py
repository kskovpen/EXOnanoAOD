import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

## To be filled in once we converge on final EXO nanoAOD content

exonanoTable = cms.EDProducer("EXOnanoAODProducer",
    inputExample = cms.InputTag("input")
)

def add_exonanoTables(process):

    process.exonanoTable = exonanoTable
    process.exonanoTask = cms.Task(process.exonanoTable)
    process.nanoTableTaskCommon.add(process.exonanoTask)

    return process
