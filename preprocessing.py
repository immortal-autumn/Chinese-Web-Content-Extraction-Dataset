import json
from pathlib import Path

author = Path('author')
cleaned = Path('cleaned')
date = Path('date')

target = {
    'author': Path('eval/author_ground.json'),
    'date': Path('eval/date_ground.json'),
    'cleaned': Path('eval/cleaned_ground.json')
}


# Produce Ground Truth
def pgt(module):
    res = {}
    for i in module.glob('*'):
        filename = i.name.split('.')[0]
        content = open(i, 'r', encoding='utf-8').read()
        res[filename] = {}
        res[filename]['articleBody'] = content
    return res


def write_gt(name, data):
    with open(target[name], 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


write_gt('author', pgt(author))
write_gt('date', pgt(date))
write_gt('cleaned', pgt(cleaned))
# print(author.__name__)
# with open(f'eval/{name.__name__}', 'w+') as f:
