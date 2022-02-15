from django.contrib.auth import get_user_model
from django.db.models import Max
from django.shortcuts import get_object_or_404

from problems.models import Submission, Problem
from .models import Contest

User = get_user_model()


def list_problems(contest_id):
    return Contest.objects.get(id=contest_id).problems.all()


def list_users(contest_id):
    return Contest.objects.get(id=contest_id).participants.all()


def list_submissions(contest_id):
    return Submission.objects.filter(problem__contest__id=contest_id).order_by("-submitted_time")


def list_problem_submissions(contest_id, problem_id):
    return Submission.objects.filter(
        problem__id=problem_id, problem__contest__id=contest_id
    ).order_by("-submitted_time")


def list_user_submissions(contest_id, user_id):
    return Submission.objects.filter(
        participant__id=user_id, problem__contest__id=contest_id
    ).order_by("-submitted_time")


def list_problem_user_submissions(contest_id, user_id, problem_id):
    return Submission.objects.filter(
        problem__id=problem_id, participant__id=user_id, problem__contest__id=contest_id
    ).order_by("-submitted_time")


def list_users_solved_problem(contest_id, problem_id):
    pass


def user_score(contest_id, user_id):
    pass


def list_final_submissions(contest_id):
    pass
