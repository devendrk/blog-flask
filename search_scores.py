from jobs import jobs

# for testing this script from terminal
query_words = ['AI','ML']

def count_job_search_score(query_words, text):
    """
    Counts a score of a text for list of search words
    """
    score = 0
    for word in query_words:
        # Simple model: a point for each occurrence of every word
        score += text.count(word)
        print(f"Word {word} has been found {score} times") # dev
    return score


def search_sort_jobs(query_words):
    # jobscore is list of lists [job id, job score]
    # this unexisting job with id:-1 is needed for purpose of simplification of the following algorithm
    jobScore = list([[-1,0]])
    for job_index in range(len(jobs)):
        # count a score for each job using title + description
        score = count_job_search_score(query_words, jobs[job_index]['title'] + '.' + jobs[job_index]['description'])
        # scores of 0 are excluded from results completely
        if score > 0:
            # Now for inserting a non-zero result in sorted order linearly. This can be changed to more optimal algorithm later.
            for record_index in range(len(jobScore)):
                # at least 1 record is guaranteed to have 0 score: the beginning record [-1,0]
                # print(jobScore[record_index])
                if jobScore[record_index][1] < score:
                    jobScore.insert(record_index,[job_index,score])
                    break
    return jobScore # return list of lists [job id, job score]. This can be changed to more relevant output later.

# for testing this script from terminal
if __name__ == "__main__":
    print(search_sort_jobs(query_words))
