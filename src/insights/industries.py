from typing import List, Dict
import src.insights.jobs as jobs

# import jobs


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # raise NotImplementedError
    data = jobs.read(path)
    unique_industries = set()
    for industry in data:
        if len(industry["industry"]) > 0:
            unique_industries.add(industry["industry"])

    return list(unique_industries)


print(get_unique_industries("data/jobs.csv"))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
