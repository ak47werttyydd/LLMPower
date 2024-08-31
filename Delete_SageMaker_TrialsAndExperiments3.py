import boto3

# Create a SageMaker client
sagemaker_client = boto3.client('sagemaker')

# List and delete trials
trials = sagemaker_client.list_trials()
for trial_summary in trials['TrialSummaries']:
    trial_name = trial_summary['TrialName']

    # List and disassociate trial components associated with the trial
    trial_components = sagemaker_client.list_trial_components(TrialName=trial_name)
    for trial_component in trial_components['TrialComponentSummaries']:
        trial_component_name = trial_component['TrialComponentName']

        # Disassociate the trial component from the trial
        sagemaker_client.disassociate_trial_component(
            TrialComponentName=trial_component_name,
            TrialName=trial_name
        )

        # Delete the trial component
        sagemaker_client.delete_trial_component(TrialComponentName=trial_component_name)

    # Delete the trial
    sagemaker_client.delete_trial(TrialName=trial_name)

print("Trials and associated trial components deleted successfully.")

# List and delete experiments
experiments = sagemaker_client.list_experiments()
for experiment_summary in experiments['ExperimentSummaries']:
    experiment_name = experiment_summary['ExperimentName']

    # Delete the experiment
    sagemaker_client.delete_experiment(ExperimentName=experiment_name)

print("Experiments deleted successfully.")
