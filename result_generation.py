# Performance Evaluation Directory
import statistics
import time

import trafilatura, gzip, json
import matplotlib
from pathlib import Path


def calculate_score():
    result['Precision'] = result['tp'] / (result['tp'] + result['fp'])
    result['Recall'] = result['tp'] / (result['tp'] + result['fn'])
    result['Accuracy'] = (result['tp'] + result['tn']) / (result['tp'] + result['fp'] + result['fn'] + result['tn'])
    result['F-Score'] = (2 * result['tp']) / (2 * result['tp'] + result['fp'] + result['fn'])


original_path = Path('original')


def evaluation_benchmark():
    output = {}
    for path in original_path.glob('*.html'):
        # with gzip.open(path, 'rt', encoding='utf8') as f:
        #     html = f.read()
        # print(path)
        with open(path, 'rb') as f:
            html = f.read()
            # print(html)
        item_id = path.stem.split('.')[0]
        # if item_id != '11':
        #     continue
        output[item_id] = {'articleBody': trafilatura.extract(html,
                                                              no_fallback=False,
                                                              include_comments=False,
                                                              include_tables=True,
                                                              include_formatting=False)}
        # print(output[item_id])
    f_result = json.dumps(output, indent=4, ensure_ascii=False)
    # with open('../benchmark/output/b_output.json', 'w+') as f:
    # Confused..
    with open(f'tmp/result.json', 'w+', encoding='latin-1') as f:
        json.dump(output, f, indent=4)
        # f.write(f_result)


if __name__ == '__main__':
    running_time = []
    start_time = time.time()
    evaluation_benchmark()
    end_time = time.time()
    print(f'Program running time is: {(end_time - start_time)} s')
    # running_time.append((end_time - start_time))
    # print(f'The program running for {running_time} s, the average running time is {statistics.mean(running_time)}')
    # evaluate()
