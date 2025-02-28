import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi import *
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *

electronVertexTable = cms.EDProducer("ElectronVertexTableProducer",
    electrons=cms.InputTag("linkedObjects","electrons"),
    beamspot=cms.InputTag("offlineBeamSpot"),
    generalTracks=cms.InputTag("generalTracks"),
    primaryVertex=cms.InputTag("offlineSlimmedPrimaryVertices")
)

def add_electronVertexTables(process):

    process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
    process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')

    process.electronVertexTable = electronVertexTable
    process.electronVertexTask = cms.Task(process.electronVertexTable)
    process.nanoTableTaskCommon.add(process.electronVertexTask)

    return process
