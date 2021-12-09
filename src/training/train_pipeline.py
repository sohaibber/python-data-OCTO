import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


from src.constants import AGGREGATOR_MODEL_PATH, DATASET_PATH, CM_PLOT_PATH
from src.models.aggregator_model import AggregatorModel
from src.models.decision_tree_model import DecisionTreeModel
from src.models.logistic_regression_model import LogisticRegressionModel
from src.models.svc_model import SVCModel
from src.models.kneighbors_classifier_model import KNeighborsModel
from src.models.random_forest_model import RandomForestModel
from src.utils import PlotUtils

#2 paths for data
class TrainingPipeline:
    def __init__(self):
        df = pd.read_csv(DATASET_PATH).iloc[:5000,:] # to update with new dataset path
        df.drop('Time', axis=1, inplace=True)

        features = df.drop('Class', axis=1).values
        y = df['Class'].values

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            features,
            y,
            test_size=0.2,
            random_state=0
        )

        self.model = None

    def train(self, serialize: bool = True, model_name: str = 'model.joblib'):
        # dt_model = DecisionTreeModel()
        # svc_model = SVCModel()
        # rfc_model = RandomForestModel()
        # kn_model = KNeighborsModel()
        # lr_model = LogisticRegressionModel()


        models_dict = {'decisiontree': DecisionTreeModel(), 'svc': SVCModel(),'randomforest':RandomForestModel() ,'knn':KNeighborsModel(),'logisticregression':LogisticRegressionModel()}
        # add checkbox  to avoid non existing keys( model names)
        models = model_name.split(',')
        

        self.model = AggregatorModel(models=[models_dict[one_model] for one_model in models])

        self.model.fit(
            self.x_train,
            self.y_train
        )
        
        
        # model_path = str(AGGREGATOR_MODEL_PATH).replace('aggregator_model.joblib', '_'.join(model_name.split(',')) + ".joblib")
        model_path = str(AGGREGATOR_MODEL_PATH)
        if serialize:
            AggregatorModel.save(
                self.model,
                model_path
            )
        
    def get_model_perfomance(self) -> tuple:
        predictions = self.model.predict(self.x_test)
        return accuracy_score(self.y_test, predictions), f1_score(self.y_test, predictions)

    def render_confusion_matrix(self, plot_name: str = 'plot.png'):
        predictions = self.model.predict(self.x_test)
        cm = confusion_matrix(self.y_test, predictions, labels=[0, 1])
        plt.rcParams['figure.figsize'] = (6, 6)

        PlotUtils.plot_confusion_matrix(
            cm,
            classes=['Clear(0)', 'Fraudulent(1)'],
            normalize=False,
            title=plot_name
        )

        plot_path = str(CM_PLOT_PATH).replace('cm_plot.png', plot_name + '.png')
        print(plot_name)
        plt.savefig(plot_path)
        plt.show()


# if __name__ == "__main__":
#     tp = TrainingPipeline()
#     tp.train(serialize=True)
#     print("here")
#     accuracy, f1 = tp.get_model_perfomance()
#     tp.render_confusion_matrix()
#     print("ACCURACY = {}, F1 = {}".format(accuracy, f1))
