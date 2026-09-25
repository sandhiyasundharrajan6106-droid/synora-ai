from app.ml.prototype_model import PrototypeScreeningModel


class ScreeningService:
    def __init__(self):
        self.model = PrototypeScreeningModel()

    def analyze(self, feature_vector):
        prediction = self.model.predict(feature_vector)
        return prediction


service = ScreeningService()

def analyze(feature_vector):
    return service.analyze(feature_vector)
