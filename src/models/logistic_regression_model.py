from sklearn.linear_model import LogisticRegression

from src.models.base_model import BaseModel


class LogisticRegressionModel(BaseModel):
    def __init__(self, penalty: str = 'l2' , C: float = 0.01):
         self.penalty = penalty
         self.C = C

         super().__init__(
            model=LogisticRegression(penalty = self.penalty , C= self.C)
         )