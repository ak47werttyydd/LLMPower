import boto3
import sagemaker
from sagemaker.session import Session
sagemaker_session = Session()
# delete trials first
trials = sagemaker_session.list_trials()
for trial in trials:
    sagemaker_session.sagemaker_client.delete_trial(TrialName=trial)
    #delete trial components
    trial_components = sagemaker_session.list_trial_components(TrialName=trial)
    for trial_component in trial_components['TrialComponentSummaries']:
        sagemaker_session.sagemaker_client.delete_trial_component(
            TrialComponentName=trial_component['TrialComponentName']
        )
print("delete trials done")

# List trials
experiments = sagemaker_session.list_experiments()
for experiment in experiments:
    sagemaker_session.sagemaker_client.delete_experiment(ExperimentName=experiment)
print("delete experiments done")