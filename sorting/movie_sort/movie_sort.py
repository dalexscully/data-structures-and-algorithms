movies = [
  {
    "title": "Beetlejuice",
    "year": 1988,
    "genres": ["Comedy", "Fantasy"],
  },
  {
    "title": "The Cotton Club",
    "year": 1984,
    "genres": ["Crime", "Drama", "Music"],
  },
  {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Crocodile Dundee",
    "year": 1986,
    "genres": ["Adventure", "Comedy"],
  },
  {
    "title": "Valkyrie",
    "year": 2008,
    "genres": ["Drama", "History", "Thriller"],
  },
  {
    "title": "Ratatouille",
    "year": 2007,
    "genres": ["Animation", "Comedy", "Family"],
  },
  {
    "title": "City of God",
    "year": 2002,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Memento",
    "year": 2000,
    "genres": ["Mystery", "Thriller"],
  },
  {
    "title": "The Intouchables",
    "year": 2011,
    "genres": ["Biography", "Comedy", "Drama"],
  },
  {
    "title": "Stardust",
    "year": 2007,
    "genres": ["Adventure", "Family", "Fantasy"],
  },
]


def year_sort(lst):
    return [movie['title'] for movie in merge_year_sort(lst)]


def merge_year_sort(movie_list):
    n = len(movie_list)

    if n > 1:
        mid = n//2
        left = movie_list[:mid]
        right = movie_list[mid:]

        merge_year_sort(left)
        merge_year_sort(right)
        year_merge(left, right, movie_list)

    return movie_list


def year_merge(left, right, movie_list):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i]['year'] < right[j]['year']:
            movie_list[k] = right[j]
            j += 1
        else:
            movie_list[k] = left[i]
            i += 1
        k += 1

    if i == len(left):
        for idx in range(j, len(right)):
            movie_list[k] = right[idx]
            k += 1

    else:
        for idx in range(i, len(left)):
            movie_list[k] = left[idx]
            k += 1


def title_sort(lst):
    return [movie['title'] for movie in merge_title_sort(lst)]


def merge_title_sort(movie_list):
    n = len(movie_list)

    if n > 1:
        mid = n//2
        left = movie_list[:mid]
        right = movie_list[mid:]

        merge_title_sort(left)
        merge_title_sort(right)
        title_merge(left, right, movie_list)

    return movie_list


def title_merge(left, right, movie_list):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if compare_titles(left[i]['title'], right[j]['title']) > 0:
            movie_list[k] = right[j]
            j += 1
        else:
            movie_list[k] = left[i]
            i += 1
        k += 1

    if i == len(left):
        for idx in range(j, len(right)):
            movie_list[k] = right[idx]
            k += 1

    else:
        for idx in range(i, len(left)):
            movie_list[k] = left[idx]
            k += 1


def compare_titles(title1, title2):
    if title1.lower() == title2.lower():
        return 0

    title1 = strip_title_prefix(title1)
    title2 = strip_title_prefix(title2)

    i = j = 0

    while i < len(title1) and j < len(title2):
        if ord(title1[i].lower()) < ord(title2[i].lower()):
            return -1

        elif ord(title1[i].lower()) > ord(title2[i].lower()):
            return 1

        else:
            i += 1
            j += 1

    if i == len(title1):
        return -1
    else:
        return 1


def strip_title_prefix(title):
    if title[0:3] == 'An ':
        return title[3:]
    elif title [0:2] == 'A':
        return title[2:]
    elif title [0:4] == 'The ':
        return title[4:]
    else:
        return title


if __name__ == "__main__":
    print(year_sort(movies))
    print(title_sort(movies))

