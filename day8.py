# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 8
"""
import time

with open('input/day8.txt') as f:
    data = f.read()


def part1():
    """Part 1.
    """
    seq = [int(d) for d in data.split()]

    meta = []
    job_stack = [0]

    while seq:
        
        # Get a job off the stack.
        job = job_stack.pop()
        
        # Process the job if not empty.
        if job:
            for _ in range(job):
                meta.append(seq.pop(0))

        # Otherwise add jobs for self and children.
        else:
            c, m = seq.pop(0), seq.pop(0)
            
            # Add own job.
            job_stack.append(m)

            # Add empty child jobs.
            for _ in range(c):
                job_stack.append(0)

    return sum(meta)


def part2():
    """Part 2.

    Not proud of this... it's brutal. Especially considering how terse
    Part 1 is. Pfff...
    """

    def get_id():
        # Needs to avoid collisions and be in order.
        # Such a hack. For shame.
        return int((1e9*time.time())%1e12)

    seq = [int(d) for d in data.split()]
    
    all_meta = []
    complete = []
    parent_id = get_id()
    job_stack = [{'parent': parent_id, 'id': get_id(), 'meta': [], 'layer': 0}]
    layer = 0

    while seq:
        job = job_stack.pop()
        layer_ = job['layer']
        
        # Process the job if not empty.
        if job['meta']:
            for _ in range(job['meta'].pop()):
                this = seq.pop(0)
                job['meta'].append(this)
                all_meta.append(this)
            complete.append(job)
            parent_id = job['parent']


        else:
            c, m = seq.pop(0), seq.pop(0)
                    
            this_id = get_id()
            job_stack.append({'parent': parent_id, 'id': this_id, 'meta': [m], 'score': 0, 'children': c, 'layer': layer_})
            parent_id = this_id
            layer += 1
            layer_ = layer

            for c_ in range(c):
                
                job_stack.append({'parent': parent_id, 'id': get_id(), 'meta': [], 'layer': layer_})
            
    # Now we can process the result to traverse the tree and get the answer.
    # This is... awful.
    for item in complete:
        if item['children'] == 0:
            item['score'] = sum(item['meta'])
        else:
            children = [i for i in complete if i['parent']==item['id']]
            children_ = sorted(children, key=lambda d: d['id'])
            for idx in item['meta']:
                try:
                    item['score'] += children_[idx-1]['score']
                except:
                    pass

    result, = [i['score'] for i in complete if i['layer'] == 0]

    return result


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
