from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer


############################
# Muon ID, ISO SF
# The readout is done via correctionlib
############################

Muon_1_ID_SF_RooWorkspace = Producer(
    name="MuonID_SF_RooWorkspace",
    call='scalefactor::muon::id_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_id_name}", "{muon_sf_id_args}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_1_Iso_SF_RooWorkspace = Producer(
    name="MuonIso_SF_RooWorkspace",
    call='scalefactor::muon::iso_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_iso_name}", "{muon_sf_iso_args}")',
    input=[q.pt_1, q.eta_1, q.iso_1],
    output=[q.iso_wgt_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_1_ID_SF = Producer(
    name="MuonID_SF",
    call='scalefactor::muon::id({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_1_Trg_Effdt = Producer(
    name="MuonTrg_Effdt",
    call='scalefactor::muon::eff({df}, {input}, "{muon_trg_effdt_variation}", {output}, "{muon_trg_eff_file}", "{muon_trg_eff_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.trg_effdt_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_1_Trg_Effmc = Producer(
    name="MuonTrg_Effmc",
    call='scalefactor::muon::eff({df}, {input}, "{muon_trg_effmc_variation}", {output}, "{muon_trg_eff_file}", "{muon_trg_eff_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.trg_effmc_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_1_Iso_SF = Producer(
    name="MuonIso_SF",
    call='scalefactor::muon::iso({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.iso_wgt_mu_1],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_ID_SF_RooWorkspace = Producer(
    name="MuonID_SF_RooWorkspace",
    call='scalefactor::muon::id_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_id_name}", "{muon_sf_id_args}")',
    input=[q.pt_2, q.eta_2],
    output=[q.id_wgt_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_Iso_SF_RooWorkspace = Producer(
    name="MuonIso_SF_RooWorkspace",
    call='scalefactor::muon::iso_rooworkspace({df}, {input}, {output}, "{muon_sf_workspace}", "{muon_sf_iso_name}", "{muon_sf_iso_args}")',
    input=[q.pt_2, q.eta_2, q.iso_2],
    output=[q.iso_wgt_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_ID_SF = Producer(
    name="MuonID_SF",
    call='scalefactor::muon::id({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_id_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.id_wgt_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_Trg_Effdt = Producer(
    name="MuonTrg_Effdt",
    call='scalefactor::muon::eff({df}, {input}, "{muon_trg_effdt_variation}", {output}, "{muon_trg_eff_file}", "{muon_trg_eff_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.trg_effdt_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_Trg_Effmc = Producer(
    name="MuonTrg_Effmc",
    call='scalefactor::muon::eff({df}, {input}, "{muon_trg_effmc_variation}", {output}, "{muon_trg_eff_file}", "{muon_trg_eff_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.trg_effmc_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)
Muon_2_Iso_SF = Producer(
    name="MuonIso_SF",
    call='scalefactor::muon::iso({df}, {input}, "{muon_sf_year_id}", "{muon_sf_varation}", {output}, "{muon_sf_file}", "{muon_iso_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.iso_wgt_mu_2],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)

MuonTrg_SF = Producer(
    name="MuonTrg_SF",
    call='scalefactor::muon::trg_sf({df}, {input}, {output})',
    input=[q.trg_effdt_mu_1, q.trg_effdt_mu_2, q.trg_effmc_mu_1, q.trg_effmc_mu_2],
    output=[q.trg_sf],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)

MuonTrg_Eff = ProducerGroup(
    name="MuonTrg_Eff",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
    subproducers={
	"vbf": [
	    Muon_1_Trg_Effdt,
	    Muon_1_Trg_Effmc,
	    Muon_2_Trg_Effdt,
	    Muon_2_Trg_Effmc,
	],
    "zh": [
	    Muon_1_Trg_Effdt,
	    Muon_1_Trg_Effmc,
	    Muon_2_Trg_Effdt,
	    Muon_2_Trg_Effmc,
	],
    "wh_mme": [
	    Muon_1_Trg_Effdt,
	    Muon_1_Trg_Effmc,
	    Muon_2_Trg_Effdt,
	    Muon_2_Trg_Effmc,
	],
	"wh_mmm": [
        Muon_1_Trg_Effdt,
        Muon_1_Trg_Effmc,
        Muon_2_Trg_Effdt,
        Muon_2_Trg_Effmc,
    ],

    },
)

MuonIDIsoTrg_SF = ProducerGroup(
    name="MuonIDIsoTrg_SF",
    call=None,
    input=None,
    output=None,
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
    subproducers={
        "vbf": [
            Muon_1_ID_SF,
            Muon_1_Iso_SF,
            Muon_2_ID_SF,
            Muon_2_Iso_SF,
        ],
        "zh": [
            Muon_1_ID_SF,
            Muon_1_Iso_SF,
            Muon_2_ID_SF,
            Muon_2_Iso_SF,
        ],
        "wh_mme": [
            Muon_1_ID_SF,
            Muon_1_Iso_SF,
            Muon_2_ID_SF,
            Muon_2_Iso_SF,
        ],
		"wh_mmm": [
            Muon_1_ID_SF,
            Muon_1_Iso_SF,
            Muon_2_ID_SF,
            Muon_2_Iso_SF,
        ],

    },
)
MuonIDIso_SF_RooWorkspace = ProducerGroup(
    name="MuonIDIso_SF_RooWorkspace",
    call=None,
    input=None,
    output=None,
    scopes=["vbf"],
    subproducers={
        "vbf": [
            Muon_1_ID_SF_RooWorkspace,
            Muon_1_Iso_SF_RooWorkspace,
            Muon_2_ID_SF_RooWorkspace,
            Muon_2_Iso_SF_RooWorkspace,
        ],

    },
)

btagging_SF = Producer(
    name="btagging_SF",
    call='scalefactor::jet::btagSF({df}, {input}, "{btag_sf_variation}", {output}, "{btag_sf_file}", "{btag_corr_algo}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["vbf", "zh", "wh_mme", "wh_mmm"],
)

