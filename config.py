from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import event as event
from .producers import genparticles as genparticles
from .producers import muons as muons
from .producers import electrons as electrons
from .producers import jets as jets
from .producers import met as met
from .producers import jetselection as jetselection
from .producers import pairquantities as pairquantities
from .producers import pairselection as pairselection
from .producers import triplequantities as triplequantities
from .producers import tripleselection as tripleselection
from .producers import scalefactors as scalefactors
from .producers import triggers as triggers
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import RemoveProducer
from code_generation.systematics import SystematicShift


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):
    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )

    configuration.add_config_parameters(
        "global",
        {
            "PU_reweighting_file": EraModifier(
                {
                    "2016": "data/pileup/Data_Pileup_2016_271036-284044_13TeVMoriond17_23Sep2016ReReco_69p2mbMinBiasXS.root",
                    "2017": "data/pileup/Data_Pileup_2017_294927-306462_13TeVSummer17_PromptReco_69p2mbMinBiasXS.root",
                    "2018": "data/pileup/Data_Pileup_2018_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18.root",
                }
            ),
            "golden_json_file": EraModifier(
                {
                    "2016": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                }
            ),
            "PU_reweighting_hist": "pileup",
            "met_filters": EraModifier(
                {
                    "2016": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                }
            ),
        },
    )

    # muon base selection:
    configuration.add_config_parameters(
        "global",
		{
			"min_muon_pt": 20.0,
			"max_muon_eta": 2.4,
			"max_muon_dxy": 0.02,
			"max_muon_dz": 0.24,
			"muon_id": "Muon_mediumId",
			"muon_iso_cut": 0.25,
			"muon_trg_cut": 1,
		},
	)

	# electron base selection:
    configuration.add_config_parameters(
		"global",
		{
			"min_ele_pt": 20,
			"max_ele_eta": 2.5,
			"max_ele_dxy": 0.045,
            "max_ele_dz": 0.2,
            "max_ele_iso": 0.3,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",
		},
	)

	# jet base selection:
    configuration.add_config_parameters(
		["global", "vbf"],
		{
			"min_jet_pt": 25,
            "max_jet_eta": 4.7,
            "jet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "jet_puid": EraModifier(
                {
                    "2016preVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medum,tight)
                    "2016postVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,meium,tight)
                    "2017": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tiht)
                    "2018": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tiht)
                }
			),
            "jet_puid_max_pt": 50,  # recommended to apply puID only for jets below 50 GeV
            "jet_reapplyJES": False,
            "jet_jes_sources": '{""}',
            "jet_jes_shift": 0,
            "jet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "jet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/jet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/jet_jerc.json.gz"',
                }
            ),
            "jet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"',
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                }
            ),
            "jet_jes_tag_data": '""',
            "jet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"',
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                }
            ),
            "jet_jec_algo": '"AK4PFchs"',
		},
	)
	
	#bjet base selection
    configuration.add_config_parameters(
		"global",
		{
			"min_bjet_pt": 20,
            "max_bjet_eta": EraModifier(
                {
                    "2016preVFP": 2.5,
                    "2016postVFP": 2.5,
                    "2017": 2.5,
                    "2018": 2.5,
                }
            ),
            "btag_cut": EraModifier(  # medium
                {
                    "2016preVFP": 0.2598,  # taken from https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecomendation106XUL16preVFP
                    "2016postVFP": 0.2489,  # taken from https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecmmendation106XUL16postVFP
                    "2017": 0.3040,
                    "2018": 0.2783,
                }
            ),
		},
	)

    #bjet scale factors
    configuration.add_config_parameters(
    scopes,
        {
            "btag_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
                    "2017": "data/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
                    "2018": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
                }
            ),
            "btag_sf_variation": "central",
            "btag_corr_algo": "deepJet_shape",
        },
    )

    
    # vbf scope selection
    configuration.add_config_parameters(
        ["vbf"],
        {
            "muon_index_in_pair": 0,
            "second_muon_index_in_pair": 1,
            "min_muon_pt": 20.0,
            "max_muon_eta": 2.4,
			"max_muon_dxy": 0.02,
			"max_muon_dz": 0.24,
			"muon_id": "Muon_mediumId",
			"muon_iso_cut": 0.25,
			"muon_trg_cut": 1,
            "min_njets": 2,
            "min_nbjets": 0,
        },
    )
	
	# WH scope selection
    configuration.add_config_parameters(
        ["wh_mme"],
        {
            "muon_index_in_triple": 0,
            "second_muon_index_in_triple": 1,
            "electron_index_in_triple": 2,
            "min_muon_pt": 26.0,
            "max_muon_eta": 2.4,
			"muon_id": "Muon_mediumId",
			"ele_id": "Electron_mvaFall17V2noIso_WP90",
            "muon_iso_cut": 0.25,
			"muon_trg_cut": 1,
            "min_njets": 0,
            "min_nbjets": 0,
            "min_ele_pt": 20,
			"max_ele_eta": 2.5,
            "max_ele_iso": 0.3,
            "p4_23_miss_sf": 0.69,
        },
    )

    configuration.add_config_parameters(
        ["wh_mmm"],
        {
            "muon_index_in_triple": 0,
            "second_muon_index_in_triple": 1,
            "third_muon_index_in_triple": 2,
            "min_muon_pt": 26.0,
            "max_muon_eta": 2.4,
			"muon_id": "Muon_mediumId",
            "muon_iso_cut": 0.25,
			"muon_trg_cut": 1,
            "min_njets": 0,
            "min_nbjets": 0,
            "p4_23_miss_sf": 0.69,
        },
    )

	# ZH scope selection
    configuration.add_config_parameters(
		["zh"],
		{
			"muon_index_in_pair": 0,
            "second_muon_index_in_pair": 1,
            "min_muon_pt": 26.0,
            "max_muon_eta": 2.4,
			"max_muon_dxy": 0.02,
			"max_muon_dz": 0.24,
			"muon_id": "Muon_mediumId",
			"muon_iso_cut": 0.25,
			"muon_trg_cut": 1,
            "min_njets": 2,
            "min_nbjets": 0,
            "min_ele_pt": 20,
			"max_ele_eta": 2.5,
			"max_ele_dxy": 0.045,
            "max_ele_dz": 0.2,
            "max_ele_iso": 0.3,
            "ele_id": "Electron_mvaFall17V2noIso_WP90",

		},
	)

    configuration.add_config_parameters(
        scopes,
        {
            "propagateLeptons": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "propagateJets": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "recoil_corrections_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2016postVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2017": "data/recoil_corrections/Type1_PuppiMET_2017.root",
                    "2018": "data/recoil_corrections/Type1_PuppiMET_2018.root",
                }
            ),
            "recoil_systematics_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/PuppiMETSys_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2016postVFP": "data/recoil_corrections/PuppiMETSys_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2017": "data/recoil_corrections/PuppiMETSys_2017.root",
                    "2018": "data/recoil_corrections/PuppiMETSys_2018.root",
                }
            ),
            "applyRecoilCorrections": SampleModifier(
                {
                    "wjets": True,
                    "dyjets": True,
                    "electroweak_boson": True,
                    "ggh_htautau": True,
                    "vbf_htautau": True,
                    "rem_htautau": True,
                    "ggh_hww": True,
                    "vbf_hww": True,
                    "rem_VH": True,
                },
                default=False,
            ),
            "apply_recoil_resolution_systematic": False,
            "apply_recoil_response_systematic": False,
            "recoil_systematic_shift_up": False,
            "recoil_systematic_shift_down": False,
            "min_jetpt_met_propagation": 15,
        },
    )

    # Muon scale factors configuration
    configuration.add_config_parameters(
        scopes,
        {
            "muon_sf_file": EraModifier(
                {
                    "2016": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                }
            ),
            "muon_id_sf_name": "NUM_MediumID_DEN_TrackerMuons",
            "muon_iso_sf_name": "NUM_TightRelIso_DEN_MediumID",
            "muon_sf_year_id": EraModifier(
                {
                    "2016": "2016postVFP_UL",
                    "2017": "2017_UL",
                    "2018": "2018_UL",
                }
            ),
            "muon_sf_varation": "sf",  # "sf" is nominal, "systup"/"systdown" are up/down variations
        },
    )

    # muon trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        scopes,
        {
            "muon_trg_sf_file": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z_trigger_schemaV2_sf.json",
            "muon_trg_sf_name": "NUM_IsoMu24_DEN_LooseRelIso_and_MediumID",
			"muon_sf_trg_variation": "nominal",
            "muon_trg_eff_file": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z_trigger_schemaV2_eff.json",
            "muon_trg_eff_name": "NUM_IsoMu24_DEN_LooseRelIso_and_MediumID",
            "muon_trg_effdt_variation": "dteff",
            "muon_trg_effmc_variation": "mceff",
            "muon_sf_year_id": EraModifier(
                {
                    "2016": "2016postVFP_UL",
                    "2017": "2017_UL",
                    "2018": "2018_UL",
                }
            ),
            "singlemuon_trigger": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
					],
				}
			),

        },
    )


    ## all scopes misc settings
    configuration.add_config_parameters(
        scopes,
        {
            "deltaR_jet_veto": 0.5,
            "pairselection_min_dR": 0.5,
            "tripleselection_min_dR_lep1lep1": 0.5,
            "tripleselection_min_dR_lep1lep2": 0.5,
        },
    )

    configuration.add_producers(
        "global",
        [
            event.SampleFlags,
            event.PUweights,
            event.Lumi,
			event.npartons,
            event.MetFilter,
            muons.BaseMuons,
			electrons.BaseElectrons,
            electrons.RenameElectronPt,
            jets.JetEnergyCorrection,
            jets.JetPtCorrection_data,
            #jets.JetMassCorrection,
			jets.GoodJets,
			jets.GoodBJets,
            met.MetBasics,
        ],
    )

    
    configuration.add_producers(
        "vbf",
        [
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            pairselection.MMPairSelection,
            pairselection.GoodMMPairFilter,
            pairselection.LVMu1,
            pairselection.LVMu2,
			pairquantities.MuMuPairQuantities,
			pairquantities.pt_dijet,
            genparticles.MMGenDiTauPairQuantities,
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            scalefactors.MuonIDIsoTrg_SF,
            scalefactors.MuonTrg_Eff,
            scalefactors.MuonTrg_SF,
            jetselection.JetSelectionFilter,
			triggers.MuMuGenerateSingleMuonTriggerFlags,
        ],
    )

    configuration.add_producers(
		"wh_mme",
		[
			muons.GoodMuons,
            muons.NumberOfGoodMuons,
            genparticles.GenMatching,
            genparticles.MMEGenTripleQuantities,
            electrons.NumberOfGoodElectrons,
            electrons.GoodElectrons,
            met.MetCorrections,
            met.PFMetCorrections,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.MMETripleSelection,
            tripleselection.LVMu2,
            tripleselection.LVMu1,
            tripleselection.LVEl3,
            tripleselection.LVEl3Uncorrected,
            tripleselection.LVMu2Uncorrected,
            tripleselection.LVMu1Uncorrected,
            triplequantities.MMETripleQuantities,
            triplequantities.UnrollHLV,
            scalefactors.MuonIDIsoTrg_SF,
            scalefactors.MuonTrg_Eff,
            scalefactors.MuonTrg_SF,
			triggers.MuMuGenerateSingleMuonTriggerFlags,
		],
	)

    configuration.add_producers(
		"wh_mmm",
		[
			muons.GoodMuons,
            muons.NumberOfGoodMuons,
            genparticles.GenMatching,
            genparticles.MMMGenTripleQuantities,
            met.MetCorrections,
            met.PFMetCorrections,
            triplequantities.mt,
            tripleselection.GoodTripleFilter,
            tripleselection.MMMTripleSelection,
            tripleselection.LVMu1,
            tripleselection.LVMu2,
            tripleselection.LVMu3,
            tripleselection.LVMu1Uncorrected,
            tripleselection.LVMu2Uncorrected,
            tripleselection.LVMu3Uncorrected,
            triplequantities.UnrollHLV,
            triplequantities.MMMTripleQuantities,
            scalefactors.MuonIDIsoTrg_SF,
            scalefactors.MuonTrg_Eff,
            scalefactors.MuonTrg_SF,
			triggers.MuMuGenerateSingleMuonTriggerFlags,
		],
	)

    configuration.add_producers(
        "zh",
        [
            electrons.NumberOfGoodElectrons,
            electrons.GoodElectrons,
            muons.NumberOfGoodMuons,
            muons.GoodMuons,
            pairselection.MMPairSelection,
            pairselection.GoodMMPairFilter,
            pairselection.ZEEPairselection,
            pairselection.GoodEEPairFilter,
            pairselection.LVMu1,
            pairselection.LVMu2,
            pairselection.LVEl1,
            pairselection.LVEl2,
            pairquantities.MuMuPairQuantities,
            pairquantities.ElElPairQuantities,
            genparticles.MMGenDiTauPairQuantities,
            scalefactors.MuonIDIsoTrg_SF,
            scalefactors.MuonTrg_Eff,
            scalefactors.MuonTrg_SF,
			triggers.MuMuGenerateSingleMuonTriggerFlags,
        ],
    )

    # Add prefiring for eras != 2018
    if era != "2018":
        configuration.add_producers(
            "global",
            [
                event.PrefireWeight,
            ],
        )

    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[
                event.PUweights,
                event.npartons,
                jets.JetEnergyCorrection,
            ],
            samples=["data"],
        ),
    )

    configuration.add_modification_rule(
        ["vbf"],
        RemoveProducer(
            producers=[
                genparticles.MMGenDiTauPairQuantities,
                scalefactors.MuonIDIsoTrg_SF,
				scalefactors.MuonTrg_Eff,
				scalefactors.MuonTrg_SF,
            ],
            samples=["data"],
        ),
    )

    configuration.add_modification_rule(
        ["global"],
        RemoveProducer(
            producers=[
                jets.JetPtCorrection_data,
            ],
            samples=["signal", "dyjets", "ttbar", "diboson", "electroweak_boson", "singletop", "triboson", "wh", "zh"],
        ),
    )

    configuration.add_modification_rule(
        ["wh_mme"],
        RemoveProducer(
            producers=[
                genparticles.MMEGenTripleQuantities,
                genparticles.GenMatching,
                scalefactors.MuonIDIsoTrg_SF,
				scalefactors.MuonTrg_Eff,
				scalefactors.MuonTrg_SF,
            ],
            samples="data",
        ),
    )

    configuration.add_modification_rule(
        ["wh_mmm"],
        RemoveProducer(
            producers=[
                genparticles.MMMGenTripleQuantities,
                genparticles.GenMatching,
                scalefactors.MuonIDIsoTrg_SF,
				scalefactors.MuonTrg_Eff,
				scalefactors.MuonTrg_SF,
            ],
            samples="data",
        ),
    )

    configuration.add_modification_rule(
        ["zh"],
        RemoveProducer(
            producers=[
                genparticles.MMGenDiTauPairQuantities,
                scalefactors.MuonIDIsoTrg_SF,
				scalefactors.MuonTrg_Eff,
				scalefactors.MuonTrg_SF,
            ],
            samples=["data"],
        ),
    )

    
    configuration.add_outputs(
        "vbf",
        [
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_diboson,
            q.is_triboson,
            q.is_wh,
            q.is_zh,
            nanoAOD.run,
            q.lumi,
			q.npartons,
            nanoAOD.event,
            q.puweight,
            q.pt_1,
            q.pt_2,
            q.eta_1,
            q.eta_2,
            q.phi_1,
            q.phi_2,
            q.m_vis,
			q.pt_vis,
            q.njets,
			q.nmuons,
            q.jpt_1,
            q.jpt_2,
            q.jeta_1,
            q.jeta_2,
            q.jphi_1,
            q.jphi_2,
            q.jtag_value_1,
            q.jtag_value_2,
            q.mjj, 
			q.pt_dijet,          
            q.nbtag,
            q.bpt_1,
            q.bpt_2,
            q.beta_1,
            q.beta_2,
            q.bphi_1,
            q.bphi_2,
            q.btag_value_1,
            q.btag_value_2,
			q.btag_weight,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_m_vis,
            q.id_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_1,
            q.iso_wgt_mu_2,
			q.trg_effdt_mu_1,
			q.trg_effdt_mu_2,
			q.trg_effmc_mu_1,
			q.trg_effmc_mu_2,
            q.trg_sf,
			triggers.MuMuGenerateSingleMuonTriggerFlags.output_group,
        ],
    )
	
	# outputs for wh scope
    configuration.add_outputs(
		"wh_mme",
		[
			q.nelectrons,
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_diboson,
            q.is_triboson,
            q.is_wh,
            q.is_zh,
            nanoAOD.run,
            q.lumi,
			q.npartons,
            nanoAOD.event,
            q.puweight,
            q.pt_1,
            q.pt_2,
            q.pt_3,
            q.eta_1,
            q.eta_2,
            q.eta_3,
            q.phi_1,
            q.phi_2,
            q.phi_3,
            q.mass_1,
            q.mass_2,
            q.mass_3,
            q.q_1,
            q.q_2,
            q.q_3,
            q.pt_H,
            q.eta_H,
            q.phi_H,
            q.m_H,
            q.met,
            q.metphi,
            q.pfmet,
            q.pfmetphi,
            q.metSumEt,
            q.pt_W,
            q.Lt,
            q.deltaR_12,
            q.deltaR_13,
            q.deltaR_23,
            q.deltaPhi_12,
            q.deltaPhi_13,
            q.deltaPhi_WH,
            q.deltaEta_13,
            q.deltaEta_23,
            q.deltaEta_WH,
            q.pt_123met,
			q.nmuons,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_pt_3,
            q.gen_eta_3,
            q.gen_phi_3,
            q.gen_mass_3,
            q.gen_pdgid_3,
            q.gen_m_vis,
            q.id_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_1,
            q.iso_wgt_mu_2,
			q.trg_effdt_mu_1,
			q.trg_effdt_mu_2,
			q.trg_effmc_mu_1,
			q.trg_effmc_mu_2,
            q.trg_sf,
			triggers.MuMuGenerateSingleMuonTriggerFlags.output_group,
		],
	)

    configuration.add_outputs(
		"wh_mmm",
		[
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_diboson,
            q.is_triboson,
            q.is_wh,
            q.is_zh,
            nanoAOD.run,
            q.lumi,
			q.npartons,
            nanoAOD.event,
            q.puweight,
            q.pt_1,
            q.pt_2,
            q.pt_3,
            q.eta_1,
            q.eta_2,
            q.eta_3,
            q.phi_1,
            q.phi_2,
            q.phi_3,
            q.mass_1,
            q.mass_2,
            q.mass_3,
            q.q_1,
            q.q_2,
            q.q_3,
            q.pt_H,
            q.eta_H,
            q.phi_H,
            q.m_H,
            q.met,
            q.metphi,
            q.pfmet,
            q.pfmetphi,
            q.metSumEt,
            q.pt_W,
            q.Lt,
            q.deltaR_12,
            q.deltaR_13,
            q.deltaR_23,
            q.deltaPhi_12,
            q.deltaPhi_13,
            q.deltaPhi_WH,
            q.deltaEta_13,
            q.deltaEta_23,
            q.deltaEta_WH,
            q.pt_123met,
			q.nmuons,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_pt_3,
            q.gen_eta_3,
            q.gen_phi_3,
            q.gen_mass_3,
            q.gen_pdgid_3,
            q.gen_m_vis,
            q.id_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_1,
            q.iso_wgt_mu_2,
			q.trg_effdt_mu_1,
			q.trg_effdt_mu_2,
			q.trg_effmc_mu_1,
			q.trg_effmc_mu_2,
            q.trg_sf,
			triggers.MuMuGenerateSingleMuonTriggerFlags.output_group,
		],
	)

    # outputs for zh scope
    configuration.add_outputs(
        "zh",
        [
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_diboson,
            nanoAOD.run,
            q.lumi,
			q.npartons,
            nanoAOD.event,
            q.puweight,
            q.pt_1,
            q.pt_2,
            q.eta_1,
            q.eta_2,
            q.phi_1,
            q.phi_2,
            q.m_vis,
			q.pt_vis,
			q.nmuons,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_m_vis,
            q.id_wgt_mu_1,
            q.id_wgt_mu_2,
            q.iso_wgt_mu_1,
            q.iso_wgt_mu_2,
			q.trg_effdt_mu_1,
			q.trg_effdt_mu_2,
			q.trg_effmc_mu_1,
			q.trg_effmc_mu_2,
            q.trg_sf,
            q.nelectrons,
            q.ele_pt_1,
            q.ele_pt_2,
            q.ele_eta_1,
            q.ele_eta_2,
            q.ele_phi_1,
            q.ele_phi_2,
            q.ele_m_vis,
            q.ele_pt_vis,
            q.ele_iso_1,
            q.ele_iso_2,
            q.ele_q_1,
            q.ele_q_2,
			triggers.MuMuGenerateSingleMuonTriggerFlags.output_group,
        ],
    )


    # add genWeight for everything but data
    if sample != "data":
        configuration.add_outputs(
            scopes,
            nanoAOD.genWeight,
        )
        if era != "2018":
            configuration.add_outputs(
                scopes,
                q.prefireweight,
            )



    '''
    configuration.add_shift(
        SystematicShift(
            name="MuonIDUp",
            shift_config={"mm": {"muon_sf_varation": "systup"}},
            producers={
                "mm": [
                    scalefactors.Muon_1_ID_SF,
                    scalefactors.Muon_2_ID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIDDown",
            shift_config={"mm": {"muon_sf_varation": "systdown"}},
            producers={
                "mm": [
                    scalefactors.Muon_1_ID_SF,
                    scalefactors.Muon_2_ID_SF,
                ]
            },
        )
    )
    '''

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
