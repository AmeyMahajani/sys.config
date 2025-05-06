def sjf(jobs):
    n = len(jobs)
    completed = []
    time = 0
    jobs.sort(key = lambda x: (x[1], x[2]))

    print(f"{'JOB':<5} {'AT':<5} {'BT':<5} {'CT':<5} {'TAT':<5} {'WT':<5}")

    while len(completed) < n:
        available = [job for job in jobs if job[1]<=time and job not in completed]

        if not available:
            time +=1
            continue

        job = min(available, key=lambda x: x[2])
        job_id, at, bt = job
        ct = time + bt
        tat = ct - at
        wt = tat - bt

        print(f"{job_id:<5} {at:<5} {bt:<5} {ct:<5} {tat:<5} {wt:<5}")

        time = ct
        completed.append(job)


jobs = [
    ('J1', 0, 7),
    ('J2', 2, 4),
    ('J3', 4, 1),
    ('J4', 5, 3)
]

sjf(jobs)
