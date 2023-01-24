from typing import Union, List, Dict
import src.insights.jobs as jobs
# import jobs

dict_test = {'job_title': 'Data Engineer, Senior with Security Clearance', 'company': 'Booz Allen Hamilton', 'state': 'VA', 'city': 'Herndon', 'min_salary': '91443', 'max_salary': '155868', 'job_desc': "Job Number: R0083334 Data Engineer, Senior\n\nKey Role: Develop data pipelines us ing Big Data services available in the Cloud. Architect data repositories, stand up data platforms, and write c us tom code for data ingestion, transformation, and aggregation. Create data models to support b us iness requirements. Work as a client-facing consultant providing solutions to Big Data us e cases. Develop continuo us integration ( CI ) and continuo us delivery ( CD ) pipelines to support automated deployment and automated testing. Basic Qualifications: -6+ years of experience with a modern programming language, including Python or Java -4+ years of experience with working in an agile development environment -4+ years of experience with developing extract, transform, load ( ETL ) and data pipelines -3+ years of experience with SQL -2+ years of experience with working in a Big Data environment -Ability to learn te chn ical concepts -Secret clearance -BA or BS degree Additional Qualifications: -Experience with Cloudera or Hortonworks -Experience with Hadoop ecosystem -Experience with data modeling concepts -Experience with leading a te chn ical team -Possession of excellent analytical and problem-solving skills -Possession of excellent oral and written communication skills, including communicating with multiple functional groups Clearance: Applicants selected will be subject to a security investigation and may need to meet eligibility requirements for access to classified information; Secret clearance is required. We're an EOE that empowers our people-no matter their race, color, religion, sex, gender identity, sexual orientation, national origin, disability, veteran status, or other protected characteristic-to fearlessly drive change.", 'industry': 'Business Services', 'rating': '3.7', 'date_posted': '2020-05-02', 'valid_until': '2020-06-06', 'job_type': 'FULL_TIME', 'id': '3323'}

def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    data = jobs.read(path)
    all_max_salaries = set()
    for max_salary in data:
        if (
            len(max_salary["max_salary"]) > 0
            and max_salary["max_salary"] != "invalid"
        ):
            teste = int(max_salary["max_salary"])
            all_max_salaries.add(teste)

    max_salary = max(list(all_max_salaries))
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    data = jobs.read(path)
    all_min_salaries = set()
    for min_salary in data:
        if (
            len(min_salary["min_salary"]) > 0
            and min_salary["min_salary"] != "invalid"
        ):
            teste = int(min_salary["min_salary"])
            all_min_salaries.add(teste)

    min_salary = min(list(all_min_salaries))
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # raise NotImplementedError
    try:
        int_salary = int(salary)
        int_job_min_salary = int(job["min_salary"])
        int_job_max_salary = int(job["max_salary"])
    except:
        raise ValueError
    if int_job_min_salary > int_job_max_salary:
        raise ValueError
    if int_salary < int_job_min_salary or int_salary > int_job_max_salary:
        return False
    else:
        return True



def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # raise NotImplementedError
    valid_jobs = []
    for job in jobs:
        if(matches_salary_range(job, salary)):
            valid_jobs.append(job)
    return valid_jobs

            
        
