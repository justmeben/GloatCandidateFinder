from CandidateFinder.models import Skill, Candidate, Job
import random

skills = ['Java', 'C++', 'PowerPoint', 'Python', 'Excel', 'Word', 'Linux', 'Windows', 'Ruby', 'Rust']
titles = ['Software Developer', 'Software Engineer', 'Quality Assurance', 'Human Resources Professional', 'Executive Manager', 'Helpdesk technician',
          'Product', 'Project Manager']


def clean_all_data():
    Job.objects.all().delete()
    Candidate.objects.all().delete()
    Skill.objects.all().delete()


def generate_sample_data():
    db_skills = []
    db_jobs = []

    for skill in skills:
        db_skills.append(Skill(name=skill))

    Skill.objects.bulk_create(db_skills)
    skills_by_name = {x.name: x for x in db_skills}

    while titles:
        title = titles.pop(titles.index(random.choice(titles)))
        db_jobs.append(Job(title=title, skill=skills_by_name[random.choice(skills)]))

        db_candidate = Candidate.objects.create(title=title)
        skills_to_add = random.sample(skills, random.randint(0, 5))
        for skill in skills_to_add:
            db_candidate.skills.add(skills_by_name[skill])

    Job.objects.bulk_create(db_jobs)
