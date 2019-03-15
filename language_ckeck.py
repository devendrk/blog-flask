# import json # development? depends on final db choice
from jobs import jobs # temporary mock up data
from langdetect import detect

"""
EXAMPLES USED
Any way pre screaning : Title should be in English
 Fluent in Swedish or English
 Fluent in French and English
 one ad was in English and no specification on languages
 Fluent in Finnish and English, both written and spoken
 Fluent skills in English
 Fluent English required
 Fluent English is required
 it is a necessity that you master English both written and spoken.
 good communications skills in English.
 Fluency in English is necessary in this position.
 fluency in English is required
 Fluency in written and spoken English and Finnish are required.
 You are fluent in written and oral English.
 Proficient/excellent English language skills
 very good written and spoken English and Finnish;
"""
# endings removed from requirement words to accomodate more forms
requirement_words = ['fluen','skil', 'requir', 'necess', 'communicat','good','spok','writ','profic','excell']
def analyze_single_statement(str):
    """
    This function takes in text (a single sentence by design) and analyzes whether it includes a statement of Finnish being required.
    """
    # finnish_required is False by default. Variable is purely for readability (it could be removed completely from the code)
    finnish_required = False
    str_lower = str.lower()
    # Exclude cases of "F not required", "no fluent F necessary", "other language or F required"
    # <- despite this may provide some degree of errors. This can be re-entered later when we have more data.
    # Hence: Finnish IS mentioned, there is no explicit negation (NO,NOT) or language alternative option list (OR)
    if ('finnish' in str_lower) and (('no' or 'not') not in str_lower) and ('or' not in str_lower):
        for word in requirement_words:
            if word in str_lower:
                finnish_required = True
                return finnish_required
    return finnish_required

def process_text(str):
    """
    This function takes in text (a Title + whole job Description by design) and analyzes whether it includes a statement of Finnish being required.
    """
    # Split by sentences. Statement is usually in a single sentence.
    str_split = str.split('.')
    print(f"Text split in {len(str_split)} pieces divided by period(.)") # dev
    # array = []
    # finnish_required is False by default. Variable is purely for readability (it could be removed completely from the code)
    finnish_required = False
    for line in str_split:
        # discard very short 'sentences' with less than a few elements
        if len(line)>5:
            # array.append(line)
            # line.replace("\n", "")
            language = detect(line)
            print("-Length: ", len(line), "-->", line, " <<<", language) # dev
            # English may not always be detected correctly in short sentences, hence it is enough if text is Not Finnish.
            if language!='fi':
                # A single statement "Finnish is required" is enough
                if analyze_single_statement(line):
                    finnish_required = True
                    return finnish_required
    return finnish_required

# for testing this script from terminal
if __name__ == "__main__":
    for job in jobs:
        finnish_required = process_text(job['title']+'.'+job['description'])
        if finnish_required:
            print(f"Result: {job['title']} requires Finnish")
        else:
            print(f"Result: {job['title']} does not require Finnish")
