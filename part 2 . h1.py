
def has_experience_as(cvs,job_title):
    for cv in cvs:
        if job_title in cv['jobs']:
            return cv['user']
        
cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]

has_experience_as(cv_list,'analyst')

##
def job_counts(cvs):
    job_dictionary={}
    for cv in cvs:
        jobs= cv.get('jobs')
        for job in jobs:
            if job in job_dictionary:
                job_dictionary[job] += 1
            else:
                job_dictionary[job] = 1

    return job_dictionary

cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]
job_counts(cv_list)

##

def job_counts(cvs):
    job_dictionary={}
    for cv in cvs:
        jobs= cv.get('jobs')
        for job in jobs:
            if job in job_dictionary:
                job_dictionary[job] += 1
            else:
                job_dictionary[job] = 1

    return job_dictionary

def most_popular_job(cvs):
    job_dictionary=job_counts(cvs)
    most_popular = max(job_dictionary.items(),key=lambda x:x[1])
    return most_popular 

cv_list=[{'user': 'john', 'jobs': ['analyst', 'engineer']},
  {'user': 'jane', 'jobs': ['finance', 'software']},
  {'user': 'dani', 'jobs': ['finance']}]
most_popular_job(cv_list)

