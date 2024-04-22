from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, ExtendedVectorProducer


####################
# Set of general producers for DiTauPair Quantities
####################
p4_123met = Producer(
    name="p4_123met",
    call="lorentzvectors::CombineP4s({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.p4_3, q.met_p4_recoilcorrected],
    output=[q.p4_123met],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
p4_23 = Producer(
    name="p4_23",
    call="lorentzvectors::CombineP4s({df}, {output}, {input})",
    input=[q.p4_2, q.p4_3],
    output=[q.p4_23],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
pt_1_uncorrected = Producer(
    name="pt_1_uncorrected",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_1_uncorrected],
    output=[q.pt_1_uncorrected],
    scopes=["eem"],
)
pt_2_uncorrected = Producer(
    name="pt_2_uncorrected",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_2_uncorrected],
    output=[q.pt_2_uncorrected],
    scopes=["eem"],
)
pt_3_uncorrected = Producer(
    name="pt_3_uncorrected",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_3_uncorrected],
    output=[q.pt_3_uncorrected],
    scopes=["eem"],
)
pt_1 = Producer(
    name="pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.pt_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
pt_2 = Producer(
    name="pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.pt_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
pt_3 = Producer(
    name="pt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.pt_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
eta_1 = Producer(
    name="eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.eta_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
eta_2 = Producer(
    name="eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.eta_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
eta_3 = Producer(
    name="eta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.eta_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
phi_1 = Producer(
    name="phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.phi_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
phi_2 = Producer(
    name="phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.phi_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
phi_3 = Producer(
    name="phi_3",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.phi_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
mass_1 = Producer(
    name="mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.mass_1],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
mass_2 = Producer(
    name="mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.mass_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
mass_3 = Producer(
    name="mass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.mass_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
m_vis = Producer(
    name="m_vis",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.p4_1, q.p4_2],
    output=[q.m_vis],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
pt_vis = Producer(
    name="pt_vis",
    call="quantities::pt_vis({df}, {output}, {input_vec})",
    input=[q.p4_1, q.p4_2],
    output=[q.pt_vis],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
p4_23_miss = Producer(
    name="p4_23_miss",
    call="lorentzvectors::scaleP4({df}, {output}, {input_vec}, {p4_23_miss_sf})",
    input=[q.p4_23],
    output=[q.p4_23_miss],
    scopes=["emt", "met", "mmt", "wh_mme", "wh_mmm", "eem", "ett", "mtt"],
)
pt_123met = Producer(
    name="pt_123met",
    call="quantities::pt({df}, {output}, {input_vec})",
    input=[q.p4_123met],
    output=[q.pt_123met],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
p4_H = Producer(
    name="p4_H",
    call="lorentzvectors::CombineP4s({df}, {output}, {input})",
    input=[q.p4_2, q.p4_3, q.p4_23_miss],
    output=[q.p4_H],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
m_tt = Producer(
    name="m_tt",
    call="quantities::mass({df}, {output}, {input_vec})",
    input=[q.p4_H],
    output=[q.m_tt],
    scopes=["emt", "met", "mmt", "wh_mme", "wh_mmm", "eem", "ett", "mtt"],
)
pt_W = Producer(
    name="pt_W",
    call="quantities::pt_W({df}, {output}, {input_vec})",
    input=[q.p4_1, q.met_p4_recoilcorrected, q.p4_23_miss],
    output=[q.pt_W],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaR_13 = Producer(
    name="deltaR_13",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_1, q.p4_3],
    output=[q.deltaR_13],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaR_23 = Producer(
    name="deltaR_23",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_2, q.p4_3],
    output=[q.deltaR_23],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaR_12 = Producer(
    name="deltaR_12",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2],
    output=[q.deltaR_12],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaPhi_12 = Producer(
    name="deltaPhi_12",
    call="quantities::deltaPhi({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2],
    output=[q.deltaPhi_12],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaPhi_13 = Producer(
    name="deltaPhi_13",
    call="quantities::deltaPhi({df}, {output}, {input})",
    input=[q.p4_1, q.p4_3],
    output=[q.deltaPhi_13],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
deltaPhi_WH = Producer(
    name="deltaPhi_WH",
    call="quantities::deltaPhi_WH({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.p4_3],
    output=[q.deltaPhi_WH],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
eta_vis = Producer(
    name="eta_vis",
    call="quantities::eta({df}, {output}, {input_vec})",
    input=[q.p4_23],
    output=[q.eta_vis],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
phi_vis = Producer(
    name="phi_vis",
    call="quantities::phi({df}, {output}, {input_vec})",
    input=[q.p4_23],
    output=[q.phi_vis],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
Lt = Producer(
    name="Lt",
    call="quantities::scalarPtSum({df}, {output}, {input})",
    input=[q.pt_1, q.pt_2, q.pt_3],
    output=[q.Lt],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)

####################
# Set of channel specific producers
####################
muon_dxy_wh_1 = Producer(
    name="muon_dxy_wh_1",
    call="quantities::dxy({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dxy],
    output=[q.dxy_1],
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
)
muon_dxy_wh_2 = Producer(
    name="muon_dxy_wh_2",
    call="quantities::dxy({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dxy],
    output=[q.dxy_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_dxy_wh_3 = Producer(
    name="muon_dxy_wh_3",
    call="quantities::dxy({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dxy],
    output=[q.dxy_3],
    scopes=["wh_mmm"],
)
muon_is_mediumid_1 = Producer(
    name="muon_is_mediumid_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_id_medium],
    output=[q.muon_is_mediumid_1],
    scopes=["met", "mmt", "wh_mme", "wh_mmm", "mtt"],
)
muon_is_mediumid_2 = Producer(
    name="muon_is_mediumid_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_id_medium],
    output=[q.muon_is_mediumid_2],
    scopes=["mmt", "wh_mme", "wh_mmm", "emt"],
)
muon_is_mediumid_3 = Producer(
    name="muon_is_mediumid_3",
    call="quantities::muon::id({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_id_medium],
    output=[q.muon_is_mediumid_3],
    scopes=["wh_mmm"],
)
muon_is_tracker_3 = Producer(
    name="muon_is_tracker_3",
    call="quantities::muon::is_tracker({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isTracker],
    output=[q.muon_is_tracker_3],
    scopes=["wh_mmm"],
)
muon_is_global_wh_2 = Producer(
    name="muon_is_global_wh_2",
    call="quantities::muon::is_global({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_is_global_wh_1 = Producer(
    name="muon_is_global_wh_1",
    call="quantities::muon::is_global({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_1],
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
)
muon_is_global_wh_2 = Producer(
    name="muon_is_global_wh_2",
    call="quantities::muon::is_global({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_is_global_wh_3 = Producer(
    name="muon_is_global_wh_3",
    call="quantities::muon::is_global({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_3],
    scopes=["wh_mmm"],
)

electron_dxy_wh_1 = Producer(
    name="electron_dxy_1",
    call="quantities::dxy({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dxy],
    output=[q.dxy_1],
    scopes=["emt", "ett", "eem"],
)
electron_dxy_wh_2 = Producer(
    name="electron_dxy_2",
    call="quantities::dxy({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dxy],
    output=[q.dxy_2],
    scopes=["met", "eem"],
)
electron_dxy_wh_3 = Producer(
    name="electron_dxy_3",
    call="quantities::dxy({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dxy],
    output=[q.dxy_3],
    scopes=["wh_mme", "wh_mmm"],
)
electron_is_nonisowp90_1 = Producer(
    name="electron_is_nonisowp90_1",
    call="quantities::electron::id({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_IDWP90],
    output=[q.electron_is_nonisowp90_1],
    scopes=["emt", "eem", "ett"],
)
electron_is_nonisowp90_2 = Producer(
    name="electron_is_nonisowp90_2",
    call="quantities::electron::id({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_IDWP90],
    output=[q.electron_is_nonisowp90_2],
    scopes=["met", "eem"],
)
electron_is_nonisowp90_3 = Producer(
    name="electron_is_nonisowp90_3",
    call="quantities::electron::id({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Electron_IDWP90],
    output=[q.electron_is_nonisowp90_3],
    scopes=["wh_mme", "wh_mmm"],
)
tau_dxy_2 = Producer(
    name="tau_dxy_2",
    call="quantities::dxy({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dxy],
    output=[q.dxy_2],
    scopes=["ett", "mtt"],
)
tau_dxy_3 = Producer(
    name="tau_dxy_3",
    call="quantities::dxy({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dxy],
    output=[q.dxy_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
muon_dz_wh_1 = Producer(
    name="muon_dz_wh_1",
    call="quantities::dz({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dz],
    output=[q.dz_1],
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
)
muon_dz_wh_2 = Producer(
    name="muon_dz_wh_2",
    call="quantities::dz({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dz],
    output=[q.dz_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_dz_wh_3 = Producer(
    name="muon_dz_wh_3",
    call="quantities::dz({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dz],
    output=[q.dz_3],
    scopes=["wh_mmm"],
)
electron_dz_wh_1 = Producer(
    name="electron_dz_wh_1",
    call="quantities::dz({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dz],
    output=[q.dz_1],
    scopes=["emt", "ett", "eem"],
)
electron_dz_wh_2 = Producer(
    name="electron_dz_wh_2",
    call="quantities::dz({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dz],
    output=[q.dz_2],
    scopes=["met", "eem"],
)
electron_dz_wh_3 = Producer(
    name="electron_dz_wh_3",
    call="quantities::dz({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dz],
    output=[q.dz_3],
    scopes=["wh_mme", "wh_mmm"],
)
tau_dz_2 = Producer(
    name="tau_dz_2",
    call="quantities::dz({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dz],
    output=[q.dz_2],
    scopes=["ett", "mtt"],
)
tau_dz_3 = Producer(
    name="tau_dz_3",
    call="quantities::dz({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dz],
    output=[q.dz_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
muon_q_wh_1 = Producer(
    name="muon_q_wh_1",
    call="quantities::charge({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_charge],
    output=[q.q_1],
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
)
muon_q_wh_2 = Producer(
    name="muon_q_wh_2",
    call="quantities::charge({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_charge],
    output=[q.q_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_q_wh_3 = Producer(
    name="muon_q_wh_3",
    call="quantities::charge({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_charge],
    output=[q.q_3],
    scopes=["wh_mmm"],
)
electron_q_wh_1 = Producer(
    name="electron_q_wh_1",
    call="quantities::charge({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_charge],
    output=[q.q_1],
    scopes=["emt", "ett", "eem"],
)
electron_q_wh_2 = Producer(
    name="electron_q_wh_2",
    call="quantities::charge({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_charge],
    output=[q.q_2],
    scopes=["met", "eem"],
)
electron_q_wh_3 = Producer(
    name="electron_q_wh_3",
    call="quantities::charge({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Electron_charge],
    output=[q.q_3],
    scopes=["wh_mme", "wh_mmm"],
)
tau_q_2 = Producer(
    name="tau_q_2",
    call="quantities::charge({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_charge],
    output=[q.q_2],
    scopes=["ett", "mtt"],
)
tau_q_3 = Producer(
    name="tau_q_3",
    call="quantities::charge({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_charge],
    output=[q.q_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
muon_iso_wh_1 = Producer(
    name="muon_iso_wh_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_iso],
    output=[q.iso_1],
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
)
muon_iso_wh_2 = Producer(
    name="muon_iso_wh_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_iso],
    output=[q.iso_2],
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
)
muon_iso_wh_3 = Producer(
    name="muon_iso_wh_3",
    call="quantities::isolation({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Muon_iso],
    output=[q.iso_3],
    scopes=["wh_mmm"],
)
electron_iso_wh_1 = Producer(
    name="electron_iso_wh_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_iso],
    output=[q.iso_1],
    scopes=["emt", "ett", "eem"],
)
electron_iso_wh_2 = Producer(
    name="electron_iso_wh_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_iso],
    output=[q.iso_2],
    scopes=["met", "eem"],
)
electron_iso_wh_3 = Producer(
    name="electron_iso_wh_3",
    call="quantities::isolation({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Electron_iso],
    output=[q.iso_3],
    scopes=["wh_mme", "wh_mmm"],
)
tau_iso_2 = Producer(
    name="tau_iso_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_IDraw],
    output=[q.iso_2],
    scopes=["ett", "mtt"],
)
tau_iso_3 = Producer(
    name="tau_iso_3",
    call="quantities::isolation({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_IDraw],
    output=[q.iso_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
tau_decaymode_2 = Producer(
    name="taudecaymode_2",
    call="quantities::tau::decaymode({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_decayMode],
    output=[q.decaymode_2],
    scopes=["ett", "mtt"],
)
tau_decaymode_3 = Producer(
    name="taudecaymode_3",
    call="quantities::tau::decaymode({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_decayMode],
    output=[q.decaymode_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
tau_gen_match_2 = Producer(
    name="taugen_match_2",
    call="quantities::tau::genmatch({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_genMatch],
    output=[q.tau_gen_match_2],
    scopes=["ett", "mtt"],
)
tau_gen_match_3 = Producer(
    name="taugen_match_3",
    call="quantities::tau::genmatch({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_genMatch],
    output=[q.tau_gen_match_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
taujet_pt_2 = Producer(
    name="taujet_pt_2",
    call="quantities::tau::matching_jet_pt({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Tau_associatedJet, nanoAOD.Jet_pt],
    output=[q.taujet_pt_2],
    scopes=["ett", "mtt"],
)
taujet_pt_3 = Producer(
    name="taujet_pt_3",
    call="quantities::tau::matching_jet_pt({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_associatedJet, nanoAOD.Jet_pt],
    output=[q.taujet_pt_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
VsJetTauIDFlag_2 = ExtendedVectorProducer(
    name="VsJetTauIDFlag_2",
    call="quantities::tau::TauIDFlag({df}, {output}, 1, {input}, {vsjet_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsJet],
    output="tau_2_vsjet_id_outputname",
    scope=["ett", "mtt"],
    vec_config="vsjet_tau_id",
)
VsJetTauIDFlag_3 = ExtendedVectorProducer(
    name="VsJetTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsjet_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsJet],
    output="tau_3_vsjet_id_outputname",
    scope=["emt", "met", "mmt", "ett", "mtt"],
    vec_config="vsjet_tau_id",
)
VsEleTauIDFlag_2 = ExtendedVectorProducer(
    name="VsEleTauIDFlag_2",
    call="quantities::tau::TauIDFlag({df}, {output}, 1, {input}, {vsele_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsEle],
    output="tau_2_vsele_id_outputname",
    scope=["ett", "mtt"],
    vec_config="vsele_tau_id",
)
VsEleTauIDFlag_3 = ExtendedVectorProducer(
    name="VsEleTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsele_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsEle],
    output="tau_3_vsele_id_outputname",
    scope=["emt", "met", "mmt", "ett", "mtt"],
    vec_config="vsele_tau_id",
)
VsMuTauIDFlag_2 = ExtendedVectorProducer(
    name="VsMuTauIDFlag_2",
    call="quantities::tau::TauIDFlag({df}, {output}, 1, {input}, {vsmu_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsMu],
    output="tau_2_vsmu_id_outputname",
    scope=["ett", "mtt"],
    vec_config="vsmu_tau_id",
)
VsMuTauIDFlag_3 = ExtendedVectorProducer(
    name="VsMuTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsmu_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsMu],
    output="tau_3_vsmu_id_outputname",
    scope=["emt", "met", "mmt", "ett", "mtt"],
    vec_config="vsmu_tau_id",
)
UnrollMuLV1 = ProducerGroup(
    name="UnrollMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["met", "mmt", "mtt", "wh_mme", "wh_mmm"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        muon_dxy_wh_1,
        muon_dz_wh_1,
        muon_q_wh_1,
        muon_iso_wh_1,
        muon_is_global_wh_1,
        muon_is_mediumid_1,
    ],
)
UnrollMuLV2 = ProducerGroup(
    name="UnrollMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "mmt", "wh_mme", "wh_mmm"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        muon_dxy_wh_2,
        muon_dz_wh_2,
        muon_q_wh_2,
        muon_iso_wh_2,
        muon_is_global_wh_2,
        muon_is_mediumid_2,
    ],
)
UnrollMuLV3 = ProducerGroup(
    name="UnrollMuLV3",
    call=None,
    input=None,
    output=None,
    scopes=["wh_mmm"],
    subproducers=[
        pt_3,
        eta_3,
        phi_3,
        mass_3,
        muon_dxy_wh_3,
        muon_dz_wh_3,
        muon_q_wh_3,
        muon_iso_wh_3,
        muon_is_global_wh_3,
        muon_is_mediumid_3,
        muon_is_tracker_3,
    ],
)
UnrollElLV1 = ProducerGroup(
    name="UnrollElLV1",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "ett", "eem"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        electron_dxy_wh_1,
        electron_dz_wh_1,
        electron_q_wh_1,
        electron_iso_wh_1,
        electron_is_nonisowp90_1,
    ],
)
UnrollElLV2 = ProducerGroup(
    name="UnrollElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["met", "eem"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        electron_dxy_wh_2,
        electron_dz_wh_2,
        electron_q_wh_2,
        electron_iso_wh_2,
        electron_is_nonisowp90_2,
    ],
)
UnrollElLV3 = ProducerGroup(
    name="UnrollElLV3",
    call=None,
    input=None,
    output=None,
    scopes=["wh_mme", "wh_mmm"],
    subproducers=[
        pt_3,
        eta_3,
        phi_3,
        mass_3,
        electron_dxy_wh_3,
        electron_dz_wh_3,
        electron_q_wh_3,
        electron_iso_wh_3,
        electron_is_nonisowp90_3,
    ],
)
UnrollTauLV2 = ProducerGroup(
    name="UnrollLV2",
    call=None,
    input=None,
    output=None,
    scopes=["ett", "mtt"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        tau_dxy_2,
        tau_dz_2,
        tau_q_2,
        tau_iso_2,
        tau_decaymode_2,
        tau_gen_match_2,
        taujet_pt_2,
        VsJetTauIDFlag_2,
        VsEleTauIDFlag_2,
        VsMuTauIDFlag_2,
    ],
)
UnrollTauLV3 = ProducerGroup(
    name="UnrollLV3",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt", "ett", "mtt"],
    subproducers=[
        pt_3,
        eta_3,
        phi_3,
        mass_3,
        tau_dxy_3,
        tau_dz_3,
        tau_q_3,
        tau_iso_3,
        tau_decaymode_3,
        tau_gen_match_3,
        taujet_pt_3,
        VsJetTauIDFlag_3,
        VsEleTauIDFlag_3,
        VsMuTauIDFlag_3,
    ],
)
#####################
# Producer Groups
#####################
EMTTripleQuantities = ProducerGroup(
    name="EMTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[
        UnrollElLV1,
        UnrollMuLV2,
        UnrollTauLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
METTripleQuantities = ProducerGroup(
    name="METTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[
        UnrollElLV2,
        UnrollMuLV1,
        UnrollTauLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
MMTTripleQuantities = ProducerGroup(
    name="MMTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mmt"],
    subproducers=[
        UnrollMuLV2,
        UnrollMuLV1,
        UnrollTauLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
MTTTripleQuantities = ProducerGroup(
    name="MTTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mtt"],
    subproducers=[
        UnrollMuLV1,
        UnrollTauLV2,
        UnrollTauLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
ETTTripleQuantities = ProducerGroup(
    name="MTTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["ett"],
    subproducers=[
        UnrollElLV1,
        UnrollTauLV2,
        UnrollTauLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
MMETripleQuantities = ProducerGroup(
    name="MMETripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["wh_mme"],
    subproducers=[
        UnrollMuLV1,
        UnrollMuLV2,
        UnrollElLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)

MMMTripleQuantities = ProducerGroup(
    name="MMMTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["wh_mmm"],
    subproducers=[
        UnrollMuLV1,
        UnrollMuLV2,
        UnrollMuLV3,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)

EEMTripleQuantities = ProducerGroup(
    name="EEMTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["eem"],
    subproducers=[
        UnrollMuLV3,
        UnrollElLV1,
        UnrollElLV2,
        p4_23,
        p4_123met,
        p4_23_miss,
        p4_H,
        m_vis,
        m_tt,
        pt_W,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
        pt_123met,
    ],
)
## advanced event quantities (can be caluculated when ditau pair and met and all jets are determined)
## leptons: q.p4_1, q.p4_2
## met: met_p4_recoilcorrected
## jets: good_jet_collection (if only the leading two are needed: q.jet_p4_1, q.jet_p4_2
## bjets: gen_bjet_collection

mt_1 = Producer(
    name="mt_1",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_1, q.met_p4_recoilcorrected],
    output=[q.mt_1],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
mt_2 = Producer(
    name="mt_2",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_2, q.met_p4_recoilcorrected],
    output=[q.mt_2],
    scopes=[
        "emt",
        "met",
        "mmt",
        "ett",
        "mtt",
        "wh_mme", 
		"wh_mmm",
        "eem",
    ],
)
mt_3 = Producer(
    name="mt_3",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_3, q.met_p4_recoilcorrected],
    output=[q.mt_3],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
)
mt = ProducerGroup(
    name="mt",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh_mme", "wh_mmm", "eem"],
    subproducers=[mt_1, mt_2, mt_3],
)
