import re
character_regex=re.compile('[a-zA-Z]')
def check_diff_characters(user_input):
    extra_characters=character_regex.sub(r'',user_input)
    if len(extra_characters)==0:
        return False
    else:
        return True
