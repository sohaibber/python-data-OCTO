import streamlit as st
from PIL import Image
import time
from src.constants import CM_PLOT_PATH
from src.training.train_pipeline import TrainingPipeline

def Training():
        st.header("Model Training")
        # st.info("Before you proceed to training your model. Make sure you "
        #         "have checked your training pipeline code and that it is set properly.")

        #name = st.text_input('Model name', placeholder='decisiontree')

        selected_models = st.multiselect('Model name',
                                  ['decisiontree', 'svc', 'randomforest','knn','logisticregression'])

        model_names=','.join(selected_models)
        st.write(model_names)
        serialize = st.checkbox('Save model')
        train = st.button('Train Model')
        if train:
            if len(selected_models):
                with st.spinner('Training model, please wait...'):
                    time.sleep(1)
                    try:
                        tp = TrainingPipeline()
                        tp.train(serialize=serialize, model_name=model_names)
                        tp.render_confusion_matrix(plot_name=model_names)
                        accuracy, f1 = tp.get_model_perfomance()
                        col1, col2 = st.columns(2)

                        col1.metric(label="Accuracy score", value=str(round(accuracy, 4)))
                        col2.metric(label="F1 score", value=str(round(f1, 4)))
                        cm_plot_path = str(CM_PLOT_PATH).replace('cm_plot.png', model_names+'.png')
                        st.image(Image.open(cm_plot_path))

                    except Exception as e:
                        st.error('Failed to train model!')
                        st.exception(e)
            else:
                st.error("Please select a model")