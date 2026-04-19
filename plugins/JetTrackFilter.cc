#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"

class JetTrackFilter : public edm::global::EDProducer<> {
public:
  explicit JetTrackFilter(const edm::ParameterSet& iConfig) :
    tracksToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))),
    jetsToken_(consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("jets"))),
    dR_(iConfig.getParameter<double>("coneSize")) {
    produces<reco::TrackCollection>();
  }

  void produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup&) const override {
    auto out = std::make_unique<reco::TrackCollection>();
    auto tracks = iEvent.getHandle(tracksToken_);
    auto jets = iEvent.getHandle(jetsToken_);

    for (const auto& track : *tracks) {
      for (const auto& jet : *jets) {
        if (reco::deltaR(track, jet) < dR_) {
          out->push_back(track);
          break;
        }
      }
    }
    iEvent.put(std::move(out));
  }

private:
  edm::EDGetTokenT<reco::TrackCollection> tracksToken_;
  edm::EDGetTokenT<std::vector<pat::Jet>> jetsToken_;
  double dR_;
};

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(JetTrackFilter);
