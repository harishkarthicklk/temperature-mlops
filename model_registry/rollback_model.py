import shutil

CURRENT_MODEL = "pkl_file/current_model.pkl"

PREVIOUS_MODEL = "pkl_file/backup/current_model_backup.pkl"

shutil.copy(
    PREVIOUS_MODEL,
    CURRENT_MODEL
)

print("Rollback Successful")