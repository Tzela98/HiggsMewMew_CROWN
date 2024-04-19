from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, Filter


JetSelectionFilter = Filter(
        name="JetSelectionFlag",
        call="topreco::JetSelectionVbfScope({df}, {min_njets}, {min_nbjets}, {input})",
        input=[
            q.good_jet_collection,
            q.good_bjet_collection,
        ],
        scopes=["vbf", "zh", "wh"],
    subproducers=[],
)


