from fastapi import FastAPI
from models import AnalysisInput
from evaluator.space import space_efficiency
from evaluator.privacy import privacy_score
from evaluator.circulation import circulation_score
from evaluator.explanation import generate_explanations

app = FastAPI()

@app.post("/analyze")
def analyze(data: AnalysisInput):

    layout = data.layout
    plot = data.plot

    scores = {
        "space_efficiency": space_efficiency(layout, plot),
        "privacy": privacy_score(layout),
        "circulation": circulation_score(layout)
    }

    explanations = generate_explanations(layout)

    return {
        "scores": scores,
        "explanations": explanations
    }