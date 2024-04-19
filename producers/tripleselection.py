from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, Filter

####################
# Set of producers used for contruction of MT good pairs and the coressponding lorentz vectors
####################

EMTTripleSelection = Producer(
    name="EMTTripleSelection",
    call="whtautau_tripleselection::elemutau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_leplep})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Tau_charge,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Electron_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_iso,
        nanoAOD.Muon_charge,
        q.good_electrons_mask,
        q.base_electrons_mask,
        q.good_muons_mask,
        q.base_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["emt"],
)
METTripleSelection = Producer(
    name="METTripleSelection",
    call="whtautau_tripleselection::mueletau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_leplep})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Tau_charge,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Electron_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_iso,
        nanoAOD.Muon_charge,
        q.good_electrons_mask,
        q.base_electrons_mask,
        q.good_muons_mask,
        q.base_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["met"],
)
MMTTripleSelection = Producer(
    name="MMTTripleSelection",
    call='whtautau_tripleselection::mumutau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_leplep}, "{ss_or_os}")',
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Tau_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_iso,
        nanoAOD.Muon_charge,
        q.good_muons_mask,
        q.base_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["mmt"],
)
EMTTripleSelectionWOEle = Producer(
    name="EMTTripleSelectionWOEle",
    call="whtautau_tripleselection::elemutau::TripleSelectionWOEle({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_electrons_mask,
        q.good_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["emt"],
)
ETTTripleSelection = Producer(
    name="ETTTripleSelection",
    call="whtautau_tripleselection::ele_tautau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_tautau})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Tau_charge,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_charge,
        q.good_electrons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["ett"],
)
MTTTripleSelection = Producer(
    name="MTTTripleSelection",
    call="whtautau_tripleselection::mu_tautau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_tautau})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Tau_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_charge,
        q.good_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["mtt"],
)
MMETripleSelection = Producer(
    name="MMETripleSelection",
    call="whtautau_tripleselection::mumuele::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_lep1lep1}, {tripleselection_min_dR_lep1lep2})",
    input=[
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_iso,
        nanoAOD.Muon_charge,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Electron_charge,
        q.good_muons_mask,
        q.base_electrons_mask,
    ],
    output=[q.leptontriple],
    scopes=["wh"],
)
EEMTripleSelection = Producer(
    name="EEMTripleSelection",
    call="whtautau_tripleselection::eleelemu::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_lep1lep1}, {tripleselection_min_dR_lep1lep2})",
    input=[
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Electron_charge,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_iso,
        nanoAOD.Muon_charge,
        q.good_electrons_mask,
        q.base_muons_mask,
    ],
    output=[q.leptontriple],
    scopes=["eem"],
)
GoodTripleFlag = Producer(
    name="GoodTripleFlag",
    call="whtautau_tripleselection::flagGoodTriples({df}, {output}, {input})",
    input=[q.leptontriple],
    output=[],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
)

GoodTripleFilter = Filter(
    name="GoodTripleFilter",
    call='basefunctions::FilterFlagsAny({df}, "GoodTriples", {input})',
    input=[],
    scopes=["emt", "met", "mmt", "ett", "mtt", "wh", "eem"],
    subproducers=[GoodTripleFlag],
)
LVMu1 = Producer(
    name="LVMu1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_1],
    scopes=["met", "mmt", "mtt", "wh"],
)
LVMu2 = Producer(
    name="LVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2],
    scopes=["emt", "mmt", "wh"],
)
LVMu3 = Producer(
    name="LVMu3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_3],
    scopes=["eem"],
)
LVEl2 = Producer(
    name="LVEl2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2],
    scopes=["met", "eem"],
)
LVEl1 = Producer(
    name="LVEl1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_1],
    scopes=["emt", "ett", "eem"],
)
LVEl3 = Producer(
    name="LVEl3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_3],
    scopes=["wh"],
)
LVTau2 = Producer(
    name="LVTau2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        q.Tau_mass_corrected,
    ],
    output=[q.p4_2],
    scopes=["ett", "mtt"],
)
LVTau3 = Producer(
    name="LVTau3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        q.Tau_mass_corrected,
    ],
    output=[q.p4_3],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
## uncorrected versions of all particles, used for MET propagation
LVMu1Uncorrected = Producer(
    name="LVMu1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_1_uncorrected],
    scopes=["met", "mmt", "mtt", "wh"],
)
LVMu2Uncorrected = Producer(
    name="LVMu2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["emt", "mmt", "wh"],
)
LVMu3Uncorrected = Producer(
    name="LVMu3Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_3_uncorrected],
    scopes=["eem"],
)
LVEl2Uncorrected = Producer(
    name="LVEl2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["met", "eem"],
)
LVEl1Uncorrected = Producer(
    name="LVEl1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_1_uncorrected],
    scopes=["emt", "ett", "eem"],
)
LVEl3Uncorrected = Producer(
    name="LVEl3Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_3_uncorrected],
    scopes=["wh"],
)
LVTau2Uncorrected = Producer(
    name="LVTau2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_pt,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["ett", "mtt"],
)
LVTau3Uncorrected = Producer(
    name="LVTau3Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_pt,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
    ],
    output=[q.p4_3_uncorrected],
    scopes=["emt", "met", "mmt", "ett", "mtt"],
)
