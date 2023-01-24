from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    # Crie uma lista de empregos para testar
    jobs = [
        {
            "name": "Job 1",
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2022-01-01",
        },
        {
            "name": "Job 2",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-01-03",
        },
        {
            "name": "Job 3",
            "min_salary": 800,
            "max_salary": 1800,
            "date_posted": "2022-01-02",
        },
        {
            "name": "Job 4",
            "min_salary": None,
            "max_salary": 1200,
            "date_posted": "2022-01-04",
        },
    ]

    sort_by(jobs, "min_salary")

    assert jobs == [
        {
            "name": "Job 2",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-01-03",
        },
        {
            "name": "Job 3",
            "min_salary": 800,
            "max_salary": 1800,
            "date_posted": "2022-01-02",
        },
        {
            "name": "Job 1",
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2022-01-01",
        },
        {
            "name": "Job 4",
            "min_salary": None,
            "max_salary": 1200,
            "date_posted": "2022-01-04",
        },
    ]

    sort_by(jobs, "max_salary")

    assert jobs == [
        {
            "name": "Job 1",
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2022-01-01",
        },
        {
            "name": "Job 3",
            "min_salary": 800,
            "max_salary": 1800,
            "date_posted": "2022-01-02",
        },
        {
            "name": "Job 2",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-01-03",
        },
        {
            "name": "Job 4",
            "min_salary": None,
            "max_salary": 1200,
            "date_posted": "2022-01-04",
        },
    ]
