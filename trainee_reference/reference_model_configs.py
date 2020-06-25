from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'trainee_subject.appointment': ['trainee_subject.subjectvisit']})

configs = {
    'trainee_subject.communityquestionnaire': [
        'community_activities', 'election', 'problems',
        'problems_other', 'collaboration'],
    'trainee_subject.educationquestionnaire': [
        'work_status', 'work_type', 'recent_job', 'previous_earning'],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
