from django import template

import datetime


register = template.Library()


@register.filter
def format_date(value):
    date = datetime.datetime.fromtimestamp(value)
    delta = datetime.datetime.now() - date
    if delta.seconds <= 600:
        return 'только что'
    elif delta.seconds <= 86400:
        return '{} часов назад'.format(delta.seconds // 3600)
    else:
        return date.date()


@register.filter
def format_score(value, param):
    if value < -5:
        return 'все плохо'
    elif value >= -5 and value <= 5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'
    else:
        return param


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif value > 0 and value <= 50:
        return value
    else:
        return '50+'

@register.filter
def format_selftext(value, count):
    splitted_text = value.split(' ')
    first_part = splitted_text[0:count]
    last_part = splitted_text[len(splitted_text) - count:len(splitted_text)]
    first_part.append('...')
    first_part.extend(last_part)
    final_text = ' '.join(first_part)
    return final_text

