import random, string


def MatchSlugGenerator(match_name, team_one, team_two, match_date):
    slug = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16))
    return slug


def ContestSlugGenerator(contest_name, contest_category, contest_price, contest_fee):
    slug = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16))
    return slug
