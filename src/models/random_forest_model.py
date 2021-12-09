from sklearn.ensemble import RandomForestClassifier

from src.models.base_model import BaseModel


class RandomForestModel(BaseModel):
    def __init__(self):
        super().__init__(
            model=RandomForestClassifier()
        )
