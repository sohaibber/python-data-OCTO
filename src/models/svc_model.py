from sklearn.svm import SVC

from src.models.base_model import BaseModel


class SVCModel(BaseModel):
    def __init__(self, kernel:str = "linear", gamma:str="scale", C:float=1.0):
        self.kernel = kernel
        self.gamma = gamma
        self.C = C
        
        super().__init__(
            model=SVC(kernel=self.kernel, C = self.C, gamma = self.gamma)
        )