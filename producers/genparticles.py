from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers to get the genParticles from the ditaupair
####################
MMGenPair = Producer(
    name="MMGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Muon_indexToGen, nanoAOD.Muon_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["vbf", "zh", "wh"],
)

MMTrueGenPair = Producer(
    name="GenPair",
    call="ditau_pairselection::buildtruegenpair({df}, {input}, {output}, {truegen_mother_pdgid}, {truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motherid,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegenpair],
    scopes=["vbf", "zh", "wh"],
)
####################
# Set of general producers for Gen DiTauPair Quantities
####################

LVGenParticle1 = Producer(
    name="LVGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.gen_dileptonpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["vbf", "zh", "wh"],
)
LVGenParticle2 = Producer(
    name="LVGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.gen_dileptonpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["vbf", "zh", "wh"],
)
LVTrueGenParticle1 = Producer(
    name="LVTrueGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.truegenpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["vbf", "zh", "wh"],
)
LVTrueGenParticle2 = Producer(
    name="LVTrueGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.truegenpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["vbf", "zh", "wh"],
)
gen_pt_1 = Producer(
    name="gen_pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_pt_1],
    scopes=["vbf", "zh", "wh"],
)
gen_pt_2 = Producer(
    name="gen_pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_pt_2],
    scopes=["vbf", "zh", "wh"],
)
gen_eta_1 = Producer(
    name="gen_eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_eta_1],
    scopes=["vbf", "zh", "wh"],
)
gen_eta_2 = Producer(
    name="gen_eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_eta_2],
    scopes=["vbf", "zh", "wh"],
)
gen_phi_1 = Producer(
    name="gen_phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_phi_1],
    scopes=["vbf", "zh", "wh"],
)
gen_phi_2 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_phi_2],
    scopes=["vbf", "zh", "wh"],
)
gen_mass_1 = Producer(
    name="gen_mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_mass_1],
    scopes=["vbf", "zh", "wh"],
)
gen_mass_2 = Producer(
    name="gen_mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_mass_2],
    scopes=["vbf", "zh", "wh"],
)
gen_pdgid_1 = Producer(
    name="gen_pdgid_1",
    call="quantities::pdgid({df}, {output}, 0, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_1],
    scopes=["vbf", "zh", "wh"],
)
gen_pdgid_2 = Producer(
    name="gen_pdgid_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["vbf", "zh", "wh"],
)
gen_m_vis = Producer(
    name="gen_m_vis",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.gen_p4_1, q.gen_p4_2],
    output=[q.gen_m_vis],
    scopes=["vbf", "zh", "wh"],
)
gen_match_2 = Producer(
    name="gen_match_2",
    call="quantities::tau::genmatch({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Tau_genMatch],
    output=[q.gen_match_2],
    scopes=["vbf", "zh", "wh"],
)
gen_taujet_pt_1 = Producer(
    name="gen_taujet_pt_1",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 0, {input})",
    input=[
        q.dileptonpair,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_1],
    scopes=["vbf", "zh", "wh"],
)
gen_taujet_pt_2 = Producer(
    name="gen_taujet_pt_2",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 1, {input})",
    input=[
        q.dileptonpair,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_2],
    scopes=["vbf", "zh", "wh"],
)
UnrollGenMuLV1 = ProducerGroup(
    name="UnrollGenMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_1],
)
UnrollGenMuLV2 = ProducerGroup(
    name="UnrollGenMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_2],
)


MMGenDiTauPairQuantities = ProducerGroup(
    name="GenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh"],
    subproducers=[
        MMGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenMuLV1,
        UnrollGenMuLV2,
        gen_m_vis,
    ],
)
MMTrueGenDiTauPairQuantities = ProducerGroup(
    name="GenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh"],
    subproducers=[
        MMTrueGenPair,
        LVTrueGenParticle1,
        LVTrueGenParticle2,
        UnrollGenMuLV1,
        UnrollGenMuLV2,
        gen_m_vis,
    ],
)

EmbeddingGenWeight = Producer(
    name="EmbeddingGenWeight",
    call="basefunctions::rename<Float_t>({df}, {input}, {output})",
    input=[nanoAOD.genWeight],
    output=[q.emb_genWeight],
    scopes=["vbf", "zh", "wh"],
)


###############################
# Genmatching Triplet Quantities
###############################

EMTGenTriple = Producer(
    name="EMTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_indexToGen,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Tau_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["emt", "met"],
)
EMTTrueGenTriple = Producer(
    name="EMTTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["emt", "met"],
)
MMEGenTriple = Producer(
    name="EMTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Electron_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["wh"],
)
MMETrueGenTriple = Producer(
    name="MMETrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["wh"],
)
MMEGenTriple = Producer(
    name="MMEGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Electron_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["wh"],
)
EEMTrueGenTriple = Producer(
    name="EEMTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["eem"],
)
EEMGenTriple = Producer(
    name="EEMGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_indexToGen,
        nanoAOD.Electron_indexToGen,
        nanoAOD.Muon_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["eem"],
)
MMTGenTriple = Producer(
    name="MMTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Tau_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["mmt"],
)
MMTTrueGenTriple = Producer(
    name="MMTTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["mmt"],
)
ETTGenTriple = Producer(
    name="ETTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_indexToGen,
        nanoAOD.Tau_indexToGen,
        nanoAOD.Tau_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["ett"],
)
ETTTrueGenTriple = Producer(
    name="ETTTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["ett"],
)
MTTGenTriple = Producer(
    name="MTTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Tau_indexToGen,
        nanoAOD.Tau_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["mtt"],
)
MTTTrueGenTriple = Producer(
    name="MTTTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["mtt"],
)
####################
# Set of general producers for Gen DiTauPair Quantities
####################
LVGenParticle1 = Producer(
    name="LVGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
LVGenParticle2 = Producer(
    name="LVGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
LVGenParticle3 = Producer(
    name="LVGenParticle3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
LVTrueGenParticle_WH1 = Producer(
    name="LVTrueGenParticleWH1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
LVTrueGenParticleWH2 = Producer(
    name="LVTrueGenParticleWH2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
LVTrueGenParticleWH3 = Producer(
    name="LVTrueGenParticleWH3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_pt_1 = Producer(
    name="gen_pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_pt_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_pt_2 = Producer(
    name="gen_pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_pt_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_pt_3 = Producer(
    name="gen_pt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_pt_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_eta_1 = Producer(
    name="gen_eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_eta_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_eta_2 = Producer(
    name="gen_eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_eta_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_eta_3 = Producer(
    name="gen_eta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_eta_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_phi_1 = Producer(
    name="gen_phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_phi_1],
    scopes=[
        "emt",
        "met",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_phi_2 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_phi_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_phi_3 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_phi_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_mass_1 = Producer(
    name="gen_mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_mass_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_mass_2 = Producer(
    name="gen_mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_mass_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
gen_mass_3 = Producer(
    name="gen_mass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_mass_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_pdgid_1 = Producer(
    name="gen_pdgid_1",
    call="quantities::pdgid({df}, {output}, 0, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_1],
    scopes=["mmt", "ett", "mtt", "wh", "eem"],
)
gen_pdgid_WH_1 = Producer(
    name="gen_pdgid_WH_1",
    call="quantities::pdgid({df}, {output}, 0, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_1],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_pdgid_WH_2 = Producer(
    name="gen_pdgid_WH_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_pdgid_WH_3 = Producer(
    name="gen_pdgid_WH_3",
    call="quantities::pdgid({df}, {output}, 2, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_m_vis_WH = Producer(
    name="gen_m_vis_WH",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.gen_p4_2, q.gen_p4_3],
    output=[q.gen_m_vis],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
gen_taujet_WH_pt_2 = Producer(
    name="gen_taujet_WH_pt_2",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 1, {input})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_2],
    scopes=["ett", "mtt"],
)
gen_taujet_WH_pt_3 = Producer(
    name="gen_taujet_WH_pt_3",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 2, {input})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
UnrollGenMuLV2 = ProducerGroup(
    name="UnrollGenMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "mmt", "wh"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_WH_2],
)
UnrollGenElLV1 = ProducerGroup(
    name="UnrollGenElLV1",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "ett", "eem"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_WH_1],
)
UnrollGenMuLV1 = ProducerGroup(
    name="UnrollGenMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["met", "mmt", "mtt", "wh"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_WH_1],
)
UnrollGenElLV2 = ProducerGroup(
    name="UnrollGenElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["met", "eem"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_WH_2],
)
UnrollGenElLV3 = ProducerGroup(
    name="UnrollGenElLV3",
    call=None,
    input=None,
    output=None,
    scopes=["wh"],
    subproducers=[gen_pt_3, gen_eta_3, gen_phi_3, gen_mass_3, gen_pdgid_WH_3],
)
UnrollGenMuLV3 = ProducerGroup(
    name="UnrollGenMuLV3",
    call=None,
    input=None,
    output=None,
    scopes=["eem"],
    subproducers=[gen_pt_3, gen_eta_3, gen_phi_3, gen_mass_3, gen_pdgid_WH_3],
)
UnrollGenTauLV2 = ProducerGroup(
    name="UnrollGenLV2",
    call=None,
    input=None,
    output=None,
    scopes=["ett", "mtt"],
    subproducers=[
        gen_pt_2,
        gen_eta_2,
        gen_phi_2,
        gen_mass_2,
        gen_pdgid_WH_2,
        gen_taujet_WH_pt_2,
    ],
)
UnrollGenTauLV3 = ProducerGroup(
    name="UnrollGenLV3",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt", "ett", "mtt"],
    subproducers=[
        gen_pt_3,
        gen_eta_3,
        gen_phi_3,
        gen_mass_3,
        gen_pdgid_WH_3,
        gen_taujet_WH_pt_3,
    ],
)
EMTGenTripleQuantities = ProducerGroup(
    name="EMTGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[
        EMTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV1,
        UnrollGenMuLV2,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
METGenTripleQuantities = ProducerGroup(
    name="METGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[
        EMTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV2,
        UnrollGenMuLV1,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
MMTGenTripleQuantities = ProducerGroup(
    name="MMTGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mmt"],
    subproducers=[
        MMTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenMuLV2,
        UnrollGenMuLV1,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
ETTGenTripleQuantities = ProducerGroup(
    name="ETTGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["ett"],
    subproducers=[
        ETTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV1,
        UnrollGenTauLV2,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
MTTGenTripleQuantities = ProducerGroup(
    name="MTTGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mtt"],
    subproducers=[
        MTTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenTauLV2,
        UnrollGenMuLV1,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
MMEGenTripleQuantities = ProducerGroup(
    name="MMEGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["wh"],
    subproducers=[
        MMEGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV3,
        UnrollGenMuLV1,
        UnrollGenMuLV2,
        gen_m_vis_WH,
    ],
)
EEMGenTripleQuantities = ProducerGroup(
    name="EEMGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["eem"],
    subproducers=[
        EEMGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV1,
        UnrollGenElLV2,
        UnrollGenMuLV3,
        gen_m_vis_WH,
    ],
)
#######################
# DiTau Genmatching
#######################

GenPairForGenMatching = Producer(
    name="GenPairForGenMatching",
    call="genmatching::tau::hadronicGenTaus({df}, {output}, {input})",
    input=[
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_motheridx,
    ],
    output=[q.hadronic_gen_taus],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)
GenMatchP1 = Producer(
    name="GenMatchP1",
    call="genmatching::tau::genmatching_wh({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_1,
    ],
    output=[q.gen_match_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)

GenMatchP2 = Producer(
    name="GenMatchP2",
    call="genmatching::tau::genmatching_wh({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_2,
    ],
    output=[q.gen_match_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh",
        "eem",
    ],
)

GenMatchP3 = Producer(
    name="GenMatch_WH_P3",
    call="genmatching::tau::genmatching_wh({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_3,
    ],
    output=[q.gen_match_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)
GenMatching = ProducerGroup(
    name="GenMatching",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
    subproducers=[
        GenPairForGenMatching,
        GenMatchP1,
        GenMatchP2,
        GenMatchP3,
    ],
)