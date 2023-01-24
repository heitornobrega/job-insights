from typing import Union, List, Dict
import src.insights.jobs as jobs

# import jobs

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
        try:
            if matches_salary_range(job, salary):
                valid_jobs.append(job)
        except:
            continue
    return valid_jobs
