from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, "r") as file:
        with open(path, "r") as file:
            jobs_file = csv.DictReader(file)
            data = list(jobs_file)
    return data

    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    # raise NotImplementedError
    file = read(path)
    set_jobs_type = set()
    for job_type in file:
        set_jobs_type.add(job_type["job_type"])
    return list(set_jobs_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # raise NotImplementedError
    selected_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            selected_jobs.append(job)
    return selected_jobs


# filter_by_job_type(read('data/jobs.csv'), 'TEMPORARY')
