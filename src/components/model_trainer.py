import os
import sys

from src.logger import logger
from src.exception import CustomException
from src.utils import save_object
from dataclasses import dataclass


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str= os.path.join('artifacts','model.pkl')

    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config= ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logger.info("Splitting training and testing input data")
            train_array = train_array.values
            test_array = test_array.values

            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models= {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "KNeighbors Regressor": KNeighborsRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()

            }

            model_names= []
            r2_scores= []

            for model_name, model in models.items():
                model.fit(X_train, y_train)
                y_pred= model.predict(X_test)
                r2_square= r2_score(y_test, y_pred)
                model_names.append(model_name)
                r2_scores.append(r2_square)
                logger.info(f"{model_name} R2 Score: {r2_square}")

            best_model_index= r2_scores.index(max(r2_scores))
            best_model_name= model_names[best_model_index]
            best_model= models[best_model_name]

            logger.info(f"Best model found: {best_model_name} with R2 Score: {r2_scores[best_model_index]}")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            predicted= best_model.predict(X_test)
            r2_square= r2_score(y_test, predicted)

            return r2_square

        except Exception as e:
            logger.info("Exception occurred at model training")
            raise CustomException(e, sys)