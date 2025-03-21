// -*- C++ -*-
//
// Package:    PhysicsTools/EXOnanoAOD
// Class:      DispJetTableProducer
//
/**\class DispJetTableProducer

 Description: Additional variables for displaced vertices involving at least one lepton and other tracks

*/
//
// Original Author:  Kirill Skovpen
//         Created:  Sat, 1 Mar 2025 08:37:01 GMT
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

// nanoAOD include files
#include "DataFormats/NanoAOD/interface/FlatTable.h"

// object specific include files
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

class DispJetTableProducer : public edm::stream::EDProducer<> {
protected:

  float dEtaInSeed(const pat::Electron* el) const;
  float getPFIso(const pat::Muon& muon) const;
  float getPFIso(const pat::Electron& electron) const;
  int findMatchedJet(const reco::Candidate& lepton, const edm::Handle< std::vector< pat::Jet > >& jets);
  void fillLeptonJetVariables(const reco::GsfElectron *el, const reco::Muon *mu, edm::Handle< std::vector< pat::Jet > >& jets, const reco::Vertex& vertex, const double rho);

  edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> ttbToken_;
  edm::EDGetTokenT<double> rhoTag_;
  edm::EDGetTokenT<std::vector<pat::Electron> > electronTag_;
  edm::EDGetTokenT<std::vector<pat::Muon> > muonTag_;
  edm::EDGetTokenT<std::vector<pat::Jet> > jetTag_;
  edm::EDGetTokenT<std::vector<pat::Jet> > jetFatTag_;
  edm::EDGetTokenT<std::vector<pat::Jet> > jetSubTag_;
  edm::EDGetTokenT<reco::VertexCollection> vtxTag_;
  edm::EDGetTokenT<reco::VertexCollection> secVtxTag_;

  const TransientTrackBuilder* theB;
  
  std::vector<int> el_idx;
  std::vector<bool> el_lIVF_match;
  std::vector<bool> el_isEB, el_isEE;
  std::vector<float> el_superClusterOverP, el_ecalEnergy, el_dEtaInSeed;
  std::vector<int> el_numberInnerHitsMissing, el_numberOfValidPixelHits, el_numberOfValidTrackerHits;
  std::vector<int> el_IVF_df, el_IVF_ntracks, el_IVF_elid;
  std::vector<float> el_IVF_x, el_IVF_y, el_IVF_z, el_IVF_cx, el_IVF_cy, el_IVF_cz, el_IVF_chi2, el_IVF_pt, el_IVF_eta, el_IVF_phi, el_IVF_E, el_IVF_mass;
  std::vector<int> el_IVF_trackcharge, el_IVF_trackelid, el_IVF_trackvtxid;
  std::vector<float> el_IVF_trackpt, el_IVF_tracketa, el_IVF_trackphi, el_IVF_trackE, el_IVF_trackdxy, el_IVF_trackdz;
  std::vector<float> el_IVF_tracksignedIP2D, el_IVF_tracksignedIP3D, el_IVF_tracksignedIP2Dsig, el_IVF_tracksignedIP3Dsig;
  
  std::vector<float> el_jetPtRatio, el_jetPtRel;
  std::vector<int> el_jetIdx, el_jetSelectedChargedMultiplicity;
  std::vector<int> el_jetFatIdx, el_jetSubIdx;
  std::vector<float> el_relIso0p4;
  std::vector<float> el_sigmaIetaIeta, el_deltaPhiSuperClusterTrack, el_deltaEtaSuperClusterTrack, el_eInvMinusPInv, el_hOverE;
  
  std::vector<float> el_dxy, el_dz, el_3dIP, el_3dIPSig;
  std::vector<float> el_IVF_signedIP2D, el_IVF_signedIP3D, el_IVF_signedIP2Dsig, el_IVF_signedIP3Dsig;
   
  std::vector<int> mu_idx;
  std::vector<bool> mu_lIVF_match;
  std::vector<float> mu_innerTrackValidFraction, mu_globalTrackNormalizedChi2, mu_CQChi2Position, mu_CQTrackKink;
  std::vector<int> mu_numberOfMatchedStation, mu_numberOfValidPixelHits, mu_numberOfValidTrackerHits, mu_numberInnerHitsMissing, mu_trackerLayersWithMeasurement, mu_numberInnerHits;
  std::vector<int> mu_IVF_df, mu_IVF_ntracks, mu_IVF_muid;
  std::vector<float> mu_IVF_x, mu_IVF_y, mu_IVF_z, mu_IVF_cx, mu_IVF_cy, mu_IVF_cz, mu_IVF_chi2, mu_IVF_pt, mu_IVF_eta, mu_IVF_phi, mu_IVF_E, mu_IVF_mass;
  std::vector<int> mu_IVF_trackcharge, mu_IVF_trackmuid, mu_IVF_trackvtxid;
  std::vector<float> mu_IVF_trackpt, mu_IVF_tracketa, mu_IVF_trackphi, mu_IVF_trackE, mu_IVF_trackdxy, mu_IVF_trackdz;
  std::vector<float> mu_IVF_tracksignedIP2D, mu_IVF_tracksignedIP3D, mu_IVF_tracksignedIP2Dsig, mu_IVF_tracksignedIP3Dsig;
  
  std::vector<float> mu_jetPtRatio, mu_jetPtRel;
  std::vector<int> mu_jetIdx, mu_jetSelectedChargedMultiplicity;
  std::vector<int> mu_jetFatIdx, mu_jetSubIdx;
  std::vector<float> mu_relIso0p4;
  std::vector<float> mu_trackPt, mu_trackPtErr;
  
  std::vector<float> mu_dxy, mu_dz, mu_3dIP, mu_3dIPSig;
  std::vector<float> mu_IVF_signedIP2D, mu_IVF_signedIP3D, mu_IVF_signedIP2Dsig, mu_IVF_signedIP3Dsig;

public:
  DispJetTableProducer(edm::ParameterSet const& params)
    :
    ttbToken_(esConsumes(edm::ESInputTag("", "TransientTrackBuilder"))),
    rhoTag_(consumes<double>(params.getParameter<edm::InputTag>("rho"))),
    electronTag_(consumes<std::vector<pat::Electron>>(params.getParameter<edm::InputTag>("electrons"))),
    muonTag_(consumes<std::vector<pat::Muon>>(params.getParameter<edm::InputTag>("muons"))),
    jetTag_(consumes<std::vector<pat::Jet>>(params.getParameter<edm::InputTag>("jets"))),
    jetFatTag_(consumes<std::vector<pat::Jet>>(params.getParameter<edm::InputTag>("jetsFat"))),
    jetSubTag_(consumes<std::vector<pat::Jet>>(params.getParameter<edm::InputTag>("jetsSub"))),
    vtxTag_(consumes<reco::VertexCollection>(params.getParameter<edm::InputTag>("primaryVertex"))),
    secVtxTag_(consumes<reco::VertexCollection>(params.getParameter<edm::InputTag>("secondaryVertex"))) {
       produces<nanoaod::FlatTable>("DispJetElectron");
       produces<nanoaod::FlatTable>("DispJetElectronVtx");
       produces<nanoaod::FlatTable>("DispJetElectronTrk");
       produces<nanoaod::FlatTable>("DispJetMuon");
       produces<nanoaod::FlatTable>("DispJetMuonVtx");
       produces<nanoaod::FlatTable>("DispJetMuonTrk");
  }   

  ~DispJetTableProducer() override {}
  
  void produce(edm::Event& iEvent, const edm::EventSetup& iSetup) override {

    theB = &iSetup.getData(ttbToken_);
    
    edm::Handle<double> rhoHandle;
    iEvent.getByToken(rhoTag_, rhoHandle);
    
    edm::Handle<std::vector<pat::Electron> > electronHandle;
    iEvent.getByToken(electronTag_, electronHandle);
    
    edm::Handle<std::vector<pat::Muon> > muonHandle;
    iEvent.getByToken(muonTag_, muonHandle);
    
    edm::Handle<std::vector<pat::Jet> > jetHandle;
    iEvent.getByToken(jetTag_, jetHandle);

    edm::Handle<std::vector<pat::Jet> > jetFatHandle;
    iEvent.getByToken(jetFatTag_, jetFatHandle);

    edm::Handle<std::vector<pat::Jet> > jetSubHandle;
    iEvent.getByToken(jetSubTag_, jetSubHandle);
    
    edm::Handle<reco::VertexCollection> primaryVertexHandle;
    iEvent.getByToken(vtxTag_, primaryVertexHandle);
    
    edm::Handle<reco::VertexCollection> secondaryVertexHandle;
    iEvent.getByToken(secVtxTag_, secondaryVertexHandle);
    
    const auto& pv = primaryVertexHandle->at(0);
    GlobalPoint primaryVertex(pv.x(), pv.y(), pv.z());
    
    const reco::VertexCollection & secVertices = (*secondaryVertexHandle);
    
    unsigned int nElectrons = electronHandle->size();
    unsigned int nMuons = muonHandle->size();
    
    el_idx.clear();
    el_lIVF_match.clear();
    el_isEB.clear(); el_isEE.clear();
    el_superClusterOverP.clear(); el_ecalEnergy.clear(); el_dEtaInSeed.clear();
    el_numberInnerHitsMissing.clear(); el_numberOfValidPixelHits.clear(); el_numberOfValidTrackerHits.clear();
    el_IVF_df.clear(); el_IVF_ntracks.clear(); el_IVF_elid.clear();
    el_IVF_x.clear(); el_IVF_y.clear(); el_IVF_z.clear(); el_IVF_cx.clear(); el_IVF_cy.clear(); el_IVF_cz.clear(); el_IVF_chi2.clear(); el_IVF_pt.clear(); el_IVF_eta.clear(); el_IVF_phi.clear(); el_IVF_E.clear(); el_IVF_mass.clear();
    el_IVF_trackcharge.clear(); el_IVF_trackelid.clear(); el_IVF_trackvtxid.clear();
    el_IVF_trackpt.clear(); el_IVF_tracketa.clear(); el_IVF_trackphi.clear(); el_IVF_trackE.clear(); el_IVF_trackdxy.clear(); el_IVF_trackdz.clear();
    el_IVF_tracksignedIP2D.clear(); el_IVF_tracksignedIP2Dsig.clear(); el_IVF_tracksignedIP3D.clear(); el_IVF_tracksignedIP3Dsig.clear();
    
    el_jetPtRatio.clear(); el_jetPtRel.clear();
    el_jetIdx.clear(); el_jetSelectedChargedMultiplicity.clear();
    el_jetFatIdx.clear(); el_jetSubIdx.clear();
    el_relIso0p4.clear();
    el_sigmaIetaIeta.clear(); el_deltaPhiSuperClusterTrack.clear(); el_deltaEtaSuperClusterTrack.clear(); el_eInvMinusPInv.clear(); el_hOverE.clear();    
    el_dxy.clear(); el_dz.clear(); el_3dIP.clear(); el_3dIPSig.clear();
    el_IVF_signedIP2D.clear(); el_IVF_signedIP2Dsig.clear(); el_IVF_signedIP3D.clear(); el_IVF_signedIP3Dsig.clear();
    
    mu_idx.clear();
    mu_lIVF_match.clear();
    mu_innerTrackValidFraction.clear(); mu_globalTrackNormalizedChi2.clear(); mu_CQChi2Position.clear(); mu_CQTrackKink.clear();
    mu_numberOfMatchedStation.clear(); mu_numberOfValidPixelHits.clear(); mu_numberOfValidTrackerHits.clear(); mu_numberInnerHitsMissing.clear(); mu_trackerLayersWithMeasurement.clear(); mu_numberInnerHits.clear();
    mu_IVF_df.clear(); mu_IVF_ntracks.clear(); mu_IVF_muid.clear();
    mu_IVF_x.clear(); mu_IVF_y.clear(); mu_IVF_z.clear(); mu_IVF_cx.clear(); mu_IVF_cy.clear(); mu_IVF_cz.clear(); mu_IVF_chi2.clear(); mu_IVF_pt.clear(); mu_IVF_eta.clear(); mu_IVF_phi.clear(); mu_IVF_E.clear(); mu_IVF_mass.clear();
    mu_IVF_trackcharge.clear(); mu_IVF_trackmuid.clear(); mu_IVF_trackvtxid.clear();
    mu_IVF_trackpt.clear(); mu_IVF_tracketa.clear(); mu_IVF_trackphi.clear(); mu_IVF_trackE.clear(); mu_IVF_trackdxy.clear(); mu_IVF_trackdz.clear();
    mu_IVF_tracksignedIP2D.clear(); mu_IVF_tracksignedIP2Dsig.clear(); mu_IVF_tracksignedIP3D.clear(); mu_IVF_tracksignedIP3Dsig.clear();
    
    mu_jetPtRatio.clear(); mu_jetPtRel.clear();
    mu_jetIdx.clear(); mu_jetSelectedChargedMultiplicity.clear();
    mu_jetFatIdx.clear(); mu_jetSubIdx.clear();
    mu_relIso0p4.clear();
    mu_trackPt.clear(); mu_trackPtErr.clear();
    
    mu_dxy.clear(); mu_dz.clear(); mu_3dIP.clear(); mu_3dIPSig.clear();
    mu_IVF_signedIP2D.clear(); mu_IVF_signedIP2Dsig.clear(); mu_IVF_signedIP3D.clear(); mu_IVF_signedIP3Dsig.clear();
     
    int ntrack_max = 100;
    int nElectronsSel = 0;
    int nMuonsSel = 0;
    
    for(unsigned int i = 0; i < nElectrons; i++) {
      
      const pat::Electron & el = (*electronHandle)[i];
      
      if(el.gsfTrack().isNull()) continue;
      if(el.pt() < 7) continue;     
      if(fabs(el.eta()) > 2.5) continue;
      
      int ielCand = 0;
      for(edm::Ref<pat::PackedCandidateCollection> cand : el.associatedPackedPFCandidates()){	  
	if( cand.isNonnull() and cand.isAvailable() ) {
	  break;
	}       
	ielCand++;
      }
      
      el_idx.push_back(i);
      el_lIVF_match.push_back(false);
      
      el_isEB.push_back(el.isEB());
      el_isEE.push_back(el.isEE());
      el_superClusterOverP.push_back(el.eSuperClusterOverP());
      el_ecalEnergy.push_back(el.ecalEnergy());
      el_dEtaInSeed.push_back(std::abs(dEtaInSeed(&el)));
      el_numberInnerHitsMissing.push_back(el.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS));
      el_numberOfValidPixelHits.push_back((!el.gsfTrack().isNull())? el.gsfTrack()->hitPattern().numberOfValidPixelHits() : 0);
      el_numberOfValidTrackerHits.push_back((!el.gsfTrack().isNull())? el.gsfTrack()->hitPattern().numberOfValidTrackerHits() : 0);
      
      el_relIso0p4.push_back(getPFIso(el));
      el_sigmaIetaIeta.push_back(el.full5x5_sigmaIetaIeta());
      el_deltaPhiSuperClusterTrack.push_back(fabs(el.deltaPhiSuperClusterTrackAtVtx()));
      el_deltaEtaSuperClusterTrack.push_back(fabs(el.deltaEtaSuperClusterTrackAtVtx()));
      el_eInvMinusPInv.push_back((1.0 - el.eSuperClusterOverP())/el.correctedEcalEnergy());
      el_hOverE.push_back(el.hadronicOverEm());
      
      el_dxy.push_back(el.dB(pat::Electron::PV2D));
      el_dz.push_back(el.dB(pat::Electron::PVDZ));
      el_3dIP.push_back(el.dB(pat::Electron::PV3D));
      el_3dIPSig.push_back(fabs(el.dB(pat::Electron::PV3D)/el.edB(pat::Electron::PV3D)));
      
      fillLeptonJetVariables(&el, NULL, jetHandle, pv, *rhoHandle);

      const reco::Candidate *el_cand = dynamic_cast<const reco::Candidate*>(&el);
      el_jetFatIdx.push_back(findMatchedJet(*el_cand, jetFatHandle));
      el_jetSubIdx.push_back(findMatchedJet(*el_cand, jetSubHandle));
      
      bool new_vtx = false;
      double dR, deta, normchi2;
      double mindR = 20, minnormchi2 = 10000;
      int nVtx = 0;
      reco::Vertex *vtxDisp = NULL;
      for(const reco::Vertex& vtx : secVertices) {
	for(reco::Vertex::trackRef_iterator vtxTrackref = vtx.tracks_begin(); vtxTrackref != vtx.tracks_end(); vtxTrackref++) {
	  reco::TrackRef vtxTrack = vtxTrackref->castTo<reco::TrackRef>();
	  for(edm::Ref<pat::PackedCandidateCollection> cand : el.associatedPackedPFCandidates()) {	       
	    dR       = reco::deltaR(cand->eta(), cand->phi(), vtxTrack->eta(), vtxTrack->phi());
	    deta     = fabs(cand->eta() - vtxTrack->eta());
	    normchi2 = fabs(vtx.chi2()/vtx.ndof());
	    
	    if((dR < 0.05 or (dR < 0.1 and deta < 0.03)) and (dR < mindR or (dR == mindR and normchi2 < minnormchi2))) {	       
	      new_vtx = true;
	      vtxDisp = const_cast<reco::Vertex*>(&vtx);
	      el_lIVF_match[nElectronsSel] = true;
	      mindR       = dR;
	      minnormchi2 = normchi2;
	    }
	  }
	}
	
	if(new_vtx) {
	  el_IVF_x.push_back(vtx.x());
	  el_IVF_y.push_back(vtx.y());
	  el_IVF_z.push_back(vtx.z());
	  el_IVF_cx.push_back(vtx.xError());
	  el_IVF_cy.push_back(vtx.yError());
	  el_IVF_cz.push_back(vtx.zError());
	  el_IVF_df.push_back(vtx.ndof());
	  el_IVF_chi2.push_back(vtx.chi2());
	  el_IVF_pt.push_back(vtx.p4().pt());
	  el_IVF_eta.push_back(vtx.p4().eta());
	  el_IVF_phi.push_back(vtx.p4().phi());
	  el_IVF_E.push_back(vtx.p4().energy());
	  el_IVF_mass.push_back(vtx.p4().mass());
	  el_IVF_elid.push_back(nElectronsSel);
	  
	  el_IVF_ntracks.push_back(0);
	  for(reco::Vertex::trackRef_iterator vtxTrackref = vtx.tracks_begin(); vtxTrackref != vtx.tracks_end(); vtxTrackref++) {
	    if(el_IVF_ntracks.back() == ntrack_max) break;
	    reco::TrackRef vtxTrack = vtxTrackref->castTo<reco::TrackRef>();
	    const auto& trk = theB->build(vtxTrack);
	    Global3DVector dir(vtxTrack->px(), vtxTrack->py(), vtxTrack->pz());
	    const auto& ip2d = IPTools::signedTransverseImpactParameter(trk, dir, *vtxDisp);
	    const auto& ip3d = IPTools::signedImpactParameter3D(trk, dir, *vtxDisp);
	    el_IVF_tracksignedIP2D.push_back(ip2d.second.value());
	    el_IVF_tracksignedIP3D.push_back(ip3d.second.value());
	    el_IVF_tracksignedIP2Dsig.push_back(ip2d.second.significance());
	    el_IVF_tracksignedIP3Dsig.push_back(ip3d.second.significance());
	    el_IVF_trackpt.push_back(vtxTrack->pt());
	    el_IVF_tracketa.push_back(vtxTrack->eta());
	    el_IVF_trackphi.push_back(vtxTrack->phi());
	    el_IVF_trackE.push_back(vtxTrack->p());
	    el_IVF_trackcharge.push_back(vtxTrack->charge());
	    el_IVF_trackdxy.push_back(std::abs(vtxTrack->dxy(pv.position())));
	    el_IVF_trackdz.push_back(std::abs(vtxTrack->dz(pv.position())));
	    el_IVF_trackelid.push_back(nElectronsSel);
	    el_IVF_trackvtxid.push_back(nVtx);
	    el_IVF_ntracks.back()++;	    
	  }
	  nVtx++;
	  new_vtx = false;

	  auto track = el.gsfTrack();
	  if( track.isNonnull() ) {
	    const auto& trk = theB->build(track);
	    Global3DVector dir(track->px(), track->py(), track->pz());
	    const auto& ip2d = IPTools::signedTransverseImpactParameter(trk, dir, *vtxDisp);
	    const auto& ip3d = IPTools::signedImpactParameter3D(trk, dir, *vtxDisp);
	    el_IVF_signedIP2D.push_back(ip2d.second.value());
	    el_IVF_signedIP3D.push_back(ip3d.second.value());
	    el_IVF_signedIP2Dsig.push_back(ip2d.second.significance());
	    el_IVF_signedIP3Dsig.push_back(ip3d.second.significance());
	  } else {
	    el_IVF_signedIP2D.push_back(-999);
	    el_IVF_signedIP3D.push_back(-999);
	    el_IVF_signedIP2Dsig.push_back(-999);
	    el_IVF_signedIP3Dsig.push_back(-999);	    
	  }
	}
      }
      nElectronsSel += 1;
    }
    
    for(unsigned int i = 0; i < nMuons; i++) {
      
      const pat::Muon & mu = (*muonHandle)[i];
      
      if(mu.innerTrack().isNull()) continue;
      if(mu.pt() < 5) continue;
      if(fabs(mu.eta()) > 2.4) continue;
      if(!mu.isPFMuon()) continue;
      if(!(mu.isTrackerMuon() || mu.isGlobalMuon())) continue;
      
      mu_idx.push_back(i);
      mu_lIVF_match.push_back(false);
      
      mu_innerTrackValidFraction.push_back((!mu.innerTrack().isNull()) ? mu.innerTrack()->validFraction() : -1);
      mu_globalTrackNormalizedChi2.push_back((!mu.globalTrack().isNull()) ? mu.globalTrack()->normalizedChi2() : -1);
      mu_CQChi2Position.push_back(mu.combinedQuality().chi2LocalPosition);
      mu_CQTrackKink.push_back(mu.combinedQuality().trkKink);
      mu_numberOfMatchedStation.push_back(mu.numberOfMatchedStations());
      mu_numberOfValidPixelHits.push_back((!mu.innerTrack().isNull()) ? mu.innerTrack()->hitPattern().numberOfValidPixelHits() : 0);
      mu_numberOfValidTrackerHits.push_back((!mu.innerTrack().isNull()) ? mu.innerTrack()->hitPattern().numberOfValidTrackerHits() : 0);
      mu_numberInnerHitsMissing.push_back(mu.innerTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS));
      mu_trackerLayersWithMeasurement.push_back((!mu.innerTrack().isNull()) ? mu.innerTrack()->hitPattern().trackerLayersWithMeasurement() : 0);
      mu_numberInnerHits.push_back((!mu.globalTrack().isNull()) ? mu.globalTrack()->hitPattern().numberOfValidMuonHits() : (!mu.outerTrack().isNull() ? mu.outerTrack()->hitPattern().numberOfValidMuonHits() : 0));
      
      mu_relIso0p4.push_back(getPFIso(mu));
      mu_trackPt.push_back(mu.innerTrack()->pt());
      mu_trackPtErr.push_back(mu.innerTrack()->ptError());
      
      mu_dxy.push_back(mu.dB(pat::Muon::PV2D));
      mu_dz.push_back(mu.dB(pat::Muon::PVDZ));
      mu_3dIP.push_back(mu.dB(pat::Muon::PV3D));
      mu_3dIPSig.push_back(fabs(mu.dB(pat::Muon::PV3D)/mu.edB(pat::Muon::PV3D)));
      
      fillLeptonJetVariables(NULL, &mu, jetHandle, pv, *rhoHandle);

      const reco::Candidate *mu_cand = dynamic_cast<const reco::Candidate*>(&mu);
      mu_jetFatIdx.push_back(findMatchedJet(*mu_cand, jetFatHandle));
      mu_jetSubIdx.push_back(findMatchedJet(*mu_cand, jetSubHandle));      
      
      bool new_vtx = false;
      double ptdiff, normchi2;
      double minptdiff = 10, minnormchi2 = 10000;
      int nVtx = 0;
      reco::Vertex *vtxDisp = NULL;
      for(const reco::Vertex& vtx : secVertices) {
	for(reco::Vertex::trackRef_iterator vtxTrackref = vtx.tracks_begin(); vtxTrackref != vtx.tracks_end(); vtxTrackref++) {
	  reco::TrackRef vtxTrack = vtxTrackref->castTo<reco::TrackRef>();
	  for( size_t iCand=0;iCand<mu.numberOfSourceCandidatePtrs();++iCand ) {
	    if( !(mu.sourceCandidatePtr(iCand).isNonnull() and mu.sourceCandidatePtr(iCand).isAvailable()) ) continue;
	    ptdiff   = fabs(mu.sourceCandidatePtr(iCand)->pt() - vtxTrack->pt());
	    normchi2 = fabs(vtx.chi2()/vtx.ndof());
	    
	    if(ptdiff < 0.001 and (ptdiff < minptdiff or (ptdiff == minptdiff and normchi2 < minnormchi2))) {
	      new_vtx = true;
	      vtxDisp = const_cast<reco::Vertex*>(&vtx);
	      mu_lIVF_match[nMuonsSel] = true;
	      minptdiff   = ptdiff;
	      minnormchi2 = normchi2;
	    }
	  }
	}       
	if(new_vtx) {
	  mu_IVF_x.push_back(vtx.x());
	  mu_IVF_y.push_back(vtx.y());
	  mu_IVF_z.push_back(vtx.z());
	  mu_IVF_cx.push_back(vtx.xError());
	  mu_IVF_cy.push_back(vtx.yError());
	  mu_IVF_cz.push_back(vtx.zError());
	  mu_IVF_df.push_back(vtx.ndof());
	  mu_IVF_chi2.push_back(vtx.chi2());
	  mu_IVF_pt.push_back(vtx.p4().pt());
	  mu_IVF_eta.push_back(vtx.p4().eta());
	  mu_IVF_phi.push_back(vtx.p4().phi());
	  mu_IVF_E.push_back(vtx.p4().energy());
	  mu_IVF_mass.push_back(vtx.p4().mass());
	  mu_IVF_muid.push_back(nMuonsSel);
	  
	  mu_IVF_ntracks.push_back(0);
	  for(reco::Vertex::trackRef_iterator vtxTrackref = vtx.tracks_begin(); vtxTrackref != vtx.tracks_end(); vtxTrackref++) {
	    if(mu_IVF_ntracks.back() == ntrack_max) break;
	    reco::TrackRef vtxTrack = vtxTrackref->castTo<reco::TrackRef>();
	    const auto& trk = theB->build(vtxTrack);
	    Global3DVector dir(vtxTrack->px(), vtxTrack->py(), vtxTrack->pz());
	    const auto& ip2d = IPTools::signedTransverseImpactParameter(trk, dir, *vtxDisp);
	    const auto& ip3d = IPTools::signedImpactParameter3D(trk, dir, *vtxDisp);
	    mu_IVF_tracksignedIP2D.push_back(ip2d.second.value());
	    mu_IVF_tracksignedIP3D.push_back(ip3d.second.value());
	    mu_IVF_tracksignedIP2Dsig.push_back(ip2d.second.significance());
	    mu_IVF_tracksignedIP3Dsig.push_back(ip3d.second.significance());
	    mu_IVF_trackpt.push_back(vtxTrack->pt());
	    mu_IVF_tracketa.push_back(vtxTrack->eta());
	    mu_IVF_trackphi.push_back(vtxTrack->phi());
	    mu_IVF_trackE.push_back(vtxTrack->p());
	    mu_IVF_trackcharge.push_back(vtxTrack->charge());
	    mu_IVF_trackdxy.push_back(std::abs(vtxTrack->dxy(pv.position())));
	    mu_IVF_trackdz.push_back(std::abs(vtxTrack->dz(pv.position())));
	    mu_IVF_trackmuid.push_back(nMuonsSel);
	    mu_IVF_trackvtxid.push_back(nVtx);
	    mu_IVF_ntracks.back()++;
	  }
	  nVtx++;
	  new_vtx = false;

	  auto track = mu.innerTrack();
	  if( track.isNonnull() ) {
	    const auto& trk = theB->build(track);
	    Global3DVector dir(track->px(), track->py(), track->pz());
	    const auto& ip2d = IPTools::signedTransverseImpactParameter(trk, dir, *vtxDisp);
	    const auto& ip3d = IPTools::signedImpactParameter3D(trk, dir, *vtxDisp);
	    mu_IVF_signedIP2D.push_back(ip2d.second.value());
	    mu_IVF_signedIP3D.push_back(ip3d.second.value());
	    mu_IVF_signedIP2Dsig.push_back(ip2d.second.significance());
	    mu_IVF_signedIP3Dsig.push_back(ip3d.second.significance());
	  } else {
	    mu_IVF_signedIP2D.push_back(-999);
	    mu_IVF_signedIP3D.push_back(-999);
	    mu_IVF_signedIP2Dsig.push_back(-999);
	    mu_IVF_signedIP3Dsig.push_back(-999);	    	    
	  }
	}	 
      }      
      nMuonsSel += 1;
    }
    
    auto dispJetElectronTab = std::make_unique<nanoaod::FlatTable>(nElectronsSel, "DispJetElectron", false, false);
    auto dispJetMuonTab = std::make_unique<nanoaod::FlatTable>(nMuonsSel, "DispJetMuon", false, false);
    
    dispJetElectronTab->addColumn<int>("idx", el_idx, "");
    dispJetElectronTab->addColumn<bool>("lIVF_match", el_lIVF_match, "");
    dispJetElectronTab->addColumn<bool>("isEB", el_isEB, "");
    dispJetElectronTab->addColumn<bool>("isEE", el_isEE, "");
    dispJetElectronTab->addColumn<float>("superClusterOverP", el_superClusterOverP, "");
    dispJetElectronTab->addColumn<float>("ecalEnergy", el_ecalEnergy, "");
    dispJetElectronTab->addColumn<float>("dEtaInSeed", el_dEtaInSeed, "");
    dispJetElectronTab->addColumn<int>("numberInnerHitsMissing", el_numberInnerHitsMissing, "");
    dispJetElectronTab->addColumn<int>("numberOfValidPixelHits", el_numberOfValidPixelHits, "");
    dispJetElectronTab->addColumn<int>("numberOfValidTrackerHits", el_numberOfValidTrackerHits, "");
    dispJetElectronTab->addColumn<float>("relIso0p4", el_relIso0p4, "");
    dispJetElectronTab->addColumn<float>("jetPtRatio", el_jetPtRatio, "");
    dispJetElectronTab->addColumn<float>("jetPtRel", el_jetPtRel, "");
    dispJetElectronTab->addColumn<int>("jetIdx", el_jetIdx, "");
    dispJetElectronTab->addColumn<int>("jetFatIdx", el_jetFatIdx, "");
    dispJetElectronTab->addColumn<int>("jetSubIdx", el_jetSubIdx, "");
    dispJetElectronTab->addColumn<int>("jetSelectedChargedMultiplicity", el_jetSelectedChargedMultiplicity, "");
    dispJetElectronTab->addColumn<float>("sigmaIetaIeta", el_sigmaIetaIeta, "");
    dispJetElectronTab->addColumn<float>("deltaPhiSuperClusterTrack", el_deltaPhiSuperClusterTrack, "");
    dispJetElectronTab->addColumn<float>("deltaEtaSuperClusterTrack", el_deltaEtaSuperClusterTrack, "");
    dispJetElectronTab->addColumn<float>("eInvMinusPInv", el_eInvMinusPInv, "");
    dispJetElectronTab->addColumn<float>("hOverE", el_hOverE, "");
    dispJetElectronTab->addColumn<float>("dxy", el_dxy, "");
    dispJetElectronTab->addColumn<float>("dz", el_dz, "");
    dispJetElectronTab->addColumn<float>("3dIP", el_3dIP, "");
    dispJetElectronTab->addColumn<float>("3dIPSig", el_3dIPSig, "");
    
    auto dispJetElectronVtxTab = std::make_unique<nanoaod::FlatTable>(el_IVF_x.size(), "DispJetElectronVtx", false, false);
    dispJetElectronVtxTab->addColumn<int>("IVF_df", el_IVF_df, "");
    dispJetElectronVtxTab->addColumn<int>("IVF_ntracks", el_IVF_ntracks, "");
    dispJetElectronVtxTab->addColumn<int>("IVF_elid", el_IVF_elid, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_x", el_IVF_x, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_y", el_IVF_y, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_z", el_IVF_z, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_cx", el_IVF_cx, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_cy", el_IVF_cy, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_cz", el_IVF_cz, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_chi2", el_IVF_chi2, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_pt", el_IVF_pt, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_eta", el_IVF_eta, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_phi", el_IVF_phi, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_E", el_IVF_E, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_mass", el_IVF_mass, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_signedIP2D", el_IVF_signedIP2D, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_signedIP2Dsig", el_IVF_signedIP2Dsig, "");   
    dispJetElectronVtxTab->addColumn<float>("IVF_signedIP3D", el_IVF_signedIP3D, "");
    dispJetElectronVtxTab->addColumn<float>("IVF_signedIP3Dsig", el_IVF_signedIP3Dsig, "");   
    
    int nTracksElectron = 0;
    for( unsigned int iv=0;iv<el_IVF_ntracks.size();iv++ ) {
      nTracksElectron += std::min(el_IVF_ntracks[iv], ntrack_max);
    }
    auto dispJetElectronTrkTab = std::make_unique<nanoaod::FlatTable>(nTracksElectron, "DispJetElectronTrk", false, false);
    dispJetElectronTrkTab->addColumn<int>("IVF_trackcharge", el_IVF_trackcharge, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_trackpt", el_IVF_trackpt, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_tracketa", el_IVF_tracketa, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_trackphi", el_IVF_trackphi, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_trackE", el_IVF_trackE, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_trackdxy", el_IVF_trackdxy, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_trackdz", el_IVF_trackdz, "");
    dispJetElectronTrkTab->addColumn<int>("IVF_trackelid", el_IVF_trackelid, "");
    dispJetElectronTrkTab->addColumn<int>("IVF_trackvtxid", el_IVF_trackvtxid, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_tracksignedIP2D", el_IVF_tracksignedIP2D, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_tracksignedIP2Dsig", el_IVF_tracksignedIP2Dsig, "");   
    dispJetElectronTrkTab->addColumn<float>("IVF_tracksignedIP3D", el_IVF_tracksignedIP3D, "");
    dispJetElectronTrkTab->addColumn<float>("IVF_tracksignedIP3Dsig", el_IVF_tracksignedIP3Dsig, "");   
    
    dispJetMuonTab->addColumn<int>("idx", mu_idx, "");
    dispJetMuonTab->addColumn<bool>("lIVF_match", mu_lIVF_match, "");
    dispJetMuonTab->addColumn<float>("innerTrackValidFraction", mu_innerTrackValidFraction, "");
    dispJetMuonTab->addColumn<float>("globalTrackNormalizedChi2", mu_globalTrackNormalizedChi2, "");
    dispJetMuonTab->addColumn<float>("CQChi2Position", mu_CQChi2Position, "");
    dispJetMuonTab->addColumn<float>("CQTrackKink", mu_CQTrackKink, "");
    dispJetMuonTab->addColumn<int>("numberOfMatchedStation", mu_numberOfMatchedStation, "");
    dispJetMuonTab->addColumn<int>("numberOfValidPixelHits", mu_numberOfValidPixelHits, "");
    dispJetMuonTab->addColumn<int>("numberOfValidTrackerHits", mu_numberOfValidTrackerHits, "");
    dispJetMuonTab->addColumn<int>("numberInnerHitsMissing", mu_numberInnerHitsMissing, "");
    dispJetMuonTab->addColumn<int>("trackerLayersWithMeasurement", mu_trackerLayersWithMeasurement, "");
    dispJetMuonTab->addColumn<int>("numberInnerHits", mu_numberInnerHits, "");
    dispJetMuonTab->addColumn<float>("relIso0p4", mu_relIso0p4, "");
    dispJetMuonTab->addColumn<float>("jetPtRatio", mu_jetPtRatio, "");
    dispJetMuonTab->addColumn<float>("jetPtRel", mu_jetPtRel, "");
    dispJetMuonTab->addColumn<int>("jetIdx", mu_jetIdx, "");
    dispJetMuonTab->addColumn<int>("jetFatIdx", mu_jetFatIdx, "");
    dispJetMuonTab->addColumn<int>("jetSubIdx", mu_jetSubIdx, "");
    dispJetMuonTab->addColumn<int>("jetSelectedChargedMultiplicity", mu_jetSelectedChargedMultiplicity, "");
    dispJetMuonTab->addColumn<float>("trackPt", mu_trackPt, "");
    dispJetMuonTab->addColumn<float>("trackPtErr", mu_trackPtErr, "");
    dispJetMuonTab->addColumn<float>("dxy", mu_dxy, "");
    dispJetMuonTab->addColumn<float>("dz", mu_dz, "");
    dispJetMuonTab->addColumn<float>("3dIP", mu_3dIP, "");
    dispJetMuonTab->addColumn<float>("3dIPSig", mu_3dIPSig, "");
     
    auto dispJetMuonVtxTab = std::make_unique<nanoaod::FlatTable>(mu_IVF_x.size(), "DispJetMuonVtx", false, false);
    dispJetMuonVtxTab->addColumn<int>("IVF_df", mu_IVF_df, "");
    dispJetMuonVtxTab->addColumn<int>("IVF_ntracks", mu_IVF_ntracks, "");
    dispJetMuonVtxTab->addColumn<int>("IVF_muid", mu_IVF_muid, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_x", mu_IVF_x, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_y", mu_IVF_y, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_z", mu_IVF_z, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_cx", mu_IVF_cx, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_cy", mu_IVF_cy, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_cz", mu_IVF_cz, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_chi2", mu_IVF_chi2, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_pt", mu_IVF_pt, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_eta", mu_IVF_eta, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_phi", mu_IVF_phi, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_E", mu_IVF_E, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_mass", mu_IVF_mass, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_signedIP2D", mu_IVF_signedIP2D, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_signedIP2Dsig", mu_IVF_signedIP2Dsig, "");   
    dispJetMuonVtxTab->addColumn<float>("IVF_signedIP3D", mu_IVF_signedIP3D, "");
    dispJetMuonVtxTab->addColumn<float>("IVF_signedIP3Dsig", mu_IVF_signedIP3Dsig, "");   
    
    int nTracksMuon = 0;
    for( unsigned int iv=0;iv<mu_IVF_ntracks.size();iv++ ) {
      nTracksMuon += std::min(mu_IVF_ntracks[iv], ntrack_max);
    }
    auto dispJetMuonTrkTab = std::make_unique<nanoaod::FlatTable>(nTracksMuon, "DispJetMuonTrk", false, false);
    dispJetMuonTrkTab->addColumn<int>("IVF_trackcharge", mu_IVF_trackcharge, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_trackpt", mu_IVF_trackpt, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_tracketa", mu_IVF_tracketa, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_trackphi", mu_IVF_trackphi, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_trackE", mu_IVF_trackE, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_trackdxy", mu_IVF_trackdxy, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_trackdz", mu_IVF_trackdz, "");
    dispJetMuonTrkTab->addColumn<int>("IVF_trackmuid", mu_IVF_trackmuid, "");
    dispJetMuonTrkTab->addColumn<int>("IVF_trackvtxid", mu_IVF_trackvtxid, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_tracksignedIP2D", mu_IVF_tracksignedIP2D, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_tracksignedIP2Dsig", mu_IVF_tracksignedIP2Dsig, "");   
    dispJetMuonTrkTab->addColumn<float>("IVF_tracksignedIP3D", mu_IVF_tracksignedIP3D, "");
    dispJetMuonTrkTab->addColumn<float>("IVF_tracksignedIP3Dsig", mu_IVF_tracksignedIP3Dsig, "");   
    
    iEvent.put(std::move(dispJetElectronTab), "DispJetElectron");
    iEvent.put(std::move(dispJetElectronVtxTab), "DispJetElectronVtx");
    iEvent.put(std::move(dispJetElectronTrkTab), "DispJetElectronTrk");
    iEvent.put(std::move(dispJetMuonTab), "DispJetMuon");
    iEvent.put(std::move(dispJetMuonVtxTab), "DispJetMuonVtx");
    iEvent.put(std::move(dispJetMuonTrkTab), "DispJetMuonTrk");
  }      
};

float DispJetTableProducer::dEtaInSeed(const pat::Electron* el) const {   
  if( el->superCluster().isNonnull() and el->superCluster()->seed().isNonnull()) return el->deltaEtaSuperClusterTrackAtVtx() - el->superCluster()->eta() + el->superCluster()->seed()->eta();
  else return std::numeric_limits<float>::max();
}

template< typename T1, typename T2 > bool isSourceCandidatePtrMatch( const T1& lhs, const T2& rhs ) {
  
  for( size_t lhsIndex = 0; lhsIndex < lhs.numberOfSourceCandidatePtrs(); ++lhsIndex ) {
    auto lhsSourcePtr = lhs.sourceCandidatePtr( lhsIndex );
    for( size_t rhsIndex = 0; rhsIndex < rhs.numberOfSourceCandidatePtrs(); ++rhsIndex ) {
      auto rhsSourcePtr = rhs.sourceCandidatePtr( rhsIndex );
      if( lhsSourcePtr == rhsSourcePtr ) {
	return true;
      }
    }
  }
  
  return false;
}

int DispJetTableProducer::findMatchedJet(const reco::Candidate& lepton, const edm::Handle< std::vector< pat::Jet > >& jets) {
  
  int iJet = -1;
  
  unsigned int nJets = jets->size();
  
  for(unsigned int i = 0; i < nJets; i++) {
    const pat::Jet & jet = (*jets)[i];
    if( isSourceCandidatePtrMatch( lepton, jet ) ) {
      return i;
    }
  }
  
  return iJet;
}

void DispJetTableProducer::fillLeptonJetVariables(const reco::GsfElectron *el, const reco::Muon *mu, edm::Handle< std::vector< pat::Jet > >& jets, const reco::Vertex& vertex, const double rho) {
   
  const reco::Candidate *cand = (el) ? dynamic_cast<const reco::Candidate*>(el) : dynamic_cast<const reco::Candidate*>(mu);
  int matchedJetIdx = findMatchedJet( *cand, jets );
  
  bool isElectron = (el);
  
  if( isElectron ) el_jetIdx.push_back(matchedJetIdx);
  else mu_jetIdx.push_back(matchedJetIdx);

  if( matchedJetIdx < 0 ) {
    if( isElectron ) {
      float ptRatio = ( 1. / ( 1. + el_relIso0p4.back() ) );
      el_jetPtRatio.push_back(ptRatio);
      el_jetPtRel.push_back(0);
      el_jetSelectedChargedMultiplicity.push_back(0);
    } else {	   
      float ptRatio = ( 1. / ( 1. + mu_relIso0p4.back() ) );
      mu_jetPtRatio.push_back(ptRatio);	 
      mu_jetPtRel.push_back(0);
      mu_jetSelectedChargedMultiplicity.push_back(0);
    }
  } else {
    const pat::Jet& jet = (*jets)[matchedJetIdx];
    auto rawJetP4 = jet.correctedP4("Uncorrected");
    auto leptonP4 = cand->p4();
    
    bool leptonEqualsJet = ( ( rawJetP4 - leptonP4 ).P() < 1e-4 );
    
    if( leptonEqualsJet ) {
      if( isElectron ) {
	el_jetPtRatio.push_back(1);
	el_jetPtRel.push_back(0);
	el_jetSelectedChargedMultiplicity.push_back(0);
      } else {
	mu_jetPtRatio.push_back(1);
	mu_jetPtRel.push_back(0);
	mu_jetSelectedChargedMultiplicity.push_back(0);	    
      }	 
    } else {
      auto L1JetP4 = jet.correctedP4("L1FastJet");
      double L2L3JEC = jet.pt()/L1JetP4.pt();
      auto lepAwareJetP4 = ( L1JetP4 - leptonP4 )*L2L3JEC + leptonP4;
      
      float ptRatio = cand->pt() / lepAwareJetP4.pt();
      float ptRel = leptonP4.Vect().Cross( (lepAwareJetP4 - leptonP4 ).Vect().Unit() ).R();
      if( isElectron ) {
	el_jetPtRatio.push_back(ptRatio);
	el_jetPtRel.push_back(ptRel);
	el_jetSelectedChargedMultiplicity.push_back(0);
      } else {
	mu_jetPtRatio.push_back(ptRatio);
	mu_jetPtRel.push_back(ptRel);
	mu_jetSelectedChargedMultiplicity.push_back(0);
      }
      
      for( const auto &daughterPtr : jet.daughterPtrVector() ) {
	const pat::PackedCandidate& daughter = *( (const pat::PackedCandidate*) daughterPtr.get() );
	
	if( daughter.charge() == 0 ) continue;
	if( daughter.fromPV() < 2 ) continue;
	if( reco::deltaR( daughter, *cand ) > 0.4 ) continue;
	if( !daughter.hasTrackDetails() ) continue;
	
	auto daughterTrack = daughter.pseudoTrack();
	    
	if( daughterTrack.pt() <= 1 ) continue;
	if( daughterTrack.hitPattern().numberOfValidHits() < 8 ) continue;
	if( daughterTrack.hitPattern().numberOfValidPixelHits() < 2 ) continue;
	if( daughterTrack.normalizedChi2() >= 5 ) continue;
	if( std::abs( daughterTrack.dz( vertex.position() ) ) >= 17 ) continue;
	if( std::abs( daughterTrack.dxy( vertex.position() ) ) >= 0.2 ) continue;
	if( isElectron ) ++el_jetSelectedChargedMultiplicity.back();
	else ++mu_jetSelectedChargedMultiplicity.back();
      }
    }      
  }
}

float DispJetTableProducer::getPFIso(const pat::Muon& muon) const {
  return (muon.pfIsolationR04().sumChargedHadronPt +
	  std::max(0.,
		   muon.pfIsolationR04().sumNeutralHadronEt + muon.pfIsolationR04().sumPhotonEt -
		   0.5 * muon.pfIsolationR04().sumPUPt)) / muon.pt();
}

float DispJetTableProducer::getPFIso(const pat::Electron& electron) const {
  return electron.userFloat("PFIsoAll04") / electron.pt();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DispJetTableProducer);
